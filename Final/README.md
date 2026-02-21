## FDA Notes FastAPI 

This simple FastAPI will manage user accounts, store personal notes, and fetch adverse events data from the FDA database for specific drugs.

## API Endpoints ##
1. **Accounts**: 

    - Create a new account: POST `/accounts` 
    
      ```
      {
        "username": "km"
      }
      ```
    - Retrieve account by ID: GET `/accounts/{id}` 
--- 

2. **Notes**: 

    - Add a note to an account: PUT `/accounts/{id}/notes`
    
      ```
      {
        "note": "i </3 pickle!"
      }
      ```
    - Read account notes: GET `/accounts/{id}/notes` 
--- 

3. **FDA Notes**: 

    - Fetch and save FDA adverse events for a drug: POST `/accounts/{id}/fda-notes`
    
      ```
      {
        "drug_name": "paracetamol",
        "limit": 5
      }
      ```
