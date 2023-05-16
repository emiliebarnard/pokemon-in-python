import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/egg-group/dragon/"
dragon_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in dragon_data:
    print("key: ", key, "\n", "value:", dragon_data[key], "\n")
