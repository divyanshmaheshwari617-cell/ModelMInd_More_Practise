import sys
import json
from pathlib import Path

root = Path.cwd()
sys.path.insert(0, str(root / "backend"))

from question_bank import QUESTIONS
from test_cases import TEST_CASES, build_setup

keywords = (
    "regression",
    "ridge",
    "lasso",
    "elasticnet",
    "polynomial",
)

selected = []

for question in QUESTIONS:
    title = question.get("title", "")
    topic = question.get("topic", "")
    text = f"{title} {topic}".lower()

    if not any(word in text for word in keywords):
        continue

    qid = question["id"]

    record = {
        "id": qid,
        "title": title,
        "topic": topic,
        "level": question.get("level"),
        "type": question.get("type"),
        "question": question.get("question"),
        "starterCode": question.get("starterCode"),
        "existingTests": list(
            TEST_CASES.get(qid, {}).get("tests", {})
        ),
        "setupCode": build_setup(qid),
    }

    selected.append(record)

    print("=" * 60)
    print("ID:", qid)
    print("TITLE:", title)
    print("LEVEL:", record["level"])
    print("EXISTING TESTS:", len(record["existingTests"]))
    print("DESCRIPTION:", record["question"])
    print("STARTER CODE:")
    print(record["starterCode"])

output = root / "modelmind_regression_audit.json"

output.write_text(
    json.dumps(selected, indent=2, ensure_ascii=False),
    encoding="utf-8"
)

print("\nTotal regression-related questions:", len(selected))
print("Report:", output)
