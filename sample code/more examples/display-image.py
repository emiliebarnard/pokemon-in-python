from PIL import Image
from io import StringIO, BytesIO

import requests, json

api_url = "https://pokeapi.co/api/v2/pokemon?limit=1015"
response = requests.get(api_url)
pokemon_json = response.json()

pokedex = [] # indexing starts at 0 for a list, so reference by subtracting 1 from the dex number

dex_num = 1
for pokemon in pokemon_json["results"]:
    pokedex.append(pokemon["name"])
    # print("Pokémon #" + str(dex_num) +",", pokemon["name"] + ", added!")
    dex_num += 1

def get_dex_num(pokemon):
    return pokedex.index(pokemon.lower()) + 1

def show_image(pokemon):
    dex_num = get_dex_num(pokemon)
    # first we need to pad the dex number with 0s based on digits:
    if dex_num < 10:
        url_num = "00" + str(dex_num)
    elif dex_num < 100:
        url_num = "0" + str(dex_num)
    else:
        url_num = str(dex_num)
    # then we can pull the image:
    img_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/" + url_num + ".png"
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))
    img.show()

show_image("skitty")