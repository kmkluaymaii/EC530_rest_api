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

# Test the function by searching for the adverse effect of 
# Paracetamol with the limit of ten patients history
get_adverse_events("PARACETAMOL", 10)