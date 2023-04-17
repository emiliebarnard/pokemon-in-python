# display the original 151 pokemon
# tutorial edited to Python from https://medium.com/@sergio13prez/fetching-them-all-poke-api-62ca580981a2

import requests

api_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
response = requests.get(api_url)
print(response.json()) # not very fancy formatting but it works for testing