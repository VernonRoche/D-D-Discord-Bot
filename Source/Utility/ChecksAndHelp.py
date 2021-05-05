import glob

from Source.Items_And_Actions.Weapon import Weapons
from Source.Utility import Globals
from Source.Utility.Messaging import send_cancelable_message


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
def is_race_valid(name):
    name = name.lower()
    if (
            name == "human" or name == "orc" or name == "half elf" or name == "elf" or name == "dragonborn" or name == "aasimar" or
            name == "halfling" or name == "dwarf" or name == "gnome" or name == "half orc" or name == "tiefling"):
        return True
    return False


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


# verify if feat exists
def is_feat_valid(name):
    return True


# verify if a numerical value is valid, depending on the category it is
# name=type of value checked, arg=value to check
def is_value_valid(arg, name):
    if name == "hp" and arg <= 0:
        return False
    if (name == "attribute" or name == "level" or name == "spellslot") and (arg <= 0 or arg > 20):
        return False
    if name == "coins" and arg < 0:
        return False
    if name == "initiative" and (arg < -10 or arg > 10):
        return False
    if name == "skill" and (arg != "dnd" and
                            arg != "acrobatics" and arg != "athletics" and arg != "sleight of hand" and arg != "stealth" and
                            arg != "arcana" and arg != "history" and arg != "investigation" and arg != "nature" and
                            arg != "religion" and arg != "animal handling" and arg != "insight" and arg != "medicine" and
                            arg != "perception" and arg != "survival" and arg != "deception" and arg != "intimidation" and
                            arg != "performance" and arg != "persuasion"):
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

def is_item_valid():
    return True
