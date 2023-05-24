import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/evolution-chain/64/"
evolution_chain_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in evolution_chain_data:
    print("key: ", key, "\n", "value:", evolution_chain_data[key], "\n")
    for pokemon in evolution_chain_data["chain"]:
        print(pokemon)
        
