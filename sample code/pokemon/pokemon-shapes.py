import requests
import json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-shape/ball"
ball_data = requests.get(api_url).json()

"""# display all key-value pairs from the JSON data:
for key in ball_data:
    print("key: ", key, "\n", "value:", ball_data[key], "\n")"""

# display all pokemon that can have this shape:
for pokemon_species in ball_data["pokemon_species"]:
    print(pokemon_species["name"])
