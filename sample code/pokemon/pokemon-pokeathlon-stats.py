import requests
import json


# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokeathlon-stat/jump"
jump_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in jump_data:
    print("key: ", key, "\n", "value:", jump_data[key], "\n")

print("The following Natures increase the", jump_data["name"] ,"stat:")
for nature in jump_data["affecting_natures"]["increase"]:
    print(nature["nature"]["name"], "increases by a max of", nature["max_change"])

print("\nThe following Natures decrease the", jump_data["name"] ,"stat:")
for nature in jump_data["affecting_natures"]["decrease"]:
    print(nature["nature"]["name"], "decreases by a max of", nature["max_change"]*-1)
