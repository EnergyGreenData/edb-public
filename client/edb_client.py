"""
EDB-P Evaluation Client

Simple client to evaluate AI systems against the Energy Decision Benchmark
by connecting to the official EDB evaluation service.

This client does NOT contain evaluation logic - it only submits responses
to the official API and retrieves results.
"""

import requests
from typing import Dict, List, Optional
from dataclasses import dataclass
import json


@dataclass
class SystemResponse:
    """Response format required by EDB"""
    decision: str
    reasoning: str
    confidence: float
    metadata: Optional[Dict] = None
    
    def to_dict(self) -> Dict:
        return {
            "decision": self.decision,
            "reasoning": self.reasoning,
            "confidence": self.confidence,
            "metadata": self.metadata or {}
        }


class EDBClient:
    """
    Client for EDB-P evaluation service.
    
    Usage:
        client = EDBClient(api_key="your-api-key")
        
        # Get a test case
        case = client.get_case("edb-p-001")
        
        # Your system generates a response
        response = SystemResponse(
            decision="La configuración es válida",
            reasoning="Tarifa 2.0TD permite hasta 15kW",
            confidence=0.92
        )
        
        # Evaluate
        result = client.evaluate_case("edb-p-001", response)
        print(f"Score: {result['overall_score']}")
    """
    
    def __init__(
        self,
        api_url: str = "https://api.vertical-agi.ai/edb/v1",  # Planned - not yet publicly available
        api_key: Optional[str] = None
    ):
        """
        Initialize EDB client.
        
        Args:
            api_url: Base URL of EDB evaluation API
            api_key: API key for authentication (required for evaluation)
        """
        self.api_url = api_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        
        if api_key:
            self.session.headers.update({
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            })
    
    def get_dataset_info(self) -> Dict:
        """Get dataset information (version, dimensions, total cases)"""
        response = self.session.get(f"{self.api_url}/dataset/info")
        response.raise_for_status()
        return response.json()
    
    def list_cases(self) -> List[str]:
        """List all test case IDs"""
        response = self.session.get(f"{self.api_url}/dataset/cases")
        response.raise_for_status()
        return response.json()["cases"]
    
    def get_case(self, case_id: str) -> Dict:
        """
        Get a specific test case.
        
        Returns input context and query, but NOT evaluation criteria
        (to prevent overfitting).
        
        Args:
            case_id: Test case ID (e.g., "edb-p-001")
        
        Returns:
            Case data with input context and query
        """
        response = self.session.get(f"{self.api_url}/dataset/case/{case_id}")
        response.raise_for_status()
        return response.json()
    
    def evaluate_case(
        self,
        case_id: str,
        system_response: SystemResponse
    ) -> Dict:
        """
        Evaluate a single case response.
        
        Args:
            case_id: Test case ID
            system_response: Your system's response
        
        Returns:
            Evaluation result with overall score and dimension scores
        """
        if not self.api_key:
            raise ValueError("API key required for evaluation")
        
        payload = {
            "case_id": case_id,
            "system_response": system_response.to_dict()
        }
        
        response = self.session.post(
            f"{self.api_url}/evaluate/case",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def evaluate_batch(
        self,
        system_name: str,
        responses: List[tuple[str, SystemResponse]]
    ) -> Dict:
        """
        Evaluate multiple cases in batch.
        
        Args:
            system_name: Name of your system
            responses: List of (case_id, system_response) tuples
        
        Returns:
            Aggregated results with dimension averages and summary
        """
        if not self.api_key:
            raise ValueError("API key required for evaluation")
        
        payload = {
            "system_name": system_name,
            "responses": [
                {
                    "case_id": case_id,
                    "system_response": response.to_dict()
                }
                for case_id, response in responses
            ]
        }
        
        response = self.session.post(
            f"{self.api_url}/evaluate/batch",
            json=payload
        )
        response.raise_for_status()
        return response.json()
    
    def evaluate_all(
        self,
        system_name: str,
        system_callable
    ) -> Dict:
        """
        Evaluate your system on all test cases.
        
        Args:
            system_name: Name of your system
            system_callable: Function that takes a case dict and returns SystemResponse
        
        Returns:
            Complete evaluation results
        """
        # Get all cases
        case_ids = self.list_cases()
        
        responses = []
        for case_id in case_ids:
            # Get case
            case = self.get_case(case_id)
            
            # Your system processes it
            system_response = system_callable(case)
            
            responses.append((case_id, system_response))
        
        # Evaluate batch
        return self.evaluate_batch(system_name, responses)


# Example usage
if __name__ == "__main__":
    # Initialize client
    client = EDBClient(api_key="your-api-key-here")
    
    # Get dataset info
    info = client.get_dataset_info()
    print(f"Dataset version: {info['version']}")
    print(f"Total cases: {info['total_cases']}")
    
    # Get a test case
    case = client.get_case("edb-p-001")
    print(f"\nCase: {case['id']}")
    print(f"Domain: {case['domain']}")
    print(f"Query: {case['input']['query']}")
    
    # Your system generates a response
    response = SystemResponse(
        decision="La configuración es válida",
        reasoning="Tarifa 2.0TD permite hasta 15kW y la potencia contratada es 4.6kW",
        confidence=0.92,
        metadata={"processing_time_ms": 150}
    )
    
    # Evaluate
    result = client.evaluate_case("edb-p-001", response)
    print(f"\nOverall score: {result['overall_score']:.2%}")
    print(f"Passed: {result['passed']}")
    print("\nDimension scores:")
    for dim, score in result['dimension_scores'].items():
        print(f"  {dim}: {score:.2%}")
