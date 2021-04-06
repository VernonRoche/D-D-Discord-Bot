import json


# pass character name to return a dictionary containing his information
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

def populate_character_dictionary(name,race,myclass,level,hp,coins,attributes,weapons,items,initiative,proficiences
                                  ,spells,feats,spellslots):
    #convert array of attributes into dictionary
    attributes = [int(x) for x in attributes]
    attributes_dict = {}
    attributes_dict['strength']= attributes[0]
    attributes_dict['dexterity']= attributes[1]
    attributes_dict['constitution']= attributes[2]
    attributes_dict['intelligence']= attributes[3]
    attributes_dict['wisdom']= attributes[4]
    attributes_dict['charisma']= attributes[5]

    #populate dictionary
    char_dictionary={}
    char_dictionary['name']=name
    char_dictionary['race']=race
    char_dictionary['class']=myclass
    char_dictionary['level']=int(level)
    char_dictionary['hp']=int(hp)
    char_dictionary['coins']=int(coins)
    char_dictionary['attributes']=attributes_dict
    char_dictionary['weapons']=weapons
    char_dictionary['items']=items
    char_dictionary['initiative']=int(initiative)
    char_dictionary['proficiencies']=proficiences
    char_dictionary['spells']=spells
    char_dictionary['feats']=feats
    char_dictionary['spellslots']=spellslots
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
    if look_for_format == False:
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




async def this_is_some_alien_bababouy(ctx):
    i = 0
    fuckfest = ""
    while (i < 25):
        fuckfest = fuckfest + ("<a:emoji_1:746866499729489950>")
        i = i + 1
    tab = separate_long_text(fuckfest)
    for x in tab:
        await ctx.send(x)
