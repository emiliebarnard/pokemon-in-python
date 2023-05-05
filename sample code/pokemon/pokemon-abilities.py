# display the original 151 pokemon
# tutorial edited to Python from https://medium.com/@sergio13prez/fetching-them-all-poke-api-62ca580981a2

import requests, json

api_url = "https://pokeapi.co/api/v2/ability/1/"
response = requests.get(api_url)
pokemon_json = response.json() # the first 151 pokemon in json (dictionary of count, next, previous, results)

for key in pokemon_json:
    print(key, pokemon_json[key])
    
