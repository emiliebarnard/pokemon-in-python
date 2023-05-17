import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/growth-rate/5"
erratic_data = requests.get(api_url).json()

# # display all key-value pairs from the JSON data:
# for key in erratic_data:
#     print("key: ", key, "\n", "value:", erratic_data[key], "\n")

for pokemon in erratic_data["pokemon_species"]:
    print(pokemon["name"])