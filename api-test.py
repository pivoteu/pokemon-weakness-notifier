# Import Functions
import requests

# Define URLS

api_url = "https://pokeapi.co/api/v2/type/1"

# Get the response from the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract relevant information
    name = data.get('name', 'Unknown')
    relations = data.get('damage_relations', {})

    #Print the damage relations
    print("Damage Relations for:", name)
    for relation, types in relations.items():
        type_names = [t['name'] for t in types]
        print(f"{relation}: {', '.join(type_names)}")
        
# Handle the case where the request was not successful  
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

