import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/gender/female/"
female_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
# for key in female_data:
#     print("key: ", key, "\n", "value:", female_data[key], "\n")

def gendered_evolution(pokemon):
    for poke in female_data["required_for_evolution"]:
        if poke["name"] == pokemon:
            return True
    return False

print(gendered_evolution("wormadam"))
print(gendered_evolution("skitty"))