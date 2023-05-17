import requests, json

api_url = "https://pokeapi.co/api/v2/pokemon?limit=1015"
response = requests.get(api_url)
pokemon_json = response.json()

pokedex = [] # indexing starts at 0 for a list, so reference by subtracting 1 from the dex number

dex_num = 1
for pokemon in pokemon_json["results"]:
    pokedex.append(pokemon["name"])
    print("Pokémon #" + str(dex_num) +",", pokemon["name"] + ", added!")
    dex_num += 1