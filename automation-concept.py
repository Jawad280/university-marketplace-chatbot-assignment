# .env ----------------------------------------------------------------------------------------
GCP_PROJECT = ''
DB_URI = ''
VECTOR_DB_URI = ''
BACKEND_URL = ''
EVALUATOR_URL = ''
GITHUB_REPO = ''
GITHUB_REPO_TOKEN = ''
TEST_CASES_SHEETS_ENDPOINT = ''

# utils.py ----------------------------------------------------------------------------------------
import os
import requests
from github import Github
import psycopg2

# Connect DB
db = psycopg2.connect(os.getenv("DB_URI"))
vdb = psycopg2.connect(os.getenv("VECTOR_DB_URI"))

# Github repo
gh_repo = Github(os.getenv("GITHUB_REPO_TOKEN")).get_repo(os.getenv("GITHUB_REPO"))

def call_bot_api(branch_name: str, input_text: str):
    """Call chatbot API with test input."""
    url = f"{os.getenv('BACKEND_URL')}/chat?branch={branch_name}"
    return requests.post(url, json={"message": input_text}).json()

def call_evaluator(response, expected_elements):
    """Send chatbot response to evaluator API."""
    url = os.getenv("EVALUATOR_URL")
    payload = {"response": response, "expected": expected_elements}
    return requests.post(url, json=payload).json()

# gcp_utils.py  ----------------------------------------------------------------------------------------
import os

def gcp_create_instance(branch_name: str, prototype:bool=False):
    # Integrate with GCP compute engine
    instance_id = ...
    return instance_id

def gcp_set_traffic(instance_id: str, traffic_threshold: float):
    # Sets traffic to instance
    print(f"[GCP] Set traffic for instance '{instance_id}' to {traffic_threshold*100:.1f}%")


# version_control.py ----------------------------------------------------------------------------------------
from utils import gh_repo
from gcp_utils import gcp_create_instance, gcp_set_traffic

def create_feature(feature_name: str, traffic_threshold: float):
    branch_name = f'feature/{feature_name}'
    gh_repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=gh_repo.get_branch("main").commit.sha)
    
    # GCP instance spin-up
    instance_id = gcp_create_instance(branch_name, prototype=True)
    gcp_set_traffic(instance_id, traffic_threshold)
    
    return branch_name

# testing_script.py ----------------------------------------------------------------------------------------
from utils import call_bot_api, call_evaluator, db
import json

PASSING_SCORE = 0.80

def fetch_test_cases(branch_name: str):
    results = []
    test_cases_url = os.getenv("TEST_CASES_SHEETS_ENDPOINT")
    
    # Fetch test cases JSON from Sheets API endpoint
    resp = requests.get(test_cases_url)
    
    # Assuming the JSON response is a list of test case dicts:
    # Each test case: {"id": "test1", "input": "...", "expected_elements": [...]}
    test_cases = resp.json()

    for case in test_cases:
        bot_response = call_bot_api(branch_name, case["input"])
        eval_result = call_evaluator(bot_response, case["expected_elements"])
        score = eval_result.get("score", 0)

        results.append({"case_id": case["id"], "score": score})
    
    save_results(results)
    return all(r["score"] >= PASSING_SCORE for r in results)

def save_results(results):
    with db.cursor() as cur:
        for r in results:
            cur.execute(
                "INSERT INTO test_results (case_id, score) VALUES (%s, %s)",
                (r["case_id"], r["score"])
            )
    db.commit()

# policy_update.py ----------------------------------------------------------------------------------------
import os
import psycopg2
from utils import db

def save_policy_update(policy_text: str, editor: str):
    """
    Save the policy to the database
    """
    with db.cursor() as cur:
        cur.execute("""
            INSERT INTO policy_versions (policy_text, editor, timestamp)
            VALUES (%s, %s, NOW())
            RETURNING id
        """, (policy_text, editor))
        policy_id = cur.fetchone()[0]
    db.commit()
    return policy_id

def get_latest_policy():
    with db.cursor() as cur:
        cur.execute("SELECT policy_text FROM policy_versions ORDER BY timestamp DESC LIMIT 1")
        row = cur.fetchone()
        return row[0] if row else None
    
def approve_policy_change(policy_id: int, approver: str):
    """
    Mark a policy version as approved by an approver.
    """
    with db.cursor() as cur:
        cur.execute("""
            INSERT INTO policy_approvals (policy_id, approver, approved_at)
            VALUES (%s, %s, NOW())
        """, (policy_id, approver))
    db.commit()

def is_policy_fully_approved(policy_id: int, required_approvals=2):
    with db.cursor() as cur:
        cur.execute("""
            SELECT COUNT(*) FROM policy_approvals WHERE policy_id = %s
        """, (policy_id,))
        count = cur.fetchone()[0]
    return count >= required_approvals