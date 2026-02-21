## User Stories for this Rest API ##
- As a user, I can create an account with a username.
- As a user, I can retrieve my account by id.
- If username already exists → return 409.
- As a user, I can add text notes
- As a user, I can read my text notes

## API Endpoints ##
1. **Create an Account**: POST `/accounts`

    - Request body: 
    
      ```
      {
        "username": "pippi"
      }
      ```
    - Response: 
    
      ```
      {
        "username": "pippi",
        "id": 1,
        "note": ""
      }
      ```
    - Error:  
      - Returned `409` if the username already exists.

--- 

2. **Retrieve an Account:** GET `/accounts/{id}`

    - Example: 
    
      ```
      GET /accounts/1
      ```
    - Response:
    
      ```
      {
        "username": "pippi",
        "id": 1,
        "note": ""
      }
      ```
    - Error:  
      - Returned `404` if the account not found.
     
---
3. **Add Notes:** PUT `/accounts/{id}/notes`

    - Request body: 
    
      ```
      {
        "note": "I <3 pickle!!"
      }
      ```
    - Response:
    
      ```
      {
        "username": "pippi",
        "id": 1,
        "note": "I <3 pickle!!"
      }
      ```
    - Error:  
      - Returned `404` if the account not found.

---
4. **Add Notes**: GET `/accounts/{id}/notes`

    - Example: 
    
      ```
      GET /accounts/1/notes

      ```
    - Response:
    
      ```
      {
        "note": "I <3 pickle!!"
      }
      ```
    - Error:  
      - Returned `404` if the account not found or no notes found.
