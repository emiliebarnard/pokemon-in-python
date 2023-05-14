import requests
import json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-species/butterfree"
butterfree_data = requests.get(api_url).json()

""" # display all key-value pairs from the JSON data:
for key in butterfree_data:
    print("key: ", key, "\n", "value:", butterfree_data[key], "\n")"""

# display this Pokemon species' flavor text in English:
for entry in butterfree_data["flavor_text_entries"]:
    if entry["language"]["name"] == "en":
        flavor_text = entry["flavor_text"]
        print(flavor_text)

# display this Pokemon species' genus in Chinese:
for genus in butterfree_data["genera"]:
    if genus["language"]["name"] == "zh-Hant":
        print(genus["genus"])
