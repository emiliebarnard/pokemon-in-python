---
# reference to pokeapi docs: https://pokeapi.co/docs/v2
layout: default
title: API Docs
---
# header 1
stuff

# Core Python Interactions

## Pokémon
some intro here

### Abilities
An <i>ability<i> is a game mechanic that grants a passive effect for a Pokémon in battle or while navigating the world. A single Pokémon may have multiple abilities but only one active ability at a given them. More information can be found on <a href="https://bulbapedia.bulbagarden.net/wiki/Ability">Bulbapedia</>.

#### API Path
`https://pokeapi.co/api/v2/ability/{id or name}/`
where `id` is an integer (`1` as the lowest option) and `name` is a lower-case string where spaces are replaced with `-`   

#### Example
The following Python code retreives JSON data for the ability named *Cute Charm* and stores it into a dictionary with the following keys:
- `effect_changes`
- `effect_entries`
- `flavor_text_entries`
- `generation`
- `id`
- `is_main_series`
- `name`
- `names`
- `pokemon`
```python
# code in python syntax
print("hello, world")
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
