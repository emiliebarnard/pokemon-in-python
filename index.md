---
# reference to pokeapi docs: https://pokeapi.co/docs/v2
layout: default
title: API Docs
---
# Getting Started
**Objective**
The purpose of this section is to provide details on recommended software to download and how to set up before beginning to code with Python.

**Disclaimer:** The instructions provided within this section will work for both Microsoft Windows and Mac users. For full details on additional system requirements, please review the documentation referenced for each software listed below.

**Visual Studio Code Requirements**
* **Hardware:** 1.6GHZ or faster processor (recommended)
* **System OS:** Microsoft Windows 10 and 11 (32-bit and 64-bit), macOS X (High Sierra 10.13+)
* System requirements documentation: https://code.visualstudio.com/docs/supporting/requirements

**Python**
* **Hardware:** 8GB RAM or higher (recommended)
* **Software:** Latest Python version 3.11.3 release - Microsoft Windows 10 or 11 and macOS 13 or higher
* Python version releases for Microsoft Windows: https://www.python.org/downloads/windows/
* Python version releases for macOS: https://www.python.org/downloads/macos/
* Python documentation (first time use) for Microsoft Windows: https://docs.python.org/3/using/windows.html
* Python documentation (first time use) for macOS: https://docs.python.org/3/using/mac.html

## Visual Studio Code (Setup)
1. Download [Visual Studio Code](https://code.visualstudio.com/)


# Core Python Interactions

## Pokémon
some intro here

### Abilities
An <i>ability<i> is a game mechanic that grants a passive effect for a Pokémon in battle or while navigating the world. A single Pokémon may have multiple abilities but only one active ability at a given time. More information can be found on <a href="https://bulbapedia.bulbagarden.net/wiki/Ability">Bulbapedia</a>.

#### API Path
`https://pokeapi.co/api/v2/ability/{id or name}/`

where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

#### Examples
The following Python code retreives JSON data for the ability named *Cute Charm* and stores it into a dictionary with the following keys:
- `effect_changes`: a list of historical effects this ability in previous versions and in different languages
- `effect_entries`: a list of the current effect this this ability in different languages
- `flavor_text_entries`: a list of the flavor text, or short text often displayed in images, of this ability in different languages
- `generation`: the Pokémon generation in which this ability first appeared
- `id`: an integer (`1` as the lowest option) unique to this ability
- `is_main_series`: a boolean to flag whether or not this ability first appeared in the main series of the games
- `name`: a string representing this ability's name
- `names`: a list of names for this ability in different languages
- `pokemon`: a list of Pokémon that may have this ability

<br>

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/ability/cute-charm/"
cute_charm_data = requests.get(api_url).json()

for key in cute_charm_data:
    print("key: ", key, "\n", "value:", cute_charm_data[key], "\n")
```

This additional line of code displays the *flavor text* of the ability:
```python
print(cute_charm_data["flavor_text_entries"][0]['flavor_text'])
```

This additional line of code displays all Pokémon that can have this ability:
```python
for pokemon in cute_charm_data["pokemon"]:
    print(pokemon["pokemon"]["name"])
```

### Characteristics
### Egg Groups
### Genders
### Growth Rates
### Natures
### Pokéatholon Stats
### Pokémon Location Areas
### Pokémon Colors
### Pokémon Forms
### Pokémon Habitats
### Pokémon Shapes
### Pokémon Species
### Stats
### Types
