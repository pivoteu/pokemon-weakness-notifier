# Import Functions
import requests
import json

# Use Local Cache to get the data for type 1 (Normal)
try:
    with open('type-cache.json', 'r') as f:
        cache = json.load(f)
    data = cache.get('1', {})
except FileNotFoundError:
    print("Cache file not found.")
    data = {}

# Extract relevant information
name = data.get('name', 'Unknown')
relations = data.get('damage_relations', {})

# Cleanup label names for better readability
label = {
    'double_damage_from': 'Double Damage From',
    'double_damage_to': 'Double Damage To',
    'half_damage_from': 'Half Damage From',
    'half_damage_to': 'Half Damage To',
    'no_damage_from': 'No Damage From',
    'no_damage_to': 'No Damage To'
}

# Order the relations in a specific order for better readability
ordered_relations = [
    'double_damage_from' or "none",
    'double_damage_to' or "none",
    'half_damage_from' or "none",
    'half_damage_to' or "none",
    'no_damage_from' or "none",
    'no_damage_to' or "none"
]

# Create a new dictionary to hold the ordered relations
ordered_relations_dict = {relation: relations.get(relation, []) for relation in ordered_relations}

# Update the relations variable to use the ordered dictionary
relations = ordered_relations_dict
    
# Create a formatted string for the output
text = f"Damage Relations for {name.capitalize()}:\n"

# Print the damage relations
print(text)
for relation, types in relations.items():
    type_names = [t['name'] for t in types]
    type_names = [name.capitalize() for name in type_names]  # Capitalize the type names for better readability
# If there are not types, ignore the relation and skip printing anything
    if not type_names:
        continue    

# Print the relation and the corresponding types ignoring the relation if there are no types associated with it
    print(f"{label.get(relation, relation)}: {', '.join(type_names)}")

else:
    exit