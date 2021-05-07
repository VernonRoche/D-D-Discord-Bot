import os

from Source.Player_Information.SkillsArmor import calculate_passive_skills

from Source.Utility.Utilities import open_character_file, save_char_file, separate_long_text


####
#### Functions used by Character Cog
####
async def display_character(ctx, character, *args):
    for ar in args:
        if ar != "":
            character = character + " " + ar
    char_dictionary = open_character_file(character)
    result = f"```ml\n"
    passive_skills = calculate_passive_skills(character)

    # Name level, race and class
    result = result + "     '" + char_dictionary['name'] + "'     \n" + "🔰Level " + str(char_dictionary['level']) \
             + " " + char_dictionary['race'] + " " + char_dictionary['class'] + "\n"

    # Armor class
    result = result + "🛡️Armor Class: " + str(char_dictionary['armor_class']) + "\n"
    # HP, Initiative and Coins
    result = result + "🩸Current HP: " + str(char_dictionary['hp']) + "\n⚔️Initiative: " \
             + str(char_dictionary['initiative']) + "\n💰Current Coins: " \
             + str(char_dictionary['coins']) + "\n"

    # Attributes and passive skills to the right side
    attributes = char_dictionary['attributes']
    result = result + "💥Strength: " + str(attributes['strength']) + "\n🎯Dexterity: " \
             + str(attributes['dexterity']) + "\n💖Constitution: " + \
             str(attributes['constitution']) + "\n💫Intelligence: " + str(
        attributes['intelligence']) + "\n💡Wisdom: " + \
             str(attributes['wisdom']) + "\n🎭Charisma: " + \
             str(attributes['charisma']) + "\n"
    # Proficiencies
    proficiencies = ""
    for i in char_dictionary['proficiencies']:
        proficiencies = proficiencies + "," + i
    proficiencies = proficiencies[1:]
    result = result + "🎲Proficiencies: " + proficiencies + "\n" + "🔍Passive Investigation: " + \
             str(passive_skills[1]) + "\n" + \
             "🗣️Passive Insight: " + str(passive_skills[0]) + "\n" + \
             "❗Passive Perception: " + str(passive_skills[0]) + "\n"

    # Weapons and Items
    result = result + "🏹Weapons: " + char_dictionary['weapons'] + "\n👜Items: " + char_dictionary['items'] + "\n"
    # Armors
    armor_list = ""
    for x in char_dictionary['armors']:
        armor_list = armor_list + " " + x[0]
    armor_list = armor_list[1:]
    result = result + "💠Armors: " + armor_list + "\n"
    # Feats
    result = result + "🔰Feats: " + char_dictionary['feats'] + "```"
    # Spell slots
    spellslots = "{"
    for x in char_dictionary['active_spellslots']:
        spellslots = spellslots + str(x) + ", "
    spellslots = spellslots[:-2] + "}"
    result = result + "☄️Available Spell Slots: " + spellslots

    await ctx.send(result)
    return


async def delete_character(ctx, character, *args):
    for ar in args:
        if ar != "":
            character = character + " " + ar
    if os.path.exists("../Characters/" + character + ".json"):
        os.remove("../Characters/" + character + ".json")
        await ctx.send("``Good riddance``")
    else:
        await ctx.send("``This character does not exist``")
    return


async def spell_book(ctx, character, *args):
    char_dictionary = open_character_file(character, *args)
    result = "```\n"
    result = result + char_dictionary['spells'] + "\n"
    result = result + "Spell Slots: {"
    for i in char_dictionary['spellslots']:
        result = result + str(i) + ", "
    result = result[:-2] + "}```\n"
    await ctx.send(result)
    return


# TO BE COMPLETED
async def cast_spell(ctx, spellname, character, *args):
    char_dictionary = open_character_file(character, *args)
    char_dictionary['spells'] = char_dictionary['spells'].split(',')
    is_owned = map(lambda i: i.lower(), char_dictionary['spells'])
    if spellname.lower() not in is_owned:
        await ctx.send("You do not have this spell!")
    else:
        slots = char_dictionary['spellslots']
        path = "../Spells/" + spellname + ".txt"
        ftemp = open(path, "r")
        tfile = ftemp.read()
        ftemp.close()
        t2file = tfile.split('\n')
        level = t2file[1][-3]
        if level.isnumeric():
            level = int(level) - 1
            if slots[level] == 0:
                while level <= 8:
                    if slots[level] > 0:
                        slots[level] = slots[level] - 1
                        break
                    level = level + 1
            else:
                slots[level] = slots[level] - 1
            if level == 9:
                await ctx.send("You can't use any spell slot to cast this spell!")
                return

        # values are good and spell can be shown. Show new spell slots
        char_dictionary['spellslots'] = slots
        save_char_file(char_dictionary)
        tfile = separate_long_text(tfile)
        for i in tfile:
            await ctx.send("```diff\n-" + i + "```")


def short_rest(character_dictionary, hit_dice):
    # checks character class and constitution and number of hit_dice
    # roll hit_dice*(class_dice+constitution)
    # replenish some features/spells
    pass


def long_rest(character_dictionary):
    pass


# Induce damage to a target character
def damage(damage_amount, target):
    pass
