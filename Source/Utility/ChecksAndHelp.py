import glob

from Source.Items_And_Actions.Armor import Armors
from Source.Items_And_Actions.Weapon import Weapons
from Source.Utility import Globals


# verify if the message received in chat is from the person that called the command
def check_author_channel(ctx, msg):
    return msg.author == ctx.author and msg.channel == ctx.channel


# verify if we call the same command as the one we are currently in
def is_command_rerun_requested(command, message):
    if command in message:
        return True
    return False


# verifies if a command rerun or cancel is requested
def should_exit_command(current_command, response):
    if is_command_rerun_requested(current_command, response):
        return True
    if Globals.is_cancel_requested:
        Globals.is_cancel_requested = False
        return True
    return False


# verify if character class exists
def is_class_valid(name):
    tempclasses = [f for f in glob.glob("../Character Classes/" + "*.txt")]
    classes = ""
    for f in tempclasses:
        f = f.lower()
        classes = classes + "," + f[21:-4]
    classes = classes[1:]
    if name.lower() not in classes:
        print("false here")
        return False
    print("true here")
    return True


# verify if character race exists
# verify if character race exists
def is_race_valid(name):
    return name.lower() in {
        'human',
        'orc',
        'half elf',
        'elf',
        'dragonborn',
        'aasimar',
        'halfling',
        'dwarf',
        'gnome',
        'half orc',
        'tiefling'
    }


# verify if spell exists
def is_spell_valid(name):
    tempspells = [f for f in glob.glob("../Spells/" + "*.txt")]
    spells = ""
    for f in tempspells:
        f = f.lower()
        spells = spells + "," + f[7:-4]
    spells = spells[1:]
    if name.lower() == "dnd":
        return True
    if name.lower() not in spells:
        return False
    return True


# TO BE COMPLETED
# verify if feat exists
def is_feat_valid(name):
    return True


# verify if a numerical value is valid, depending on the category it is
# name=type of value checked, arg=value to check
def is_value_valid(arg, name):
    if name == "hp" and arg <= 0:
        return False
    if (name in ("attribute", "level", "spellslot")) and not (0 < arg <= 20):
        return False
    if name == "coins" and arg < 0:
        return False
    if name == "initiative" and not (-10 <= arg <= 10):
        return False
    if name == "skill" and (arg not in ("dnd", "acrobatics", "athletics", "sleight of hand", "stealth"
                                        , "arcana", "history", "investigation", "nature"
                                        , "religion", "animal handling", "insight", "medicine"
                                        , "perception", "survival", "deception", "intimidation", "performance",
                                        "persuasion")):
        return False
    return True


# verifies if weapon name exists in keys of the weapons dictionary
def is_weapon_valid(name, weapon_dictionary=Weapons().weapon_dictionary):
    if " " in name:
        name = name.split(' ')
        newname = ""
        for i in name:
            i = (i.lower()).capitalize()
            newname = newname + i + " "
        newname = newname[:-1]
    else:
        newname = (name.lower()).capitalize()
    if "Dnd" in newname:
        return True
    if newname in weapon_dictionary.keys():
        return True
    return False


# TO BE COMPLETED
def is_item_valid():
    return True


def is_armor_valid(name, armor_dictionary=Armors().armor_dictionary):
    if " " in name:
        name = name.split(' ')
        newname = ""
        for i in name:
            i = (i.lower()).capitalize()
            newname = newname + i + " "
        newname = newname[:-1]
    else:
        newname = (name.lower()).capitalize()
    if "Dnd" in newname:
        return True
    if newname in armor_dictionary.keys():
        return True
    return False


# Receives an armor tuple (name,bool) and sends if it's equipped
def is_armor_equipped(armor):
    return armor[1]


# TO BE COMPLETED
# Checks if multiple armors are equipped. Does not count if it's a shield
def are_multiple_armors_equipped(armors):
    return


# TO BE COMPLETED
# Checks if there are enough available hit dice
def can_throw_hit_dice(character_level, requested_dice):
    return True


# Checks if message is sent by the owner in the same channel as before (usually when responding to a command)
def is_message_by_owner(ctx, msg):
    return msg.author == ctx.author and msg.channel == ctx.channel


# Checks if that string contains a valid type of coin
def is_coin_valid(coin):
    coin = coin.lower()
    if coin != "copper" and coin != "silver" and coin != "gold" and coin != "electrum" and coin != "platinum":
        return False
    return True


# Gets previous coin type
def get_previous_coin_type(coin):
    coin = coin.lower()
    if coin == "copper" or coin == "silver":
        return "copper"
    elif coin == "electrum":
        return "silver"
    elif coin == "gold":
        return "electrum"
    else:
        return "gold"


# Gets next coin type
def get_next_coin_type(coin):
    coin = coin.lower()
    if coin == "copper":
        return "silver"
    elif coin == "silver":
        return "electrum"
    elif coin == "electrum":
        return "gold"
    else:
        return "platinum"
