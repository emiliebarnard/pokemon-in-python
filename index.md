---
# reference to pokeapi docs: https://pokeapi.co/docs/v2
layout: default
title: API Docs
---
## About this documentation
This documentation was created as a team project for the Professional Technical Writing course at the University of Washington. The project contributors and authors were Chani Enochs, Christa Mitchell, Emilie Barnard, Jared Prewitt, Shayla Cabalan, and Yvonne Ben.
<br>
The documentation is hosted on [GitHub](https://github.com/emiliebarnard/pokemon-in-python) and was last updated in May 2023. 
<br>

# Introduction
This documentation provides Python developers with references and tutorials to utilize [PokéAPI](https://pokeapi.co/).
<br>
If you are reading this documentation, we assume you know what Pokémon is, have at least a basic understanding of Python, and know how RESTful API works.


## What is PokéAPI?
[PokéAPI](https://pokeapi.co/) is a modern [RESTful Application Programming Interface (API)](https://en.wikipedia.org/wiki/Overview_of_RESTful_API_Description_Languages) for developers to quickly consume Pokémon data required for their projects. The data includes Pokémon moves, abilities, types, egg groups, and more.

## What are Python dictionaries?
<i>Dictionaries</i> are Python’s implementation of a data structure. The API URL line retrieves the relevant data in a JSON file and then in Python we convert the JSON file into a <i>dictionary</i>.
<br>
A <i>dictionary</i> consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.
<br>
<i>Key</i> is a unique identifier, and <i>value</i> is where all the data is for the key. 
<br>
You can define a <i>dictionary</i> by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value. For example:
```python
d = {
    <key>: <value>,
    <key>: <value>,
      .
      .
      .
    <key>: <value>
}
```
## Overview of the Documentation
The documentation is organized as follows:
* Introduction
* Getting Started
* Core Python Interactions
    * Encounters
      * Encounter Methods
      * Encounter Conditions
      * Encounter Condition Values
    * Evolution
      * Evolution Chains
      * Evolution Triggers
    * Moves
      * Move Ailments
      * Move Battle Styles
      * Move Categories
      * Move Damage Classes
      * Move Learn Methods
      * Move Targets
    * Pokémon
      * Abilities
      * Characteristics
      * Egg Groups
      * Genders
      * Growth Rates
      * Natures
      * Pokéatholon Stats
      * Pokémon Location Areas
      * Pokémon Colors
      * Pokémon Forms
      * Pokémon Habitats
      * Pokémon Shapes
      * Pokémon Species
      * Stats
      * Types
* More Python Sample Code
    * Create Pokédex
    * Search Pokémon by Filters
    * Display Pokémon Image
* Resources




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

## Visual Studio Code & Python Software (Setup)
1. Download [Visual Studio Code](https://code.visualstudio.com/).
![Visual Studio Code download screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Visual%20Studio%20Code%20Image.png)

![Visual Studio Code choose operating system image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Visual%20Studio%20Code%20Image%202.png)

2. Download [Python](https://www.python.org/downloads/). **Note:** Some Windows users may need to download Python directly from the Microsoft Store instead. This can be done [here](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=en-us&gl=us).
![Python download screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image.png)

3. Download [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code.
![Python install screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%202.png)

**Note:** The [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) link opens Visual Studio code application. From there, select **Install**. When finished, a page will appear in the app titled, *"Get Started with Python Development."*

![Python install screen in Microsoft Windows store image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%203.png)

![Python Get Started with Python Development screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%204.png)

4. Install the **Python Request Libraries**. Select **Terminal** from the top menu bar and then **New Terminal**. A small terminal window appears at the bottom of the screen.

![Python Terminal selection in Visual Studio Code screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%205%20Terminal.png)

![Python Terminal window below screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20image%206%20Terminal%20below%20screen.png)

5. In the terminal window, type **pip install requests** and press **enter**. A wall of text will appear; the words **"successfully installed"** will display.
**Note:** If an error appears, then type **pip3 install requests** instead for the **"succesfully installed"** message to display.

![Python success message in termail screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%207%20Success%20Message.png)

### PokéAPI (How to use)
**Disclaimer:** Anyone can access PokéAPI as it is free to use and open source. Be sure to follow the Fair Use Policy referenced in PokéAPI’s [documentation](https://pokeapi.co/docs/v2) page.

The PokéAPI site allows users to generate Pokémon attributes by typing in the name of a Pokémon. The resource for the Pokemon entered displays attributes from the API pull request. Below are example instructions of how to display Pikachu's traits.

1. Place mouse cursor on search bar and replace **Ditto** with **Pikachu**.
2. Click the **Submit** button.
3. Review the resource attributes below of the API’s result displaying Pikachu’s traits.

![Pikachu API attribute display screen image example](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/PokeAPI%20Image%20Pikachu%20Example.png)

**Note:** Next steps involve coding with Python to generate an API request for Pokémon.

# Core Python Interactions

## Pokémon
some intro here

### Abilities
An <i>ability</i> is a game mechanic that grants a passive effect for a Pokémon in battle or while navigating the world. A single Pokémon may have multiple abilities but only one active ability at a given time. More information can be found on <a href="https://bulbapedia.bulbagarden.net/wiki/Ability">Bulbapedia</a>.

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

This additional snippet of code displays all Pokémon that can have this ability:
```python
for pokemon in cute_charm_data["pokemon"]:
    print(pokemon["pokemon"]["name"])
```

### Characteristics

The *charactertic* of a Pokémon is determined by which stat holds the highest IV (individual values), or strength, and the remainder of that IV when divided by 5 (modulo 5). The highest stat will be one of the following six options:

- HP (hit points), the total amount of attacks needed to be defeated)
- Attack, which partly determines how much damage the Pokémon deals when applying a physical move
- Defense, which partly determines how much damage the Pokémon takes when hit by a physical move
- Special Attack, which partly determines how much damage the Pokémon deals when applying a special move
- Special Defense, which partly determines how much damage the Pokémon takes when hit by a special move
- Speed, which determines the order of Pokémon in battle

Further, each stat has 5 options for the *characteristic* phrase applied. The modulo 5 of the IV determines which of the 5 to use.

#### API Path
`https://pokeapi.co/api/v2/characteristic/{id}`

where `id` is an integer (`1` as the lowest option)

#### Examples
The following Python code retreives JSON data for the characteristic *Highly curious* and stores it into a dictionary with the following keys:
- `descriptions`: a list of dictionaries with two keys, descriptions and language. The description key stores a string value which is the description in the associated language. The language key holds another dictionary with two keys, name and url, where both values are strings associated with the language. 
- `gene_modulo`: an inteeger between 0 and 4 (inclusive) which is the remainder of the highest IV divided by 5 (modulo 5)
- `highest_stat`: a dictionary with two keys, name and url, both of which are string values that refer to the IV associated with this characteristic
- `id`: an integer (`1` as the lowest option) unique to this characteristic
- `possible_values`: a list of integers that represent the possible values of the highest IV of a Pokémon with this characteristic

<br>

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/characteristic/4"
highly_curious_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in highly_curious_data:
    print("key: ", key, "\n", "value:", highly_curious_data[key], "\n")
```

This additional snippet of code displays the *description* of the characteristic in English, Spanich, and French:
```python
print("English:", highly_curious_data["descriptions"][7]["description"])
print("Spanish:", highly_curious_data["descriptions"][5]["description"])
print("French:", highly_curious_data["descriptions"][3]["description"])
```

This code displays the 5 possible characteristics given a highest attack stat (see [stats](#stats) for more information):

```python
import requests, json

api_url = "https://pokeapi.co/api/v2/stat/attack"
attack_data = requests.get(api_url).json()

for characteristic in attack_data["characteristics"]:
    characteristic_data = requests.get(characteristic['url']).json()
    print(characteristic_data["descriptions"][7]["description"])
```

### Egg Groups
A Pokémon can belong to one or two *Egg Groups*, or groups of Pokémon that are compatible for breeding.

#### API Path
`https://pokeapi.co/api/v2/egg-group/{id or name}`

where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of *Egg Group*

#### Examples
The following Python code retreives JSON data for the Egg Group *Dragon* and stores it into a dictionary with the following keys:
- `id`: an integer (starting with 1) that acts as the identifier for the Egg Group
- `name`: the name of the Egg Group (in English)
- `names`: a list of dictionaries with two keys, name and language. The value of name is a string, and the value of language is a dictionary with two keys, name and url. These keys refer to the name and url of the language used to express the Egg Group name.
- `pokemon_species`: a list of dictionaries with two keys, name and url. These reference all the Pokémon in the Egg Group.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/egg-group/dragon/"
dragon_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in dragon_data:
    print("key: ", key, "\n", "value:", dragon_data[key], "\n")
```

This additional code displays all Pokémon that belong to the Egg Group *Dragon*:
```python
for pokemon in dragon_data["pokemon_species"]:
    print(pokemon["name"])
```

### Genders
Most Pokémon have a *gender*, either male or female, though some species do not. *Genders* impact breeding compatability and sometimes the appearance of a Pokémon.

#### API Path
`https://pokeapi.co/api/v2/gender/{id or name}`
where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of the *gender*

#### Examples
The following Python code retreives JSON data for the Gender *female* and stores it into a dictionary with the following keys:
- `id`: an integer (starting with 1) that acts as the identifier for the Gender
- `name`: the name of the Gender (in English)
- `pokemon_species_details`: a list of dictionaries with two keys, name and language. The value of name is a string, and the value of language is a dictionary with two keys, rate and pokemon_species. rate refers to the likelihood of a Pokémon species being this gender, out of ?. pokemon_species is a dictionary with keys name and url, both referring to the Pokémon that can be this gender.
- `required_for_evolution`: a list of dictionaries with two keys, name and url. These reference all the Pokémon that require a previous Pokémon to be this specific gender in order to evolve into them.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/gender/female/"
female_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in female_data:
    print("key: ", key, "\n", "value:", female_data[key], "\n")
```

This additional function checks to see if a Pokémon requires a previous Pokémon to be female for evolution:
```python
def gendered_evolution(pokemon):
    for poke in female_data["required_for_evolution"]:
        if poke["name"] == pokemon:
            return True
    return False
```

### Growth Rates
A Pokémon's *Growth Rate* defines how quickly it levels up from experience. The options are as follows:
- erratic
- fast
- medium fast
- medium slow
- slow
- fluctuating

#### API Path
`https://pokeapi.co/api/v2/growth-rate/{id or name}`
where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of the *growth rate*

#### Examples
The following Python code retreives JSON data for the growth rate *erratic* and stores it into a dictionary with the following keys:
- `id`: an integer (starting with 1) that acts as the identifier for the Gender
- `name`: a string, the name of the growth rate (in English)
- `formula`: a string that represents the mathematical formula used to cacluate the rate at which a Pokémon levels up, based on current level and the specific growth rate
- `descriptions`: a list of dictionaries with keys description and language. language is also a dictionary with keys name and url. This is a list of the descriptions of the growth rate in various languages.
- `levels`: a list of dictionaires with keys level and experience. This indicates how much experience is needed to level up based on the current level and growth rate.
- `pokemon_species`: a list of dictionaries with keys name and url. This is a list of all Pokémon that level up at this growth rate.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/growth-rate/5"
erratic_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in erratic_data:
    print("key: ", key, "\n", "value:", erratic_data[key], "\n")
```

The following additional code displays all Pokémon with an *erratic* growth rate.

```python
for pokemon in erratic_data["pokemon_species"]:
    print(pokemon["name"])
```

### Natures
A Pokémon's *Nature* defines how they behave, what flavors it likes and dislikes, and typically the value of some of its stats. There are 25 possible natures, ranging from *hardy* to *quirky*.

#### Examples
The following Python code retreives JSON data for the nature *quirky* and stores it into a dictionary with the following keys:
- `decreased_stat`: a dictionary with two keys, name and url, that identifies the stat whose value is decreased by 10% due to this nature
- `hates_flavor`: a dictionary with two keys, name and url, that identifies the the flavor hated by Pokémon with this nature
- `id`: an integer (starting with 1) that acts as the identifier for the Nature
- `increased_stat`: a dictionary with two keys, name and url, that identifies the stat whose value is increased by 10% due to this nature
- `likes_flavor`: a dictionary with two keys, name and url, that identifies the the flavor liked by Pokémon with this nature
- `move_battle_style_preferences`: a list of dictionaries with three keys, low_hp_preference, high_hp_preference, and move_battle_style. move_battle_stype is a dictionary with two keys, name and url. low_hp_preference and high_hp_preference are integers that refer to how likely a Pokémon with this nature is to use a particular move battle style.
- `name`: a string, the name of the Nature (in English)
- `names`: a list of names for this nature in different languages
- `pokeathlon_stat_changes`: a list of dictionaries with two keys, max_change and pokeathalon_stat. pokeathalon_stat is a dictionary with two keys, name and url. This lists all Pokéathalon stats affected by this nature and how much they are impacted.

```python
import requests
import json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/nature/quirky"
quirky_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in quirky_data:
    print("key: ", key, "\n", "value:", quirky_data[key], "\n")
```

This additional line of code describes a few of the impacts of this nature:
```python
print()
```



### Pokéatholon Stats
### Pokémon Location Areas
Players encounter Pokémon in multiple locations. *Location Areas* describe where a specified Pokémon can be encountered. Note: Some Pokémon do not have Location Area data. 

#### API Path
`https://pokeapi.co/api/v2/pokemon/{id or name}/encounters`

where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`

#### Examples

The following Python code retrieves JSON data for the location areas of the Pokémon Rhydon (this Pokémon's id is 1) and stores it into a dictionary with the following keys:
- `location_area`: the name of the location and the API url for that location
- `version_details`: a list of encounters, chances, and versions related to the specified Pokémon
<br>


```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon/1/encounters"
rhydon_locations = requests.get(api_url).json()

for location in rhydon_locations:
    for key, value in location.items():
        print(key, ":", value)
    print()
```

This additional code displays only the `name` of the location(s) in which players can encounter the specified Pokémon:
```python
for location in rhydon_locations:
    location_area = location["location_area"]
    if location_area:
        name = location_area["name"]
        if name:
            print("Rhydon Encounter Location:", name)
```

### Pokémon Colors
### Pokémon Forms
### Pokémon Habitats
### Pokémon Shapes
    
### Pokémon Species
A <i>Pokémon Species</i> forms the basis for at least one Pokémon. Attributes of a <i>Pokémon species</i> are shared across all varieties of Pokémon within the species. 

#### API Path
`https://pokeapi.co/api/v2/pokemon-species/{id or name}`

where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

#### Examples
The following Python code retreives JSON data for the species named <i>Butterfree</i> and stores it into a dictionary with the following keys:

- `base_happiness`: the happiness when caught by a normal Pokéball; up to 255. The higher the number, the happier the Pokémon
- `capture_rate`: the base capture rate; up to 255. The higher the number, the easier the catch
- `color`:the color of this Pokémon for Pokédex search
- `egg_groups`: a list of egg groups this Pokémon species is a member of
- `evolution_chain`: the evolution chain this Pokémon species is a member of
- `evolves_from_species`: the Pokémon species that evolves into this Pokemon_species
- `flavor_text_entries`: a list of flavor text entries for this Pokémon species
- `form_descriptions`: descriptions of different forms Pokémon take on within the Pokémon species
- `forms_switchable`: whether or not this Pokémon has multiple forms and can switch between them
- `gender_rate`: the chance of this Pokémon being female, in eighths; or -1 for genderless
- `genera`: the genus of this Pokémon species listed in multiple languages
- `generation`: the generation this Pokémon species was introduced in
- `growth_rate`: the rate at which this Pokémon species gains levels
- `habitat`: the habitat this Pokémon species can be encountered in
- `has_gender_differences`: whether or not this Pokémon has visual gender differences
- `hatch_counter`: initial hatch counter: one must walk 255 × (hatch_counter + 1) steps before this Pokémon's egg hatches, unless utilizing bonuses like Flame Body's
- `id`: the identifier for this resource
- `is_baby`: whether or not this is a baby Pokémon
- `is_legendary`: whether or not this is a legendary Pokémon
- `is_mythical`: whether or not this is a mythical Pokémon
- `name`: the name for this resource
- `names`: the name of this resource listed in different languages
- `order`: the order in which species should be sorted. Based on National Dex order, except families are grouped together and sorted by stage
- `pal_park_encounters`: a list of encounters that can be had with this Pokémon species in pal park
- `pokedex_numbers`: a list of Pokedexes and the indexes reserved within them for this Pokémon species
- `shape`: the shape of this Pokémon for Pokédex search
- `varieties`: a list of the Pokémon that exist within this Pokémon species
<br>

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-species/butterfree"
butterfree_data = requests.get(api_url).json()

for key in butterfree_data:
    print("key: ", key, "\n", "value:", butterfree_data[key], "\n")
```

This additional line of code displays the flavor text of this species in English:

```python
for entry in butterfree_data["flavor_text_entries"]:
    if entry["language"]["name"] == "en":
        flavor_text = entry["flavor_text"]
        print(flavor_text)
```

This additional line of code displays this species' genus in Chinese:

```python
for genus in butterfree_data["genera"]:
    if genus["language"]["name"] == "zh-Hant":
        print(genus["genus"])
```

### Stats
<i>Stats</i> determine certain aspects of battles. Each Pokémon has a value for each stat which grows as they gain levels and can be altered momentarily by effects in battles.

#### API Path
`https://pokeapi.co/api/v2/stat/{id or name}/`

where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

#### Examples
The following Python code retreives JSON data for the stat named <i>attack</i> and stores it into a dictionary with the following keys:
- `affecting_moves`: a detail of moves which affect this stat positively or negatively
- `affecting_natures`: a detail of natures which affect this stat positively or negatively
- `characteristics`: a list of characteristics that are set on a Pokémon when its highest base stat is this stat
- `game_index`: id the games use for this stat
- `id`: the identifier for this resource
- `is_battle_only`: whether this stat only exists within a battle
- `move_damage_class`: the class of damage this stat is directly related to
- `name`: the name for this resource
- `names`: the name of this resource listed in different languages
<br>

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/stat/attack"
attack_data = requests.get(api_url).json()

for key in attack_data:
    print("key: ", key, "\n", "value:", attack_data[key], "\n")
```

This additional line of code displays moves which decrease the referenced stat:
```python
for decrease in attack_data["affecting_moves"]["decrease"]:
    print(decrease["move"]["name"]))
```

This additional line of code displays natures which increase the referenced stat:
```python
for increase in attack_data["affecting_natures"]["increase"]:
    print(increase["name"])
```

### Types
<i>Types</i> are properties for Pokémon and their moves. Each type has three properties: which types of Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against.

#### API Path
`https://pokeapi.co/api/v2/type/{id or name}/`

where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

#### Examples
The following Python code retreives JSON data for the type named <i>ghost</i> and stores it into a dictionary with the following keys:
- `damage_relations`: a detail of how effective this type is toward others and vice versa
- `game_indices`: a list of game indices relevent to this item by generation
- `generation`: the generation this type was introduced in.
- `id`: the identifier for this resource
- `move_damage_class`: the class of damage inflicted by this type
- `moves`: a list of moves that have this type
- `name`: the name for this resource
- `names`: the name of this resource listed in different languages
- `past_damage_relations`: a list of details of how effective this type was toward others and vice versa in previous generations
- `pokemon`: a list of details of Pokémon that have this type
<br>

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/type/ghost"
ghost_data = requests.get(api_url).json()

for key in ghost_data:
    print("key: ", key, "\n", "value:", ghost_data[key], "\n")
```

This additional line of code displays a list of types that are very effective against this type:
```python
for double_damage_from in ghost_data["damage_relations"]["double_damage_from"]:
    print(double_damage_from["name"])
```

This additional line of code displays a list of types this type is very effect against:
```python
for double_damage_to in ghost_data["damage_relations"]["double_damage_to"]:
    print(double_damage_to["name"])
```
