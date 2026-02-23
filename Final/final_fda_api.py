import requests

def get_adverse_events(drug_name, limit=5):
    # Call the base url to get the information in the json file
    base_url = "https://api.fda.gov/drug/event.json"
    
    # Search for the specific drug with the limit of information shown
    params = {
        "search": f"patient.drug.medicinalproduct:{drug_name}",
        "limit": limit
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  
        
        data = response.json()
        
        results = data.get("results", [])
        
        if not results:
            print("No results found.")
            return
        
        print(f"\nAdverse Effects for", drug_name.lower().capitalize(), "!!")
        
        for i, event in enumerate(results, 1):
            print(f"\nPatient {i} Adverse Effect")
            
            reactions = event.get("patient", {}).get("reaction", [])
            
            # Get the adverse effect from each patient
            for reaction in reactions:
                print(" - Reaction:", reaction.get("reactionmeddrapt"))
    
    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)
    except Exception as e:
        print("Error:", e)


# Add Function to fetch adverse events from the FDA API and return them as notes 

def fetch_adverse_events(drug_name: str, limit: int = 5):
    base_url = "https://api.fda.gov/drug/event.json"
    
    params = {
        "search": f"patient.drug.medicinalproduct:{drug_name}",
        "limit": limit
    }
    
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    
    data = response.json()
    results = data.get("results", [])
    
    if not results:
        return "No adverse events found."
    
    notes = []
    
    for i, event in enumerate(results, 1):
        reactions = event.get("patient", {}).get("reaction", [])
        
        for reaction in reactions:
            reaction_text = reaction.get("reactionmeddrapt")
            if reaction_text:
                notes.append(f"Patient {i}: {reaction_text}")
    
    return "\n".join(notes)