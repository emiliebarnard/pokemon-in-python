import requests
import json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/nature/quirky"
quirky_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in quirky_data:
    print("key: ", key, "\n", "value:", quirky_data[key], "\n")
