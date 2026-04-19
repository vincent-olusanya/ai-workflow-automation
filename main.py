"""
AI Workflow Automation System

A simple Python workflow automation script that:
1. Validates structured input
2. Applies decision logic
3. Sends data to a mock API client
4. Returns normalized output
"""

from typing import Any, Dict


def validate_input(data: Dict[str, Any]) -> bool:
    """Validate required fields and basic value quality."""
    required_fields = ["task_name", "priority", "payload"]

    if not all(field in data for field in required_fields):
        return False

    if not isinstance(data["task_name"], str) or not data["task_name"].strip():
        return False

    if not isinstance(data["priority"], str):
        return False

    if data["priority"].lower() not in {"high", "medium", "low"}:
        return False

    if not isinstance(data["payload"], dict):
        return False

    return True


def apply_decision_logic(data: Dict[str, Any]) -> Dict[str, Any]:
    """Apply simple workflow decision logic."""
    priority = data["priority"].lower()

    if priority == "high":
        status = "expedite"
    elif priority == "medium":
        status = "queue"
    else:
        status = "defer"

    return {
        "task_name": data["task_name"].strip(),
        "status": status,
        "payload": data["payload"],
    }


def mock_api_client(processed_data: Dict[str, Any]) -> Dict[str, Any]:
    """Simulate sending processed data to an external API."""
    return {
        "success": True,
        "message": "Data processed successfully",
        "data": processed_data,
    }


def normalize_output(api_response: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize API response output."""
    return {
        "ok": api_response.get("success", False),
        "result": api_response.get("data", {}),
        "info": api_response.get("message", ""),
    }


def run_workflow(data: Dict[str, Any]) -> Dict[str, Any]:
    """Run the full workflow pipeline."""
    if not validate_input(data):
        return {
            "ok": False,
            "result": {},
            "info": "Invalid input data",
        }

    processed = apply_decision_logic(data)
    api_response = mock_api_client(processed)
    return normalize_output(api_response)


if __name__ == "__main__":
    sample_input = {
        "task_name": "Review client request",
        "priority": "High",
        "payload": {"client_id": 101, "request_type": "analysis"},
    }

    output = run_workflow(sample_input)
    print("Workflow Output:")
    print(output)
