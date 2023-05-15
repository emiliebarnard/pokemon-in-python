import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/characteristic/4"
highly_curious_data = requests.get(api_url).json()

# # display all key-value pairs from the JSON data:
# for key in highly_curious_data:
#     print("key: ", key, "\n", "value:", highly_curious_data[key], "\n")

# for key in highly_curious_data:
#      print(key)

print("English:", highly_curious_data["descriptions"][7]["description"])
print("Spanish:", highly_curious_data["descriptions"][5]["description"])
print("French:", highly_curious_data["descriptions"][3]["description"])