import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/ability/cute-charm/"
cute_charm_data = requests.get(api_url).json()

""" # display all key-value pairs from the JSON data:
for key in cute_charm_data:
    print("key: ", key, "\n", "value:", cute_charm_data[key], "\n") """

# display the flavor text in english:
print(cute_charm_data["flavor_text_entries"][0]['flavor_text'])