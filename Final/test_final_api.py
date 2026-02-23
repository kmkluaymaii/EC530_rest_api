import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from final_rest_api import app, accounts  

client = TestClient(app)

def setup_function():
    """Reset accounts before each test"""
    accounts.clear()
    # Reset global account_id
    from final_rest_api import account_id
    from importlib import reload
    import final_rest_api
    final_rest_api.account_id = 0

def test_create_account():
    response = client.post("/accounts", json={"username": "alice"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"
    assert data["id"] == 1
    assert data["note"] == ""

    # Test duplicate username
    response_dup = client.post("/accounts", json={"username": "alice"})
    assert response_dup.status_code == 409

def test_retrieve_account():
    # Create account first
    client.post("/accounts", json={"username": "bob"})
    response = client.get("/accounts/1")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "bob"

    # Test non-existent account
    response_404 = client.get("/accounts/999")
    assert response_404.status_code == 404

def test_add_and_read_notes():
    client.post("/accounts", json={"username": "carol"})

    # Add note
    response = client.put("/accounts/1/notes", json={"note": "Test note"})
    assert response.status_code == 200
    data = response.json()
    assert data["note"] == "Test note"

    # Read note
    response = client.get("/accounts/1/notes")
    assert response.status_code == 200
    assert response.json() == {"note": "Test note"}

    # Read note for account with no note
    client.post("/accounts", json={"username": "dave"})
    response_no_note = client.get("/accounts/2/notes")
    assert response_no_note.status_code == 404

def test_save_fda_notes():
    client.post("/accounts", json={"username": "eve"})

    # Patch fetch_adverse_events to avoid real API calls
    with patch("final_rest_api.fetch_adverse_events") as mock_fetch:
        mock_fetch.return_value = "FDA adverse event summary"
        response = client.post("/accounts/1/fda-notes", json={"drug_name": "aspirin", "limit": 5})
        assert response.status_code == 200
        data = response.json()
        assert data["note"] == "FDA adverse event summary"
        mock_fetch.assert_called_once_with("aspirin", 5)

    # Test account not found
    response_404 = client.post("/accounts/999/fda-notes", json={"drug_name": "aspirin", "limit": 5})
    assert response_404.status_code == 404

    # Test HTTPError handling
    with patch("final_rest_api.fetch_adverse_events") as mock_fetch:
        import requests
        mock_fetch.side_effect = requests.exceptions.HTTPError
        response_error = client.post("/accounts/1/fda-notes", json={"drug_name": "ibuprofen", "limit": 3})
        assert response_error.status_code == 500