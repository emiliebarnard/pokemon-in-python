import requests
import json


# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/stat/attack"
attack_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in attack_data:
    print("key: ", key, "\n", "value:", attack_data[key], "\n")

"""# display details of moves which affect the attack stat positively or negatively:
print(attack_data["affecting_moves"])

# display details of nature which affect the attack stat positively or negatively:
print(attack_data["affecting_natrues"])"""

# display moves which decrease the attack stat:
for decrease in attack_data["affecting_moves"]["decrease"]:
    print(decrease["move"]["name"])

# display natures which increase the attack stat:
for increase in attack_data["affecting_natures"]["increase"]:
    print(increase["name"])
