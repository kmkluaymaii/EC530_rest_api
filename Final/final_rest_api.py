from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from final_fda_api import fetch_adverse_events
import requests

app = FastAPI()

accounts = {}
account_id = 0

class AccountCreate(BaseModel):
    username: str
    
class Account(BaseModel):
    username: str
    id: int
    note: str

class Note(BaseModel):
    note: str

class FDANoteRequest(BaseModel):
    drug_name: str
    limit: int = 5

@app.post("/accounts", response_model=Account)
def create_account(account: AccountCreate):
    for a in accounts.values():
        if a["username"] == account.username:
            raise HTTPException(status_code=409, detail="Username already exists")
    
    global account_id
    account_id += 1
    new_account = {
        "username": account.username,
        "id": account_id,
        "note": ""
    }
    accounts[account_id] = new_account
    return new_account

@app.get("/accounts/{id}", response_model=Account)
def retrieve_account(id: int):
    if id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts[id]

@app.put("/accounts/{id}/notes", response_model=Account)
def add_notes(id:int, notes: Note):
    if id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    
    accounts[id]["note"] = notes.note
    return accounts[id]

@app.get("/accounts/{id}/notes")    
def read_notes(id:int):
    if id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    
    if not accounts[id]["note"]:
        raise HTTPException(status_code=404, detail="No notes found")
    
    return {"note": accounts[id]["note"]}   
    
@app.post("/accounts/{id}/fda-notes")
def save_fda_notes(id: int, request: FDANoteRequest):
    if id not in accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    
    try:
        notes = fetch_adverse_events(request.drug_name, request.limit)
        accounts[id]["note"] = notes
        return accounts[id]
    
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=500, detail="Error fetching FDA data")