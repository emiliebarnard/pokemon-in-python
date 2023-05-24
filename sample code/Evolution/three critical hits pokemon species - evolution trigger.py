import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/evolution-trigger/8/"
evolution_trigger_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in evolution_trigger_data:
    print("key: ", key, "\n", "value:", evolution_trigger_data[key], "\n")
    for pokemon in evolution_trigger_data["pokemon_species"]:
        print(pokemon)
