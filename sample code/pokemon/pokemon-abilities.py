# display the original 151 pokemon
# tutorial edited to Python from https://medium.com/@sergio13prez/fetching-them-all-poke-api-62ca580981a2

import requests, json

api_url = "https://pokeapi.co/api/v2/ability/cute-charm/"
cute_charm_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in cute_charm_data:
    print("key: ", key, "\n", "value:", cute_charm_data[key], "\n")

for key in cute_charm_data:
    print(key)
# display 