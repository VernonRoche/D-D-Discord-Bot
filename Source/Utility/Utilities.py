import json

# pass character name to return a dictionary containing his information
from Source.Utility.Globals import emojis


def open_character_file(character, *args):
    for ar in args:
        if ar != "":
            print(ar)
            character = character + " " + ar

    path = "../Characters/" + character + ".json"
    with open(path, 'r') as input_file:
        return json.load(input_file)


# takes a dictionary with character information and saves it into a .json file
def save_char_file(char_dictionary):
    filename = "../Characters/" + char_dictionary['name'] + ".json"
    with open(filename, "w+") as output_file:
        json.dump(char_dictionary, output_file)


def populate_character_dictionary(name, race, myclass, level, hp, coins, attributes, weapons, items, initiative,
                                  proficiences, spells, feats, spellslots, armor_class, armors, active_spellslots):
    # convert array of attributes into dictionary
    attributes = [int(x) for x in attributes]
    attributes_dict = {'strength': attributes[0], 'dexterity': attributes[1], 'constitution': attributes[2],
                       'intelligence': attributes[3], 'wisdom': attributes[4], 'charisma': attributes[5]}

    # populate dictionary
    char_dictionary = {'name': name, 'race': race, 'class': myclass, 'level': int(level), 'hp': int(hp),
                       'coins': int(coins), 'attributes': attributes_dict, 'weapons': weapons, 'items': items,
                       'initiative': int(initiative), 'proficiencies': proficiences, 'spells': spells, 'feats': feats,
                       'spellslots': spellslots, 'active_spellslots': active_spellslots, 'armor_class': armor_class,
                       'armors': armors}
    print(char_dictionary)
    return char_dictionary


# checks if a text is too long for a single discord message
def is_long_text(text):
    if len(text) >= 1900:
        return True
    return False


# looks for the nearest text breaking character and returns it's location.
# look_for_format indicates if it must search the end of ``` for text formatting
def detect_endof_word(text, position, look_for_format):
    if not look_for_format:
        counter = position
        for char in text[position:]:
            counter += 1
            if char == ' ' or char == ',' or char == '\n':
                return counter

    else:
        counter = position
        format_counter = 0
        for char in text[position:]:
            if char == '`':
                format_counter += 1
            counter += 1
            if format_counter == 3:
                return counter


# recursively separates a long text into an array of texts with 1900 or less words
def separate_long_text(text, look_for_format=False):
    if is_long_text(text):
        separator = detect_endof_word(text, 1900, look_for_format)
        left, right = text[:(separator + 1)], text[separator:]
        return [left] + separate_long_text(right)
    else:
        return [text]


def merge_name(character_name, args):
    for ar in args:
        if ar != "":
            character_name = character_name + " " + ar
    return character_name


###
#   This function takes a value, and check if it is in the bounds of inputs
#   If yes then returns corresponding output, else just default
###
def get_value_between_values(value, inputs, outputs):
    if len(inputs)-len(outputs) != 1:
        raise ValueError
    for i in range(len(inputs) - 1):
        if inputs[i] <= value < inputs[i + 1]:
            return outputs[i]
    raise ValueError


async def this_is_some_alien_bababouy(ctx):
    i = 0
    fuckfest = ""
    while i < 25:
        fuckfest = fuckfest + emojis["DANCING PARROT"]
        i = i + 1
    tab = separate_long_text(fuckfest)
    for x in tab:
        await ctx.send(x)
