from fastapi.testclient import TestClient
import rest_api
from rest_api import app

client = TestClient(app)

def setup_function():
    rest_api.accounts.clear()
    rest_api.account_id = 0


def test_create_account():
    response = client.post("/accounts", json={"username": "pippi"})
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_duplicate_username():
    client.post("/accounts", json={"username": "pippi"})
    response = client.post("/accounts", json={"username": "pippi"})
    assert response.status_code == 409


def test_retrieve_account():
    response = client.post("/accounts", json={"username": "km"})
    account_id = response.json()["id"]

    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 200
    assert response.json()["username"] == "km"

def test_retrieve_nonexistent_account():
    response = client.get("/accounts/999")
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Account not found"

def test_add_and_read_notes():
    response = client.post("/accounts", json={"username": "osama"})
    account_id = response.json()["id"]

    client.put(
        f"/accounts/{account_id}/notes",
        json={"note": "i love fastapi <3"}
    )

    response = client.get(f"/accounts/{account_id}/notes")
    assert response.status_code == 200
    assert response.json()["note"] == "i love fastapi <3"
    
def test_read_notes_when_empty():
    response = client.post("/accounts", json={"username": "km"})
    account_id = response.json()["id"]

    response = client.get(f"/accounts/{account_id}/notes")
    
    assert response.status_code == 404
    assert response.json()["detail"] == "No notes found"
    
def test_add_note_to_nonexistent_account():
    response = client.put(
        "/accounts/999/notes",
        json={"note": "hello"}
    )
    
    assert response.status_code == 404
    assert response.json()["detail"] == "Account not found"
    