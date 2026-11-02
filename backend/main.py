from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from jupyter_bridge import router as jupyter_router


import ast
import json
import os
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
from pathlib import Path

from test_cases import TEST_CASES, PUBLIC_TEST_COUNT, PUBLIC_CASE_DETAILS, build_setup


def public_test_count(question_id):
    return min(
        PUBLIC_TEST_COUNT.get(question_id, 2),
        len(TEST_CASES[question_id]["tests"]),
    )

from problem_specs import enrich_question
from question_bank import (
    QUESTIONS,
    public_question,
    get_question,
)


from ml_benchmark import router as ml_benchmark_router

app = FastAPI(
    title="ModelMind More Practice Evaluator",
    version="1.0.0"
)

# Allow the deployed Question Bank and local development frontends.
# Keep a single CORSMiddleware configuration.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://modelmind-more-practise.onrender.com",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(jupyter_router)
app.include_router(ml_benchmark_router)

# ---------------------------------------------------------
# Question Bank API
# ---------------------------------------------------------

def practice_mode(question):
    if question.get("type") in ("Coding", "Debugging") and question.get("starterCode"):
        return "coding"
    if question.get("type") == "Mathematics":
        try:
            float(str(question.get("expectedAnswer", "")))
            return "numerical"
        except (ValueError, TypeError):
            pass
    return "theory"


@app.get("/api/questions")
def get_questions():
    result = []

    for question in QUESTIONS:
        question_id = question["id"]
        mode = practice_mode(question)

        case = (
            TEST_CASES.get(question_id, {})
            if mode == "coding"
            else {}
        )

        all_tests = case.get("tests", {})

        public_count = (
            public_test_count(question_id)
            if case
            else 0
        )

        details = PUBLIC_CASE_DETAILS.get(
            question_id, {}
        )

        visible_tests = []

        for name in list(all_tests)[:public_count]:
            spec = details.get(name, {})

            visible_tests.append({
                "name": name,
                "input": spec.get("input"),
                "expected": (
                    repr(spec["expected"])
                    if "expected" in spec
                    else None
                ),
            })

        result.append({
            **enrich_question(
                public_question(question)
            ),
            "answer": float(question["expectedAnswer"]) if mode == "numerical" and question.get("expectedAnswer") is not None else None,
            "practiceMode": mode,
            "testsAvailable": bool(case),
            "visibleTests": visible_tests,
            "publicTestCount": public_count,
            "hiddenTestCount": max(
                0,
                len(all_tests) - public_count
            ),
        })

    # MODELMIND_QA_ONEBATCH_OVERRIDES_V1: display-only question clarity overlays.
    import json as _mm_json
    from pathlib import Path as _mm_Path
    _mm_overrides_path = _mm_Path(__file__).resolve().parent.parent / "public" / "modelmind-qa-onebatch-overrides.json"
    if _mm_overrides_path.is_file():
        _mm_overrides = _mm_json.loads(_mm_overrides_path.read_text(encoding="utf-8"))
        for _mm_q in result:
            if _mm_q.get("id") in _mm_overrides:
                _mm_q.update(_mm_overrides[_mm_q["id"]])
    return result


# ---------------------------------------------------------
# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

RUNS_DIR = BASE_DIR / "runs"
RUNS_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# Security limits
# ---------------------------------------------------------

BLOCKED_IMPORTS = {
    "os",
    "subprocess",
    "socket",
    "shutil",
    "pathlib",
    "ctypes",
    "multiprocessing",
    "threading",
    "asyncio",
    "importlib",
    "winreg",
    "requests",
    "urllib",
    "http",
    "ftplib",
    "telnetlib",
}

BLOCKED_CALLS = {
    "open",
    "eval",
    "exec",
    "compile",
    "__import__",
}

BLOCKED_ATTRIBUTES = {
    "system",
    "popen",
    "spawn",
    "remove",
    "unlink",
    "rmtree",
    "walk",
    "getenv",
}

MAX_CODE_LENGTH = 30000
MAX_AST_NODES = 6000
TIMEOUT_SECONDS = 8


# ---------------------------------------------------------
# Request model
# ---------------------------------------------------------

class RunRequest(BaseModel):
    question_id: str
    mode: str = "submit"
    code: str = Field(
        min_length=1,
        max_length=MAX_CODE_LENGTH
    )


# ---------------------------------------------------------
# AST validation
# ---------------------------------------------------------

def validate_code(code: str):

    if len(code) > MAX_CODE_LENGTH:
        raise ValueError(
            f"Code exceeds {MAX_CODE_LENGTH} characters."
        )

    tree = ast.parse(code, mode="exec")

    nodes = list(ast.walk(tree))

    if len(nodes) > MAX_AST_NODES:
        raise ValueError(
            "Code is too large or complex."
        )

    for node in nodes:

        # Import validation
        if isinstance(node, ast.Import):

            for alias in node.names:

                root = alias.name.split(".")[0]

                if root in BLOCKED_IMPORTS:
                    raise ValueError(
                        f"Import '{root}' is not allowed."
                    )

        # from x import y
        elif isinstance(node, ast.ImportFrom):

            root = (node.module or "").split(".")[0]

            if root in BLOCKED_IMPORTS:
                raise ValueError(
                    f"Import '{root}' is not allowed."
                )

        # Dangerous function calls
        elif isinstance(node, ast.Call):

            if (
                isinstance(node.func, ast.Name)
                and node.func.id in BLOCKED_CALLS
            ):
                raise ValueError(
                    f"Call '{node.func.id}()' is not allowed."
                )

        # Dangerous attributes
        elif isinstance(node, ast.Attribute):

            if node.attr in BLOCKED_ATTRIBUTES:
                raise ValueError(
                    f"Attribute '{node.attr}' is not allowed."
                )

    return tree


# ---------------------------------------------------------
# Runner generation
# ---------------------------------------------------------

def make_runner(
    setup_code: str,
    student_code: str,
    question_id: str,
    mode: str = "submit"
):

    all_tests = TEST_CASES[question_id]["tests"]
    public_count = public_test_count(question_id)
    tests = dict(list(all_tests.items())[:public_count]) if mode == "run" else all_tests

    test_names = list(tests.keys())

    test_items = []

    for test_name in test_names:

        test_items.append(
            f"({test_name!r}, "
            f"test_cases.TEST_CASES[{question_id!r}]"
            f"['tests'][{test_name!r}])"
        )

    tests_source = ",\n".join(test_items)

    runner = f"""
import json
import traceback
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_cases


namespace = {{}}

result = {{
    "status": "failed",
    "score": 0,
    "passed": 0,
    "total": {len(test_names)},
    "tests": [],
    "error": None
}}


try:

    # -----------------------------------------------------
    # Setup hidden data
    # -----------------------------------------------------

    setup_code = {setup_code!r}

    if setup_code.strip():

        exec(
            compile(
                setup_code,
                "<setup>",
                "exec"
            ),
            namespace,
            namespace
        )


    # -----------------------------------------------------
    # Student code
    # -----------------------------------------------------

    student_code = {student_code!r}

    exec(
        compile(
            student_code,
            "<student>",
            "exec"
        ),
        namespace,
        namespace
    )


    # -----------------------------------------------------
    # Hidden tests
    # -----------------------------------------------------

    test_items = [
        {tests_source}
    ]


    # Public diagnostic examples are explicitly tied to a question ID.
    # The expected values are maintained beside tests in test_cases.py.
    public_case_specs = test_cases.PUBLIC_CASE_DETAILS.get({question_id!r}, {{}})

    for test_name, test_function in test_items:

        try:

            test_function(namespace)

            result["passed"] += 1

            result["tests"].append({{
                "name": test_name,
                "passed": True
            }})

        except AssertionError as exc:

            result["tests"].append({{
                "name": test_name,
                "passed": False,
                "error": str(exc) or "Assertion failed"
            }})

        except Exception as exc:

            result["tests"].append({{
                "name": test_name,
                "passed": False,
                "error": (
                    f"{{type(exc).__name__}}: {{exc}}"
                )
            }})


        # Diagnostic values are returned for verified public tests only.
        # Direct function cases are evaluated independently for display; the
        # original assertion remains the source of truth for pass/fail.
        if len(result["tests"]) <= {public_count} and test_name in public_case_specs:
            spec = public_case_specs[test_name]
            detail = {{
                "input": spec["input"],
                "expected": repr(spec["expected"]),
                "hidden": False,
            }}
            try:
                if "function" in spec:
                    args = spec.get("args", [spec.get("argument")])
                    computed = namespace[spec["function"]](*args)
                else:
                    computed = namespace[spec["variable"]]
                if hasattr(computed, "tolist"):
                    computed = computed.tolist()
                detail["actual"] = repr(computed)
            except Exception as exc:
                detail["actual"] = f"{{type(exc).__name__}}: {{exc}}"
            result["tests"][-1].update(detail)

    # -----------------------------------------------------
    # Score
    # -----------------------------------------------------

    if result["total"] > 0:

        result["score"] = round(
            result["passed"]
            / result["total"]
            * 100
        )

    else:

        result["score"] = 0


    if result["passed"] == result["total"]:

        result["status"] = "passed"

    else:

        result["status"] = "failed"


except SyntaxError as exc:

    result["error"] = (
        f"SyntaxError: {{exc}}"
    )


except Exception as exc:

    result["error"] = (
        f"{{type(exc).__name__}}: {{exc}}"
    )

    result["traceback"] = traceback.format_exc()


print(
    "__MODELMIND_RESULT__"
    + json.dumps(result)
)
"""

    return textwrap.dedent(runner)


# ---------------------------------------------------------
# Root
# ---------------------------------------------------------

@app.get("/")
def root():

    return {
        "name": "ModelMind More Practice Evaluator",
        "status": "running"
    }


# ---------------------------------------------------------
# Health
# ---------------------------------------------------------

@app.get("/api/health")
def health():

    return {
        "status": "ok"
    }


# ---------------------------------------------------------
# Run code
# ---------------------------------------------------------

@app.post("/api/run")
def run_code(request: RunRequest):
    # Host subprocess execution is only allowed for trusted local development.
    if os.environ.get("MODELMIND_LOCAL_JUDGE", "").lower() != "true":
        raise HTTPException(status_code=503, detail="Local code execution is disabled. Use a properly isolated judge for public deployment.")

    question_id = request.question_id
    question = get_question(question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Unknown question_id.")
    if practice_mode(question) != "coding":
        raise HTTPException(status_code=400, detail="Only coding challenges can be executed.")

    # -----------------------------------------------------
    # Check question
    # -----------------------------------------------------

    if question_id not in TEST_CASES:

        return {"status": "not_available", "tests_available": False, "score": 0, "passed": 0, "total": 0, "tests": [], "stdout": "", "stderr": "", "error": "Automated tests are not yet available for this exercise.", "execution_time_ms": 0}


    if request.mode not in ("run", "submit"):
        raise HTTPException(status_code=400, detail="mode must be run or submit")
    total_tests = len(TEST_CASES[question_id]["tests"])
    if request.mode == "run":
        total_tests = min(public_test_count(question_id), total_tests)


    # -----------------------------------------------------
    # Validate code
    # -----------------------------------------------------

    try:

        validate_code(request.code)

    except SyntaxError as exc:

        return {
            "status": "failed",
            "tests_available": True,
            "score": 0,
            "passed": 0,
            "total": total_tests,
            "tests": [],
            "stdout": "",
            "stderr": "",
            "error": f"SyntaxError: {exc}",
            "execution_time_ms": 0
        }

    except ValueError as exc:

        return {
            "status": "failed",
            "tests_available": True,
            "score": 0,
            "passed": 0,
            "total": total_tests,
            "tests": [],
            "stdout": "",
            "stderr": "",
            "error": str(exc),
            "execution_time_ms": 0
        }


    # -----------------------------------------------------
    # Temporary execution directory
    # -----------------------------------------------------

    run_dir = Path(
        tempfile.mkdtemp(
            prefix="run_",
            dir=RUNS_DIR
        )
    )

    runner_path = run_dir / "runner.py"
    shutil.copy2(BASE_DIR / "test_cases.py", run_dir / "test_cases.py")


    setup_code = (
        ""
        if question_id in {
            "numpy-basic-001",
            "pandas-basic-001",
            "pandas-medium-001",
        }
        else build_setup(question_id)
    )


    runner_path.write_text(
        make_runner(
            setup_code,
            request.code,
            question_id,
            request.mode
        ),
        encoding="utf-8"
    )


    # -----------------------------------------------------
    # Environment
    # -----------------------------------------------------

    env = os.environ.copy()

    env["PYTHONNOUSERSITE"] = "1"

    env["PYTHONPATH"] = str(BASE_DIR)


    # -----------------------------------------------------
    # Execute
    # -----------------------------------------------------

    start = time.perf_counter()

    process = None

    try:

        process = subprocess.Popen(
            [
                sys.executable,
                "-I",
                str(runner_path)
            ],
            cwd=str(run_dir),
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
            shell=False
        )


        try:

            stdout, stderr = process.communicate(
                timeout=TIMEOUT_SECONDS
            )

        except subprocess.TimeoutExpired:

            process.kill()

            try:

                stdout, stderr = process.communicate(
                    timeout=1
                )

            except subprocess.TimeoutExpired:

                stdout = ""
                stderr = ""


            return {
                "status": "failed",
                "tests_available": True,
                "score": 0,
                "passed": 0,
                "total": total_tests,
                "tests": [],
                "stdout": "",
                "stderr": stderr[-10000:],
                "error": (
                    f"Execution timed out after "
                    f"{TIMEOUT_SECONDS} seconds."
                ),
                "execution_time_ms": round(
                    (time.perf_counter() - start) * 1000
                )
            }


        execution_ms = round(
            (time.perf_counter() - start) * 1000
        )


        # -------------------------------------------------
        # Find evaluator result
        # -------------------------------------------------

        marker = "__MODELMIND_RESULT__"

        result = None

        result_line = None

        for line in stdout.splitlines():

            if line.startswith(marker):

                result_line = line

                try:

                    result = json.loads(
                        line[len(marker):]
                    )

                except json.JSONDecodeError:

                    result = None


        # -------------------------------------------------
        # Evaluator failure
        # -------------------------------------------------

        if result is None:

            return {
                "status": "failed",
                "tests_available": True,
                "score": 0,
                "passed": 0,
                "total": total_tests,
                "tests": [],
                "stdout": stdout[-10000:],
                "stderr": stderr[-10000:],
                "error": (
                    "Evaluator process did not "
                    "return a valid result."
                ),
                "execution_time_ms": execution_ms
            }


        # -------------------------------------------------
        # Student output
        # -------------------------------------------------

        clean_stdout = stdout

        if result_line:

            clean_stdout = stdout.replace(
                result_line,
                ""
            ).strip()


        if request.mode == "submit":
            for idx, test in enumerate(result.get("tests", [])):
                if idx >= public_test_count(question_id):
                    passed = bool(test.get("passed", False))
                    test.clear()
                    test.update({
                        "name": f"Hidden test {idx - public_test_count(question_id) + 1}",
                        "passed": passed,
                        "hidden": True,
                    })
        result["tests_available"] = True

        result["stdout"] = clean_stdout[-10000:] if request.mode == "run" else ""

        result["stderr"] = stderr[-10000:] if request.mode == "run" else ""

        result["execution_time_ms"] = execution_ms

        return result


    finally:

        shutil.rmtree(
            run_dir,
            ignore_errors=True
        )
        
        
class CheckAnswerRequest(BaseModel):
    question_id: str
    selected_option: int | None = None
    answer: str = ""


@app.post("/api/check-answer")
def check_answer(request: CheckAnswerRequest):
    question = get_question(request.question_id)

    if question is None:
        raise HTTPException(
            status_code=404,
            detail="Question not found."
        )

    if practice_mode(question) != "numerical":
        raise HTTPException(status_code=400, detail="Only numerical questions can be graded. Theory questions are read-only.")

    import math
    try:
        supplied = float(request.answer.strip())
        expected = float(question["expectedAnswer"])
    except (ValueError, TypeError, KeyError):
        raise HTTPException(status_code=400, detail="Please enter a valid number.")

    if not math.isfinite(supplied) or not math.isfinite(expected):
        raise HTTPException(status_code=400, detail="The answer must be a finite number.")
    tolerance = max(0.001, abs(expected) * 0.0001)
    correct = abs(supplied - expected) <= tolerance
    return {"correct": correct, "explanation": question.get("explanation") or
            f"Expected answer: {expected:g} (tolerance ±{tolerance:g})", "grading_method": "numerical"}
