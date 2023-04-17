# display the original 151 pokemon
# tutorial edited to Python from https://medium.com/@sergio13prez/fetching-them-all-poke-api-62ca580981a2

import requests, json

api_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get(api_url)
pokemon_json = response.json() # the first 151 pokemon in json (dictionary of count, next, previous, results)

for pokemon in pokemon_json["results"]: # each pokemon is a dictionary with a name and url
    print(pokemon["name"], pokemon["url"])