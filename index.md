---
# reference to pokeapi docs: https://pokeapi.co/docs/v2
layout: default
title: API Docs
---

# About this documentation

This documentation was created as a team project for the Professional Technical Writing course at the University of Washington. The project contributors and authors were Chani Enochs, Christa Mitchell, Emilie Barnard, Jared Prewitt, Shayla Cabalan, and Yvonne Ben.  

<br>

The documentation is hosted on [GitHub](https://github.com/emiliebarnard/pokemon-in-python) and was last updated in May 2023.

---

# Introduction

This documentation provides Python developers with references and tutorials to utilize [PokéAPI](https://pokeapi.co/).  
If you are reading this documentation, we assume you know what Pokémon is, have at least a basic understanding of Python, and know how RESTful API works.

<br>

## What is PokéAPI?

[PokéAPI](https://pokeapi.co/) is a modern [RESTful Application Programming Interface (API)](https://en.wikipedia.org/wiki/Overview_of_RESTful_API_Description_Languages) for developers to quickly consume Pokémon data required for their projects. The data includes Pokémon moves, abilities, types, egg groups, and more.

<br>

## What are Python dictionaries?

<i>Dictionaries</i> are Python’s implementation of a data structure. The API URL line retrieves the relevant data in a JSON file and then in Python we convert the JSON file into a <i>dictionary</i>.

<br>

A <i>dictionary</i> consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

<br>

<i>Key</i> is a unique identifier, and <i>value</i> is where all the data is for the key.

<br>

You can define a <i>dictionary</i> by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key from its associated value. 

<br>

For example:
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

---

# Getting started

**Objective:**
The purpose of this section is to provide details on how to download and install Visual Studio Code and Python programs for coding with the PokéAPI.

**Disclaimer:** The instructions provided within this section will work for both Microsoft Windows, Mac, and Linux users. For full details on additional system requirements, please review the documentation referenced for each software listed below.

## Requirements

### Visual Studio Code requirements
* **Hardware:** 1.6GHZ or faster processor (recommended)
* **System OS:** Microsoft Windows 10 and 11 (32-bit and 64-bit), macOS X (High Sierra 10.13+), Linux (Debian): Ubuntu Desktop 16.04, Debian 9, & Linux (Red Hat): Red Hat Enterprise Linux 7, CentOS 7, Fedora 34
* [System requirements documentation](https://code.visualstudio.com/docs/supporting/requirements)

### Python requirements
* **Hardware:** 8GB RAM or higher (recommended)
* **Software:** Latest Python version 3.11.3 release - Microsoft Windows 10 or 11 and macOS 13 or higher, & Linux (pre-installed) for most systems.
* Python version releases for [Microsoft Windows](https://www.python.org/downloads/windows/), [macOS](https://www.python.org/downloads/macos/), and [Linux](https://www.python.org/downloads/source/)
* Python documentation for [Microsoft Windows](https://docs.python.org/3/using/windows.html), [macOS](https://docs.python.org/3/using/mac.html), and [Linux](https://docs.python.org/3/using/unix.html)

<br>

## Download and install software

1. Download [Visual Studio Code](https://code.visualstudio.com/).
![Visual Studio Code download screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Visual%20Studio%20Code%20Image.png)

![Visual Studio Code choose operating system image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Visual%20Studio%20Code%20Image%202.png)

<br>

2. Download [Python](https://www.python.org/downloads/).  
**Note:** Windows users may need to download Python directly from the [Microsoft Store](https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K?hl=en-us&gl=us). The software auto-detects your OS for download.
![Python download screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image.png)

<br>

3. Download [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for Visual Studio Code. Clicking **Install** will open Visual Studio Code. Select **Install** in Visual Studio Code.  
**Note:** When finished, a page will appear in Visual Studio Code titled, *"Get Started with Python Development."*
![Python install screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%202.png)

![Python install screen in Microsoft Windows store image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%203.png)

![Python Get Started with Python Development screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%204.png)

<br>

4. Install the **Python Request Libraries**. Select **Terminal** from the top menu bar and then **New Terminal**. A small terminal window will appear at the bottom of the screen.

![Python Terminal selection in Visual Studio Code screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20Image%205%20Terminal.png)

![Python Terminal window below screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%20image%206%20Terminal%20below%20screen.png)

<br>

5. In the terminal window, type **pip install requests** and press **enter**. A wall of text will appear; the words **"successfully installed"** will display towards the bottom of the text.  
**Note:** If an error appears, then type **pip3 install requests** instead for the **"succesfully installed"** message to display.

![Python success message in termail screen image](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/Python%207%20Success%20Message.png)

---

# Using the PokéAPI site

**Note:** Anyone can access PokéAPI as it is free to use and open source. Be sure to follow the Fair Use Policy referenced in PokéAPI’s [documentation](https://pokeapi.co/docs/v2) page.

The PokéAPI site allows users to generate Pokémon attributes by typing in the name of a Pokémon. The resource for the Pokemon entered displays attributes from the API pull request. Below are example instructions of how to display Pikachu's traits. To perform the actions below, visit the [PokéAPI](https://pokeapi.co/) site.

1. Place the mouse cursor on the search bar. Click the search bar and for this example replace pokemon/ditto with pokemon/pikachu.  
2. Click the **Submit** button.  
3. Review the resource attributes below of the API’s result displaying Pikachu’s traits. You will use these resource attributes to create your Python code and generate API requests for Pokémon in the **Core Python Interactions** section.

![Pikachu API attribute display screen image example](https://github.com/emiliebarnard/pokemon-in-python/raw/gh-pages/images/PokeAPI%20Image%20Pikachu%20Example.png)

---

# Core Python interactions

## Evolution

### Evolution chains

Many Pokémon have an evolution attribute that transforms into a new type of Pokémon  from their family tree. A Pokémon’s new form consists of new abilities and can often turn the tide in battle.

#### API path

`https://pokeapi.co/api/v2/evolution-chain/{id}/` 

id is the integer (1 as the lowest option) of which we’ll use the id number for an example Pokémon.

##### Examples

The following Python code retrieves JSON data for the Pokémon Magikarp (`id` = `64`) and stores it into a dictionary with the following keys:  
- `id`: the number associated with the Pokémon as an identifier.
- `baby_trigger_item`: the specified item requirement needed to trigger the egg hatching process from a baby Pokémon versus a standard Pokémon that doesn’t have a baby form.
- `chain`: the base link to indicate all evolution details of the identified Pokémon and showcase evolution order.

<br>

**Note:** There are a total of 530 evolution chains to choose from. Use the API path on the [PokéAPI site](https://pokeapi.co/) and remove {id or name} portion to initiate a search to see a list of 530 evolution chains to use by id to enter into Python.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/evolution-chain/64/"
evolution_chain_data = requests.get(api_url).json()
```

<br>

This line of code displays chain data for listed Pokémon:

```python
# display all key-value pairs from the JSON data:
for key in evolution_chain_data:
    print("key: ", key, "\n", "value:", evolution_chain_data[key], "\n")
    for pokemon in evolution_chain_data["chain"]:
        print(pokemon)
```

<br>

### Evolution triggers

Pokémon transformations occur when a condition is met to where the Pokémon changes into a specific type or form.  
For more details on evolution methods that trigger transformations, please refer to [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Methods_of_evolution).

#### API path

`https://pokeapi.co/api/v2/evolution-trigger/{id or name}/`  
id is the integer (1 as the lowest option) of which we’ll use the id number for an example Pokémon.

##### Examples

The following Python code retrieves JSON data for the Pokémon evolution trigger `three critical hits` (`id` = `8`) and stores it into a dictionary with the following keys:  
- `id`: the number associated with the Pokémon as an identifier.
- `name`: the name of the Pokémon identified.
- `names`: the name of the Pokémon  identified used for multiple languages.
- `pokémon_species`: a comprehensive list of Pokémon types associated with evolutions.

<br>

**Note:** There are a total of 13 evolution triggers to choose from. Use the API path on the [PokéAPI site](https://pokeapi.co/) and remove {id or name} portion to initiate a search to see a list of 13 evolution triggers to use by id or name to enter into Python.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/evolution-trigger/8/"
evolution_trigger_data = requests.get(api_url).json()
```

<br>

This line of code displays three critical hits data for listed Pokémon:

```python
# display all key-value pairs from the JSON data:
for key in evolution_trigger_data:
    print("key: ", key, "\n", "value:", evolution_trigger_data[key], "\n")
    for pokemon in evolution_trigger_data["pokemon_species"]:
        print(pokemon)
```

---

## Moves

Pokémon have an assortment of skills and can range from class type to specific conditions to initiate. This section will provide a list of various move types to try in Python. 
Pokémon use *moves* in battle. Some moves are used outside of battle, but only in specific situations related to exploring new areas. 

### API path

`https://pokeapi.co/api/v2/move/{id or name}/`  
where id is an integer representing the move's `id` (`1` as the lowest option) and `name` is a lower-case string (the move's name) where spaces are replaced with `-`

#### Examples

The following Python code retrieves JSON data for the move called 'bubble' (the id for bubble is 145) and stores it into a dictionary with the following keys:

| <span style="display: inline-block; width:100px;">Name</span>  | <span style="display: inline-block; width:410px;">Description</span> | <span style="display: inline-block; width:100px;">Type</span> |
| ----- | -------------------- | ---- |
| `id` | the move's id | integer |
| `name` | the move's name | string |
| `accuracy` | the chance of this move's success as a percentage value | integer |
| `effect_chance` | the chance of this move's effect happening as a percentage value | integer |
| `pp` | this move's power points (power points determine the number of times a move can be used) | integer |
| `priority` | sets the order of moves in battle with values between -8 and 8 ([See Bulbapedia for more information about priority](https://bulbapedia.bulbagarden.net/wiki/Priority)) | integer |
| `power` | the power of this move (moves without a base power have a value of 0) | integer |
| `contest_combos` | the contest combos this move is involved in the information includes which normal or super moves are used before or after this move | ContestComboSets object |
| `contest_type` | the type of appeal this moves gives Pokémon when they use it in a contest  | NamedAPIRecourse(ContestType) object |
| `contest_effect` | the effect this move has when used in a contest | APIRsource(ContestEffect) object |
| `damage_class` | the type of damage this move does | NamedAPIResource(MoveDamageClass) object |
| `effect_entries` | the effect of this move in different languages | list |
| `effect_changes` | previous effects this move had across version groups in different games | list |
| `learned_by_pokemon` | Pokémon capable of learning this move | list |
| `flavor_text_entries` | the flavor text for this move in different languages | list |
| `generation` | the generation this move was introduced | NamedAPIResource(Generation) object |
| `machines` | machines this move is learned from | list |
| `meta` | Metadata about this move | MoveMetaData object |
| `names` | names for this move in different languages | list |
| `past_values` | move resource values changes in different games | list |
| `stat_changes` | the stats changed with the amount they change | list |
| `super_contest_effect` | the effect this move has in a super contest | APIResource(SuperContestEffect) object |
| `target` | the type of target receiving the effects of this move | NamedAPIResource(MoveTarget) object |
| `type` | the elemental type of this move | NamedAPIResource(Type) object |

<br>

```python
import requests, json

# fetch the api data for the move called bubble and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/move/bubble"
bubble_data = requests.get(api_url).json()

for key in bubble_data:
    print("key:", key, "\n", "value:", bubble_data[key], "\n")
```

<br>

This additional code returns a list of Pokémon who can have the Bubble move:

```python
for pokemon in bubble_data["learned_by_pokemon"]:
    print(pokemon["name"])
```

<br>

### Move ailments

*Move ailments* are status conditions caused by moves.   

#### API path

`https://pokeapi.co/api/v2/move-ailment/{id or name}/`  
where `id` is an integer representing the move ailment's id (`1` as the lowest option) and `name` is a lower-case string (the move ailment's name) where spaces are replaced with `-`

##### Examples

The following Python code retrieves JSON data for the move ailment called 'sleep' (the id for sleep is 2) and stores it into a dictionary with the following keys:  
- `id`: the integer id of the move ailment 
- `name`: the move ailment's name (as a string)
- `moves`: a list of moves that cause this ailment 
- `names`: a list of names for this move ailment in different languages 

<br>

```python
import requests, json

# fetch the api data for the move ailment called sleep and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/move-ailment/2"
sleep_data = requests.get(api_url).json()

for key in sleep_data:
    print("key:", key, "\n", "value:", sleep_data[key], "\n")
```

<br>

This additional code returns a list of moves that create the ailment effect:

```python
for language in attack_data["names"]:
    print(language["name"])
```

<br>

### Move battle styles

Pokémon moves have one of three different *move battle styles*. The three styles are:  
- Attack
- Defense
- Support 

#### API path

`https://pokeapi.co/api/v2/move-battle-style/{id or name}/`  
where `id` is an integer representing the move battle style id (`1` as the lowest option and `3` as the highest option) and `name` is a lower-case string (the move battle style name) where spaces are replaced with `-`

##### Examples

The following Python code retrieves JSON data for the move battle style called 'attack' (the id for attack is 1) and stores it into a dictionary with the following keys:  
- `id`: the integer id of the move battle style
- `name`: the move battle style's name (as a string)
- `names`: a list of names for this move battle style in different languages
 
<br>

```python
import requests, json

# fetch the api data for the attack move battle style and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/move-battle-style/1"
attack_data = requests.get(api_url).json()

for key in attack_data:
    print("key:", key, "\n", "value:", attack_data[key], "\n")
```

<br>

This additional code prints the move battle style's name in all languages (the two languages available are French and English):

```python
for language in attack_data["names"]:
    print(language["name"])
```

<br>

### Move categories

General *move categories* grouping similar move effects together. 

#### API path

`https://pokeapi.co/api/v2/move-category/{id or name}/`  
where `id` is an integer representing the move categories id (`0` as the lowest option and `13` as the highest option) and `name` is a lower-case string (the move categories name) where spaces are replaced with `-`

##### Examples

The following Python code retrieves JSON data for the move category called 'swagger' (the id for swagger is 5) and stores it into a dictionary with the following keys:  
- `id`: the integer id of the move category
- `name`: the move category's name (as a string)
- `moves`: a list of moves assigned to this category
- `descriptions`: descriptions of this category in different languages

<br>

```python
import requests, json

# fetch the api data for the swagger move category and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/move-category/5"
swagger_data = requests.get(api_url).json()

for key in swagger_data:
    print("key:", key, "\n", "value:", swagger_data[key], "\n")
```

<br>

This additional code prints the moves grouped together in the swagger move category:

```python
for move in swagger_data["moves"]:
    print(move["name"])
```

<br>

### Move damage classes

Certain types of Pokémon have a variety of moves that are special skills to be used against other opponents where these specialzed Pokémon are associated with a damage class.

#### API path

`https://pokeapi.co/api/v2/move-damage-class/{id or name}/`  
id is the integer (1 as the lowest option) of which we’ll use the id number for an example Pokémon.

##### Examples

The following Python code retrieves JSON data for the Pokémon move damage class `special` (`id` = `3`) and stores it into a dictionary with the following keys:

- `id`: the number associated with the Pokémon as an identifier.
- `name`: the name of the Pokémon identified.
- `descriptions`: the displayed information of a Pokémon  used in multiple languages.
- `moves`: a list of abilities associated with damage class Pokémon.
- `names`: the name of the Pokémon  identified used for multiple languages.

<br>

**Note:** There are a total of 3 move damage classes to choose from. Use the API path on the [PokéAPI site](https://pokeapi.co/) and remove {id or name} portion to initiate a search to see a list of 3 move damage classes to use by id or name to enter into Python.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/move-damage-class/3/"
move_damage_class = requests.get(api_url).json()
```

<br>

This line of code displays specials for Pokémon:

```python
# display all key-value pairs from the JSON data:
for key in move_damage_class:
    print("key: ", key, "\n", "value:", move_damage_class[key], "\n")
    for pokemon in move_damage_class["moves"]:
        print(pokemon)
```

<br>

### Move learn method

Pokémon that learn moves from certain methods whether it is from leveling or otherwise. This section focuses on how to identify these types of Pokémon.

#### API path

`https://pokeapi.co/api/v2/move-learn-method/{id or name}/`

id is the integer (1 as the lowest option) of which we’ll use the id number for an example Pokémon.

##### Examples

The following Python code retrieves JSON data for the Pokémon move learn method `form change` (`id` = `9`) and stores it into a dictionary with the following keys:  
- `id`: the number associated with the Pokémon as an identifier.
- `name`: the name of the Pokémon identified.
- `descriptions`: the displayed information of a Pokémon  used in multiple languages.
- `names`: the name of the Pokémon  identified used for multiple languages.
- `version_groups`: a list showing the different types of Pokémon that learn moves from specific groups.

<br>

**Note**: There are a total of 11 move learn methods to choose from. Use the API path on the [PokéAPI site](https://pokeapi.co/) and remove {id or name} portion to initiate a search to see a list of 3 move damage classes to use by id or name to enter into Python.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/move-learn-method/9/"
move_learn_method = requests.get(api_url).json()
```

<br>

This line of code displays form change names for Pokémon:

```python
# display all key-value pairs from the JSON data:
for key in move_learn_method:
    print("key: ", key, "\n", "value:", move_learn_method[key], "\n")
    for pokemon in move_learn_method["name"]:
        print(pokemon)
```

<br>

### Move targets

An ability to lock on to a Pokémon, environments, or other targetable attributes. This section will focus on how to identify these types of move targets. 

#### API path

`https://pokeapi.co/api/v2/move-target/{id or name}/`  
id is the integer (1 as the lowest option) of which we’ll use the id number for an example Pokémon.

##### Examples

The following Python code retrieves JSON data for the Pokémon move target `fainting Pokémon`  (`id` = `16`) and stores it into a dictionary with the following keys:

- `id`: the number associated with the Pokémon as an identifier.
- `name`: the name of the Pokémon identified.
- `descriptions`: the displayed information of a Pokémon  used in multiple languages.
- `moves`: a list of abilities associated with damage class Pokémon.
- `names`: the name of the Pokémon  identified used for multiple languages.

<br>

**Note:** There are a total of 16 move targets to choose from. Use the API path on the [PokéAPI site](https://pokeapi.co/) and remove {id or name} portion to initiate a search to see a list of 3 move damage classes to use by id or name to enter into Python.

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/move-target/16/"
move_target = requests.get(api_url).json()
```

<br>

This line of code displays fainting Pokémon moves:

```python
# display all key-value pairs from the JSON data:
for key in move_target:
    print("key: ", key, "\n", "value:", move_target[key], "\n")
    for pokemon in move_target["moves"]:
        print(pokemon)
```

---

## Pokémon

### Abilities

An <i>ability</i> is a game mechanic that grants a passive effect for a Pokémon in battle or while navigating the world. A single Pokémon may have multiple abilities but only one active ability at a given time. More information can be found on <a href="https://bulbapedia.bulbagarden.net/wiki/Ability">Bulbapedia</a>.

#### API path

`https://pokeapi.co/api/v2/ability/{id or name}/`  
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

##### Examples

The following Python code retrieves JSON data for the ability named *Cute Charm* and stores it into a dictionary with the following keys:  
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

<br>

This additional line of code displays the *flavor text* of the ability:

```python
print(cute_charm_data["flavor_text_entries"][0]['flavor_text'])
```

<br>

This additional snippet of code displays all Pokémon that can have this ability:

```python
for pokemon in cute_charm_data["pokemon"]:
    print(pokemon["pokemon"]["name"])
```

---

### Characteristics

The *characteristic* of a Pokémon is determined by which stat holds the highest IV (individual values), or strength, and the remainder of that IV when divided by 5 (modulo 5). The highest stat will be one of the following six options:  
- HP (hit points), the total amount of attacks needed to be defeated)
- Attack, which partly determines how much damage the Pokémon deals when applying a physical move
- Defense, which partly determines how much damage the Pokémon takes when hit by a physical move
- Special Attack, which partly determines how much damage the Pokémon deals when applying a special move
- Special Defense, which partly determines how much damage the Pokémon takes when hit by a special move
- Speed, which determines the order of Pokémon in battle

<br>

Further, each stat has 5 options for the *characteristic* phrase applied. The modulo 5 of the IV determines which of the 5 to use.

#### API path

`https://pokeapi.co/api/v2/characteristic/{id}`  
where `id` is an integer (`1` as the lowest option)

##### Examples

The following Python code retrieves JSON data for the characteristic *Highly curious* and stores it into a dictionary with the following keys:  
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

<br>

This additional snippet of code displays the *description* of the characteristic in English, Spanich, and French:

```python
print("English:", highly_curious_data["descriptions"][7]["description"])
print("Spanish:", highly_curious_data["descriptions"][5]["description"])
print("French:", highly_curious_data["descriptions"][3]["description"])
```

<br>

This code displays the 5 possible characteristics given a highest attack stat (see [stats](#stats) for more information):

```python
import requests, json

api_url = "https://pokeapi.co/api/v2/stat/attack"
attack_data = requests.get(api_url).json()

for characteristic in attack_data["characteristics"]:
    characteristic_data = requests.get(characteristic['url']).json()
    print(characteristic_data["descriptions"][7]["description"])
```

---

### Egg Groups

A Pokémon can belong to one or two *Egg Groups*, or groups of Pokémon that are compatible for breeding.

#### API path

`https://pokeapi.co/api/v2/egg-group/{id or name}`  
where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of *Egg Group*

##### Examples

The following Python code retrieves JSON data for the Egg Group *Dragon* and stores it into a dictionary with the following keys:  
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

<br>

This additional code displays all Pokémon that belong to the Egg Group *Dragon*:

```python
for pokemon in dragon_data["pokemon_species"]:
    print(pokemon["name"])
```

---

### Genders

Most Pokémon have a *gender*, either male or female, though some species do not. *Genders* impact breeding compatibility and sometimes the appearance of a Pokémon.

#### API path

`https://pokeapi.co/api/v2/gender/{id or name}`  
where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of the *gender*

##### Examples

The following Python code retrieves JSON data for the Gender *female* and stores it into a dictionary with the following keys:
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

<br>

This additional function checks to see if a Pokémon requires a previous Pokémon to be female for evolution:

```python
def gendered_evolution(pokemon):
    for poke in female_data["required_for_evolution"]:
        if poke["name"] == pokemon:
            return True
    return False
```

---

### Growth Rates

A Pokémon's *Growth Rate* defines how quickly it levels up from experience. The options are as follows:
- erratic
- fast
- medium fast
- medium slow
- slow
- fluctuating

#### API path

`https://pokeapi.co/api/v2/growth-rate/{id or name}`  
where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of the *growth rate*

#### Examples

The following Python code retrieves JSON data for the growth rate *erratic* and stores it into a dictionary with the following keys:
- `id`: an integer (starting with 1) that acts as the identifier for the Gender
- `name`: a string, the name of the growth rate (in English)
- `formula`: a string that represents the mathematical formula used to calculate the rate at which a Pokémon levels up, based on current level and the specific growth rate
- `descriptions`: a list of dictionaries with keys description and language. language is also a dictionary with keys name and url. This is a list of the descriptions of the growth rate in various languages.
- `levels`: a list of dictionaries with keys level and experience. This indicates how much experience is needed to level up based on the current level and growth rate.
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

<br>

The following additional code displays all Pokémon with an *erratic* growth rate.

```python
for pokemon in erratic_data["pokemon_species"]:
    print(pokemon["name"])
```

---

### Natures

A Pokémon's *Nature* defines how they behave, what flavors it likes and dislikes, and typically the value of some of its stats. There are 25 possible natures, ranging from *hardy* to *quirky*.

#### API path

`https://pokeapi.co/api/v2/nature/{id or name}`  
where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of the *nature*

##### Examples

The following Python code retrieves JSON data for the nature *sassy* and stores it into a dictionary with the following keys:
- `decreased_stat`: a dictionary with two keys, name and url, that identifies the stat whose value is decreased by 10% due to this nature
- `hates_flavor`: a dictionary with two keys, name and url, that identifies the the flavor hated by Pokémon with this nature
- `id`: an integer (starting with 1) that acts as the identifier for the Nature
- `increased_stat`: a dictionary with two keys, name and url, that identifies the stat whose value is increased by 10% due to this nature
- `likes_flavor`: a dictionary with two keys, name and url, that identifies the the flavor liked by Pokémon with this nature
- `move_battle_style_preferences`: a list of dictionaries with three keys, low_hp_preference, high_hp_preference, and move_battle_style. move_battle_stype is a dictionary with two keys, name and url. low_hp_preference and high_hp_preference are integers that refer to how likely a Pokémon with this nature is to use a particular move battle style.
- `name`: a string, the name of the Nature (in English)
- `names`: a list of names for this nature in different languages
- `pokeathlon_stat_changes`: a list of dictionaries with two keys, max_change and pokeathalon_stat. pokeathalon_stat is a dictionary with two keys, name and url. This lists all Pokéathalon stats affected by this nature and how much they are impacted. See (Pokéatholon Stats)[#pokéatholon-stats] for more information.

```python
import requests
import json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/nature/sassy"
sassy_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in sassy_data:
    print("key: ", key, "\n", "value:", sassy_data[key], "\n")
```

<br>

This additional line of code describes a few of the impacts of this nature:

```python
print("A", sassy_data["name"], "Pokémon has the following attributes:\n",
      "Increased stat:", sassy_data["increased_stat"]["name"],"\n",
      "Decreased stat:", sassy_data["decreased_stat"]["name"],"\n",
      "Likes this flavor:", sassy_data["likes_flavor"]["name"],"\n",
      "Dislikes this flavor:", sassy_data["hates_flavor"]["name"])
```

---

### Pokéathlon stats

A Pokéatholon is a competition where Pokémon race, jump, and participate in other field events. *Pokéatholon Stats* define how a Pokémon performs in these events. There are five different stats:  
- speed
- power
- skill
- stamina
- jump

#### API path

`https://pokeapi.co/api/v2/pokeathlon-stat/{id or name}`
where `id` is an integer (`1` as the lowest option) and `name` is a string referring to the name of the *Pokéatholon Stats*

##### Examples

The following Python code retreives JSON data for the Pokéatholon Stat *jump* and stores it into a dictionary with the following keys:
- `affecting_natures`: a list of dictionaries with two keys, increase and decrease. Both increase and decrease are dictionaries with two keys, max_change and nature. This list contains data on which Pokémon natures impact the stat, and how it is impacted. See (Natures)[#natures] for more information.
- `id`: an integer (starting with 1) that acts as the identifier for the stat
- `name`: a string, the name of the stat (in English)
- `names`: a list of names for this skill in different languages

```python
import requests
import json


# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokeathlon-stat/jump"
jump_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in jump_data:
    print("key: ", key, "\n", "value:", jump_data[key], "\n")
```

<br>

The following code snippet displays how various Natures impact *jump*:

```python
print("The following Natures increase the", jump_data["name"] ,"stat:")
for nature in jump_data["affecting_natures"]["increase"]:
    print(nature["nature"]["name"], "increases by a max of", nature["max_change"])

print("\nThe following Natures decrease the", jump_data["name"] ,"stat:")
for nature in jump_data["affecting_natures"]["decrease"]:
    print(nature["nature"]["name"], "decreases by a max of", nature["max_change"]*-1)
```

---

### Pokémon location areas

Players encounter Pokémon in multiple locations. *Location Areas* describe where a specified Pokémon can be encountered. Note: Some Pokémon do not have Location Area data. 

#### API path

`https://pokeapi.co/api/v2/pokemon/{id or name}/encounters`  
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`

##### Examples

The following Python code retrieves JSON data for the location areas of the Pokémon Rhydon (this Pokémon's id is 1) and stores it into a dictionary with the following keys:  
- `location_area`: the name of the location and the API url for that location
- `version_details`: a list of encounters, chances, and versions related to the specified Pokémon

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

<br>

This additional code displays only the `name` of the location(s) in which players can encounter the specified Pokémon:
```python
 for location in rhydon_locations:
    print("Rhydon Encounter Location:", location["location_area"]["name"])
```

---

### Pokémon Colors

Pokémon can be sorted by *colors* in a Pokédex. Pokémon are sorted into a color group determined by the color covering most of their body. **Note**: Orange is not a color option. Orange Pokémon are listed as red or brown.  

#### API path

`https://pokeapi.co/api/v2/pokemon-color/`  
returns all Pokémon colors. To return results from a specific color use:

`https://pokeapi.co/api/v2/pokemon-color/{id or name}/`  
where `id` is an integer representing the color's id (`1` as the lowest option) and `name` is a lower-case string (the color's name) where spaces are replaced with `-`

##### Examples
The following Python code retrieves JSON data for the color *blue* (the id for blue is 2) and stores it into a dictionary with the following keys:
- `id`: the integer id of the color
- `name`: the color's name (as a string)
- `names`: a list of the color's name in different languages
- `pokemon_species`: a list of Pokémon in this color group

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-color/2/"
color_2_data = requests.get(api_url).json()

for key in color_2_data:
    print("key:", key, "\n", "value:", color_2_data[key], "\n")
```

<br>

This additional line of code displays the name of the current color in English:
```python
print(color_2_data["name"])
```

<br>

This code prints a list of all the blue Pokémon: 
```python
for pokemon in color_2_data["pokemon_species"]:
    print(pokemon["name"])
```

---

### Pokémon Forms

Pokémon may appear in different *forms*. The forms are visual and cosmetic. Pokémon that vary more than just visually are listed as different Pokémon entities. 

#### API path
`https://pokeapi.co/api/v2/pokemon-form/{id or name}/`  
where `id` is an integer representing the  Pokémon's id (`1` as the lowest option) and `name` is a lower-case string (the Pokémon's name) where spaces are replaced with `-`

##### Examples

The following Python code retrieves JSON data for the West form of  the Pokémon 'Shellos' (the id for the West form of Shellos is 422) and stores it into a dictionary with the following keys:  
- `id`: the Pokémon's id (as an integer) 
- `name`: the Pokémon's name (as a string)
- `order`: an integer that indicates where in the list of all Pokémon forms the Pokémon form you are looking for is located
- `form_order`: the order this Pokémon form appears relative to other Pokémon of the same species
- `is_default`: set to 'true' for only one Pokémon can be set to default within a species 
- `is_battle_only`: a boolean indicating if the form can only happen in battle
- `is_mega`: a boolean indicating if the form is a mega form or not
- `form_name`: the name of the form (as a string)
- `pokemon`: the Pokémon that can take this form including their API path
- `types`: a list of the types this Pokémon form has
- `sprites`: URL links to the sprites used to represent this Pokémon form
- `version_group`: the version name and API path for the version group this Pokémon form was introduced in 
- `names`: a list of the full names of this Pokémon form in different languages (this is empty if no specific names exist)
- `form_names`: a list of the specific form names for this Pokemon form in different languages  (this is empty if no specific names exist)

```python
import requests, json

# fetch the api data for Shellos West and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-form/422"
shellos_w_form_data = requests.get(api_url).json()

for key in shellos_w_form_data:
    print("key:", key, "\n", "value:", shellos_w_form_data[key], "\n")
```  

<br>

Shellos also has an East form. This additional code gets information about Shellos's East form:

```python
# fetch the api data for Shellos East and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-form/10039"
shellos_e_form_data = requests.get(api_url).json()

for key in shellos_e_form_data:
    print("key:", key, "\n", "value:", shellos_e_form_data[key], "\n")
```  

<br>

The two versions of Shellos are right next to each other in the Pokemon Forms Order. To see their order numbers together use this additional line of code:

```python
print("Shellos West's Order Number is", shellos_w_form_data["order"], "and Shellos East's Order Number is", shellos_e_form_data["order"]) 
```  

<br>

**Note**: Searching for just 'Shellos' using the API like this:  
`https://pokeapi.co/api/v2/pokemon-form/shellos`  
returns an error because Shellos has two forms and the API needs you to specifiy which form you want information about. 

---

### Pokémon Habitats

*Pokémon Habitats* are generally different terrain Pokémon can be found in but can also be areas designated for rare or legendary Pokémon. There are nine habitats:  
- Cave
- Forest
- Grassland
- Mountain
- Rare
- Rough-terrain
- Sea
- Urban
- Waters-edge

#### API path

`https://pokeapi.co/api/v2/pokemon-habitat/{id or name}/`  
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

##### Examples

The following Python code retreives JSON data for the shape named *forest* and stores it into a dictionary with the following keys:  
- `id`: the identifier for this resource
- `name`: the name for this resource
- `names`: the name of this resource listed in different languages
- `pokemon_species`: a list of the Pokémon species that can be found in this habitat

<br>

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-habitat/forest/"
forest_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in forest_data:
    print("key: ", key, "\n", "value:", forest_data[key], "\n")
```

This additional line of code displays all Pokémon that can be found in this habitat:

```python
for pokemon_species in forest_data["pokemon_species"]:
    print(pokemon_species["name"])
```

---

### Pokémon shapes
*Pokémon Shape* is used for sorting Pokémon in a Pokédex. There are 14 shapes:  
- Ball
- Squiggle
- Fish
- Arms
- Blob
- Upright
- Legs
- Quadruped
- Wings
- Tentacles
- Heads
- Humanoid
- Bug-wings
- Armor

#### API path

`https://pokeapi.co/api/v2/pokemon-shape/{id or name}/`  
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

##### Examples

The following Python code retreives JSON data for the shape named *ball* and stores it into a dictionary with the following keys:  
- `awesome_names`: the "scientific" name of this Pokémon shape listed in different languages
- `id`: the identifier for this resource
- `name`: the name for this resource
- `names`: the name of this resource listed in different languages
- `pokemon_species`: a list of the Pokémon species that have this shape

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-shape/ball"
ball_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in ball_data:
    print("key: ", key, "\n", "value:", ball_data[key], "\n")
```

<br>

This additional line of code displays all Pokémon that have this shape:
<br>
```python
for pokemon_species in ball_data["pokemon_species"]:
    print(pokemon_species["name"])
```

---
    
### Pokémon species

A <i>Pokémon Species</i> forms the basis for at least one Pokémon. Attributes of a <i>Pokémon species</i> are shared across all varieties of Pokémon within the species. 

#### API path

`https://pokeapi.co/api/v2/pokemon-species/{id or name}`  
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

##### Examples
The following Python code retrieves JSON data for the species named <i>Butterfree</i> and stores it into a dictionary with the following keys:  
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

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/pokemon-species/butterfree"
butterfree_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in butterfree_data:
    print("key: ", key, "\n", "value:", butterfree_data[key], "\n")
```

<br>

This additional line of code displays the flavor text of this species in English:

```python
for entry in butterfree_data["flavor_text_entries"]:
    if entry["language"]["name"] == "en":
        flavor_text = entry["flavor_text"]
        print(flavor_text)
```

<br>

This additional line of code displays this species' genus in Chinese:

```python
for genus in butterfree_data["genera"]:
    if genus["language"]["name"] == "zh-Hant":
        print(genus["genus"])
```

---

### Stats

<i>Stats</i> determine certain aspects of battles. Each Pokémon has a value for each stat which grows as they gain levels and can be altered momentarily by effects in battles.

#### API path

`https://pokeapi.co/api/v2/stat/{id or name}/`  
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

##### Examples

The following Python code retrieves JSON data for the stat named <i>attack</i> and stores it into a dictionary with the following keys:
- `affecting_moves`: a detail of moves which affect this stat positively or negatively
- `affecting_natures`: a detail of natures which affect this stat positively or negatively
- `characteristics`: a list of characteristics that are set on a Pokémon when its highest base stat is this stat
- `game_index`: id the games use for this stat
- `id`: the identifier for this resource
- `is_battle_only`: whether this stat only exists within a battle
- `move_damage_class`: the class of damage this stat is directly related to
- `name`: the name for this resource
- `names`: the name of this resource listed in different languages

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/stat/attack"
attack_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in attack_data:
    print("key: ", key, "\n", "value:", attack_data[key], "\n")
```

<br>

This additional line of code displays moves which decrease the referenced stat:

```python
for decrease in attack_data["affecting_moves"]["decrease"]:
    print(decrease["move"]["name"]))
```

<br>

This additional line of code displays natures which increase the referenced stat:

```python
for increase in attack_data["affecting_natures"]["increase"]:
    print(increase["name"])
```

---

### Types

<i>Types</i> are properties for Pokémon and their moves. Each type has three properties: which types of Pokémon it is super effective against, which types of Pokémon it is not very effective against, and which types of Pokémon it is completely ineffective against.

#### API path

`https://pokeapi.co/api/v2/type/{id or name}/`  
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

##### Examples

The following Python code retrieves JSON data for the type named <i>ghost</i> and stores it into a dictionary with the following keys:  
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

```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/type/ghost"
ghost_data = requests.get(api_url).json()

# display all key-value pairs from the JSON data:
for key in ghost_data:
    print("key: ", key, "\n", "value:", ghost_data[key], "\n")
```

<br>

This additional line of code displays a list of types that are very effective against this type:

```python
for double_damage_from in ghost_data["damage_relations"]["double_damage_from"]:
    print(double_damage_from["name"])
```

<br>

This additional line of code displays a list of types this type is very effect against:

```python
for double_damage_to in ghost_data["damage_relations"]["double_damage_to"]:
    print(double_damage_to["name"])
```

---

# More Python sample code

## Create Pokédex

The following Python code creates a Pokédex of all 1015 Pokémon by storing them into a list:

```python
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
```

---

## Search Pokémon by filters

There are various ways to search for Pokémon by filters. Please refer to the example code in the following sections:  
- [Abilities](#abilities)
- [Egg Group](#egg-group)
- [Growth Rates](#growth-rates)

---

## Display Pokémon image

To display images in Python, install one more library named *Pillow*. To do this, type `pip install pillow` in your Terminal (just like `pip install requests` as explained in [Getting Started](getting-started)).

<br>

The following Python code creates a Pokédex (see (Create Pokédex)[create-pokédex]), then defines two functions to display an image of any given Pokémon. The sample call included displays an image of Skitty.

```python
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

show_image("Skitty")
```

# Resources

## Common errors

### API error

Below is a common error when working with the API:

```  File "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/requests/models.py", line 975, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)```

In this scenario, check the API path call in the form of ```api_url = "https://pokeapi.co/api/v2/{category}/{name or id}/"```. If the syntax is correct, `name` or `id` likely does not exist for the specific `category`. Change `id` to `1` for further testing.

### Python errors

Refer to the [Python documentation](https://docs.python.org/3/) for troubleshooting other Python-specific error messages.

## Links

Refer to the below links for more resources:
- [Bulbapedia, the community-driven Pokémon encyclopedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page)
- [PokéAPI on GitHub](https://github.com/PokeAPI/pokeapi)
- [Python Docs: Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

