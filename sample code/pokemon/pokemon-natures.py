import requests
import json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/nature/sassy"
sassy_data = requests.get(api_url).json()

""" # display all key-value pairs from the JSON data:
for key in sassy_data:
    print("key: ", key, "\n", "value:", sassy_data[key], "\n") """

print("A", sassy_data["name"], "Pokémon has the following attributes:\n",
      "Increased stat:", sassy_data["increased_stat"]["name"],"\n",
      "Decreased stat:", sassy_data["decreased_stat"]["name"],"\n",
      "Likes this flavor:", sassy_data["likes_flavor"]["name"],"\n",
      "Dislikes this flavor:", sassy_data["hates_flavor"]["name"])