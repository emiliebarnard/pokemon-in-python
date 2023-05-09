import requests
import json


# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/type/ghost"
ghost_data = requests.get(api_url).json()

"""# display all key-value pairs from the JSON data:
for key in ghost_data:
    print("key: ", key, "\n", "value:", ghost_data[key], "\n")

# display damage relations for this type:
print(ghost_data["damage_relations"])"""

# display a list of types that are very effective against this type:
for double_damage_from in ghost_data["damage_relations"]["double_damage_from"]:
    print(double_damage_from["name"])

# display a list of types this type is very effect against:
for double_damage_to in ghost_data["damage_relations"]["double_damage_to"]:
    print(double_damage_to["name"])
