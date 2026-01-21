#!/usr/bin/env python3
"""
EDB Quickstart - Evaluate your AI system on the Energy Decision Benchmark

Usage:
    1. Request API access at https://vertical-agi.ai?source=edb-benchmark
    2. Set your API key below
    3. Run: python quickstart.py
"""

import requests
import json

API_URL = "https://api.watioverse.com"
API_KEY = "your_api_key_here"  # Replace with your key


def get_test_case(case_id: str) -> dict:
    """Fetch a test case from the dataset."""
    response = requests.get(f"{API_URL}/dataset/case/{case_id}")
    response.raise_for_status()
    return response.json()


def evaluate_response(case_id: str, decision: str, reasoning: str, confidence: float) -> dict:
    """Submit your system's response for evaluation."""
    response = requests.post(
        f"{API_URL}/evaluate/case",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "X-EDB-Client": "EDB-Research",
            "Content-Type": "application/json",
        },
        json={
            "case_id": case_id,
            "system_response": {
                "decision": decision,
                "reasoning": reasoning,
                "confidence": confidence,
            },
        },
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # 1. Get a test case
    case = get_test_case("edb-p-001")
    print("Test Case:")
    print(json.dumps(case, indent=2))
    
    # 2. Your AI system processes the case and generates a response
    # (Replace this with your actual system's output)
    my_decision = "Maintain current power contract"
    my_reasoning = "Based on consumption patterns, current setup is optimal"
    my_confidence = 0.85
    
    # 3. Submit for evaluation
    if API_KEY != "your_api_key_here":
        result = evaluate_response("edb-p-001", my_decision, my_reasoning, my_confidence)
        print("\nEvaluation Result:")
        print(json.dumps(result, indent=2))
    else:
        print("\n⚠️  Set your API_KEY to run evaluation")
        print("   Request access at: https://vertical-agi.ai?source=edb-benchmark")
