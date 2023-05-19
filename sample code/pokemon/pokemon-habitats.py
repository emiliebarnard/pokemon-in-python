import requests
import json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-habitat/forest/"
forest_data = requests.get(api_url).json()

"""# display all key-value pairs from the JSON data:
for key in forest_data:
    print("key: ", key, "\n", "value:", forest_data[key], "\n")"""

# display all Pokémon species that have this habitat:
for pokemon_species in forest_data["pokemon_species"]:
    print(pokemon_species["name"])
