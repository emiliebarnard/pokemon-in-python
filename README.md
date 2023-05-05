# pokemon-in-python

Don't forget to swap to gh-pages branch if editing the website!

Website link: https://emiliebarnard.github.io/pokemon-in-python/

## Using GitHub

### Branches

There are two *branches* for this project: `main` and `gh-pages`. `main` is where I've been throwing my testing Python code. This section won't actually be part of the final deliverable, but we can use it to save Python code that you work with if you'd like. `gh-pages` is the branch that actually is the website, our deliverable.

To see what branch you're currently looking at, look for the drop down arrow on the top left. If you want to work on the website, make sure you swap over to gh-pages.

<img width="325" alt="Screenshot 2023-05-04 at 6 43 56 PM" src="https://user-images.githubusercontent.com/1448658/236362338-8c1d3f7d-8e12-49d2-8abc-06314d3363a3.png">

### Contributing

There's a few different ways you can contribute to files on GitHub. I'll suggest the easiest possible for those who haven't used it before, but feel free to do whatever works for you or research alternatives. You can click on a file listed out in the folder structure to view it. **The bulk of the content needs to be added to index.md under the gh-pages branch.** So, for example, once you make sure you're on the gh-pages branch, click on the index.md file in the folder list. Look for the pencil button on the top left:

<img width="358" alt="Screenshot 2023-05-04 at 6 45 49 PM" src="https://user-images.githubusercontent.com/1448658/236362458-5a555869-4351-40bd-a203-a210d5b774c8.png">

Click that to edit the file. To "save," scroll down and enter in some sort of "title" to explain the change you made. You can optionally add a longer description. Then, click *commit changes.* Don't worry about the second option to create a new branch - no need for that here.

### Warnings

GitHub is great, but when two people are working on the same file at the same time, weird things can happen. So, I **strongly recommend you send a quick message to the group on Discord if you are starting to work on a file, then send another one when you are done.** Ideally, we should try to *not* overlap the time we are working on the same file.

### Checking the Website

It will take up to a few minutes for GitHub to properly set up the website anytime you make an edit to a file in gh-pages. You can track the "build" progress by clicking on the *Actions* tab at the top. There will be a long list of workflows there, as it shows everything that was done when anyone saved a file. The most recent one is at the top, so watch that one. It should hopefully turn into a green checkmark. When it does, you can check the results on the website: https://emiliebarnard.github.io/pokemon-in-python/. You may need to check using a private/incognito window if your computer cached the website before to see the changes.

## The Website

### Editing the Website

As mentioned above, **the bulk of the content needs to be added to index.md under the gh-pages branch.** Use the instructions above to open, edit, "save" your edits, and "commit" them to the website. Then wait a minute or two and check the website. Don't worry - if something doesn't work it's really easy to "revert" back versions. You can see all previous verions of all files by looking at the version history.

This index.md file expects *markdown* so add content in markdown form. You can use HTML too if needed (I sometimes add a br to force an extra line for example). A refresher for markdown can be found here: https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

### Current Issues

I scrapped the base website together relatively quickly, so there are a few things I still need to fix. In particular, the navigation on the side doesn't do anything right now. I took some time to get the "bullet points" and the "drop down" structure working, but I still need to go back and add the actual links so you can click around the document. I'll do this once all the headers have been added to the index.md file. I created a GitHub issue about this here for tracking: https://github.com/emiliebarnard/pokemon-in-python/issues/2

I'm not married to the current theme, but I picked this one initially because it had a relatively "easy" way to set up the navigation sidebar that anchors on the left, which I thought would be good for users. I also like it because it automatically swaps between light and dark mode depending on what your device prefers. That said, there's an issue with dark mode: the colors in the syntax highlighting for Python. You can see what I mean here: https://github.com/emiliebarnard/pokemon-in-python/issues/1

## Writing Tips

I am using the info here as a starting point: https://pokeapi.co/docs/v2. I attempted to rephrase it in a way that was a bit more accessible so it would appeal to even non-gamers. You can see what I did with the <i>Pokemon - Ability</i> piece for example (which is open to edits, please!! I did it kinda quikcly.)

## Python Code Tips

### Dictionaries

So...**dictionaries are pretty important here. I actually think we may want to add a little info about them in the "info" section of our project.** Basically, the API URL line gives you some JSON code, and then in Python we convert it to a data structure called a dictionary. The main think to know here is that a dictionary is a set of multiple key-value pairs. The idea is that the "key" is usually something short, a unique identifier, and the "value" is where all the data is for that key. I'm guessing for most things we look at the keys will all be strings, maybe integers?. The value is trickier though - sometimes it's a list, but sometimes it's yet another dictionary! LOL

Mentally you can think of a dictionary as, well, a dictionary. Like, the book kind. For the book, the "key" is the word itself. You then go do your dictionary, locate that word, then you can read the full defintion, which is the "value." In short, you use the key to look up the value in the dictionary. You know what the key is, but the value is probably some complicated longer thing.

### Starting & Layout Goals
I am using the info in https://pokeapi.co/docs/v2 to know what API path to use. I wasn't exactly sure what format we wanted to do, so I went with this sort of layout:

1. plain description in english
2. General API path link with explanations for any variables at the end of it (try to call out the type (integer, string, list, etc) if possible
3. bullet-point list of all of the keys in the dictionary converted from the JSON info with explanations. again, if possibl include the type here.
4. Sample code that shows the imports and API path call (with a specific example tacked on to the end of the API call - your choice what to use here! For example, for Abilities I did *cute-charm*), plus a simple loop structure that displays all of the key-value pairs in the dictionary.
5. One or two more short line snippets that you can add to the sample code to do a specific action that you think might be common with this particular feature. 

### How I Played with the Code

Looking at #4 in the Starting & Layout Goals above, most of that piece will look something like this:
```python
import requests, json

# fetch the api data and convert to dictionary:
api_url = "https://pokeapi.co/api/v2/ability/cute-charm/"
some_name_here_data = requests.get(api_url).json()

for key in some_name_here_data:
    print("key: ", key, "\n", "value:", some_name_here_data[key], "\n") """
```

replace `some_name_here_data` with something that makes more sense for the example though. I did `cute_charm_data` in the Abilities example.

Looking at #3 above, I think the easiest way to get an abc ordered list of all of the keys in the dictionary for whatever your data is that you pulled would look something like this:
```python
keys = []
for key in some_name_here_data:
    keys.append(key)
keys.sort()
print(keys)
```
(be sure you add these lines to what is above already. You need those imports and the two lines that fetch the api part first.)

The tickier part is #4 above, as you kinda just have to try things until it works. There's a bit of a method for doing that though:
1. pick a key you think would be neat to pull the data/value out of. Like, in Abilities I made examples with the keys `"flavor_text_entries"' and '"pokemon"'
2. To see the value stored in that key, do `some_name_here_data[key]` where `key` is the key. You could print this, for example, to see what it looks like:
```print(some_name_here_data[key])```
You can also get the type of what the value is by doing:
```print(value(some_name_here_data[key]))```
Knowing what it looks like and what type the value is can give you some hints about how to access the smaller piece you actually want to display. Feel free to ping me about this part though cuz I know it gets a little weird. Just remember, use a lot of print statements to see what different pieces are!

You can also sort of see my progression with figuring out the abilities by seeing my code history here: https://github.com/emiliebarnard/pokemon-in-python/commits/main/sample%20code/pokemon/pokemon-abilities.py

### Adding Code to the Website

Neat trick - there is GitHub markdown that says "hey, this is code. But also, it's Python code, so do syntax highlighting for me." Info on that is here: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks (There's an example here where they use ruby. Just change that word to Python for us.) I sometimes have to add extra newlines around these code blocks so the formatting doesn't look weird when it's on the website.

### Adding Code File to the Repository

To be consistent, once you get some working code for your section we should probably add the actual Python file to the repository so it's easy for the rest of us to run it if we want. For that, you'll want to make sure you're on the *main* branch, not *gh-pages*. 

## Yikes this was a lot of text

LOL. Ping me on Discord if any of this makes no sense or if you get stuck anywhere!!!
