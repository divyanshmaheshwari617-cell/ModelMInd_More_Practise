"""Read-only coverage and benchmark mapping report for the existing ModelMind project."""
from __future__ import annotations
import csv
from collections import Counter, defaultdict
from pathlib import Path
from question_bank import QUESTIONS
from test_cases import TEST_CASES, PUBLIC_TEST_COUNT

OUT = Path(__file__).resolve().parents[1] / 'modelmind_coverage_reports'
OUT.mkdir(exist_ok=True)
LEVELS = ('Basic', 'Medium', 'Advanced')
rows = []
for q in QUESTIONS:
    qid = q['id']; mode = q.get('type',''); coding = mode in ('Coding','Debugging') and bool(q.get('starterCode'))
    suite = TEST_CASES.get(qid,{}) if coding else {}
    all_tests = suite.get('tests',{}) if isinstance(suite,dict) else {}
    n = len(all_tests)
    pub = min(PUBLIC_TEST_COUNT.get(qid,2), n) if n else 0
    tags = q.get('tags') or []
    rows.append({'id':qid,'topic':q.get('topic','Unknown'),'level':q.get('level','Unknown'),
                 'type':mode, 'title':q.get('title',''), 'tags':'|'.join(map(str,tags)),
                 'coding':int(coding),'total_tests':n,'public_tests':pub,'hidden_tests':max(0,n-pub),
                 'status':('not_coding' if not coding else 'no_tests' if n==0 else
                           'below_public_target' if pub<5 else 'below_hidden_target' if n-pub<80 else 'count_target_met'),
                 'contract_review_required':int(coding and not n)})
with (OUT/'question_coverage.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f, fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
by_topic=defaultdict(list)
for r in rows:by_topic[r['topic']].append(r)
summary=[]
for topic, items in sorted(by_topic.items()):
    for level in LEVELS:
        sub=[q for q in items if q['level']==level]
        summary.append({'topic':topic,'level':level,'questions':len(sub),
                        'coding':sum(q['coding'] for q in sub),
                        'coding_without_tests':sum(q['status']=='no_tests' for q in sub),
                        'coding_below_5_public':sum(q['coding'] and q['public_tests']<5 for q in sub),
                        'coding_below_80_hidden':sum(q['coding'] and q['hidden_tests']<80 for q in sub)})
with (OUT/'topic_level_coverage.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=summary[0].keys());w.writeheader();w.writerows(summary)
print('ACTIVE QUESTIONS:',len(rows));print('TOPICS:',len(by_topic));print('CODING:',sum(r['coding'] for r in rows))
print('CODING WITHOUT TESTS:',sum(r['status']=='no_tests' for r in rows))
print('CODING BELOW 5 PUBLIC:',sum(r['coding'] and r['public_tests']<5 for r in rows))
print('CODING BELOW 80 HIDDEN:',sum(r['coding'] and r['hidden_tests']<80 for r in rows))
print('TOPIC/LEVEL COMBINATIONS WITH ZERO QUESTIONS:',sum(r['questions']==0 for r in summary))
print('Note: tags are topic metadata, not a verified concept taxonomy.')
print('Reports saved:',OUT)
