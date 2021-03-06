import os

from Source.Player_Information.Skills_AC import calculate_passive_skills

from Source.Utility.Utilities import open_character_file, save_char_file, separate_long_text, merge_name

from Source.Utility.Globals import emojis


####
#### Functions used by Character Cog
####
async def display_character(ctx, character, *args):
    character = merge_name(character, args)
    char_dictionary = open_character_file(character)
    result = f"```ml\n"
    passive_skills = calculate_passive_skills(character)

    # Name level, race and class
    result = result + "     '" + char_dictionary['name'] + "'     \n" + emojis["SHIELD YELLOW GREEN"]+  "Level " + str(char_dictionary['level']) \
             + " " + char_dictionary['race'] + " " + char_dictionary['class'] + "\n"

    # Armor class
    result = result + emojis["SHIELD"]+"Armor PlayerClass: " + str(char_dictionary['armor_class']) + "\n"
    # HP, Initiative and Coins
    result = result + emojis["BLOOD"] + "Current HP: " + str(char_dictionary['hp']) + emojis["SWORDS"]+"\n️Initiative: " \
             + str(char_dictionary['initiative']) + emojis["MONEY BAG"]+"\nCurrent Coins: " \
             + str(char_dictionary['coins']) + "\n"

    # Attributes and passive skills to the right side
    attributes = char_dictionary['attributes']
    result = result + emojis["EXPLOSION"]+"Strength: " + str(attributes['strength']) + emojis["ARROW TARGET"]+"\nDexterity: " \
             + str(attributes['dexterity']) + emojis["HEART"]+"\nConstitution: " + \
             str(attributes['constitution']) + emojis["ROTATING STAR"]+"\nIntelligence: " + str(
        attributes['intelligence']) + emojis["LIGHT BULB"]+"\nWisdom: " + \
             str(attributes['wisdom']) + emojis["MASKS"]+"\nCharisma: " + \
             str(attributes['charisma']) + "\n"
    # Proficiencies
    proficiencies = ""
    for i in char_dictionary['proficiencies']:
        proficiencies = proficiencies + "," + i
    proficiencies = proficiencies[1:]
    result = result + emojis["DICE"]+"Proficiencies: " + proficiencies + "\n" + emojis["ZOOM"]+"Passive Investigation: " + \
             str(passive_skills[1]) + "\n" + \
             emojis["SPEECH"]+"Passive Insight: " + str(passive_skills[0]) + "\n" + \
             emojis["EXCLAMATION MARK"]+"Passive Perception: " + str(passive_skills[0]) + "\n"

    # Weapons and Items
    result = result + emojis["BOW"]+"Weapons: " + char_dictionary['weapons'] + emojis["BAG"]+"\nItems: " + char_dictionary['items'] + "\n"
    # Armors
    armor_list = ""
    for x in char_dictionary['armors']:
        armor_list = armor_list + " " + x[0]
    armor_list = armor_list[1:]
    result = result + emojis["SHIELD BLUE"]+"Armors: " + armor_list + "\n"
    # Feats
    result = result + emojis["SHIELD YELLOW GREEN"]+"Feats: " + char_dictionary['feats'] + "\n"
    # Spell slots
    spellslots = "{"
    for x in char_dictionary['active_spellslots']:
        spellslots = spellslots + str(x) + ", "
    spellslots = spellslots[:-2] + "}"
    result = result + emojis["STARS"]+"Available Spell Slots: " + spellslots + "```"

    await ctx.send(result)
    return


async def delete_character(ctx, character, *args):
    character = merge_name(character, args)
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


async def cast_with_level(ctx, char_dictionary, spellname, level_request):
    # Check if the requested level exists
    if 9 < level_request < 1:
        await ctx.send(f"``That spell level does not exist``")
        return
    level_request = level_request - 1
    is_owned = map(lambda tmp: tmp.lower(), char_dictionary['spells'])
    # Check if spell is inside owned spells
    if spellname.lower() not in is_owned:
        await ctx.send("You do not have this spell!")
        return
    else:
        # Get spell's level and check if there are available spell slots of the requested level
        slots = char_dictionary['active_spellslots']
        path = "../Spells/" + spellname + ".txt"
        ftemp = open(path, "r")
        tfile = ftemp.read()
        ftemp.close()
        t2file = tfile.split('\n')
        level = t2file[1][-3]
        if level.isnumeric():
            level = int(level) - 1

            # Check if the spell is castable with the requested level
            if level > level_request:
                await ctx.send(f"``The spell you want to cast needs a higher lever spell slot``")
                return
            # See if there are spell slots of that level left
            if slots[level_request] == 0:
                await ctx.send(
                    f"``There are not enough spell slots of the level you requested``")
                return
            await ctx.send(f"``You will cast this spell with a level " + str(level_request + 1) + " slot``")
            slots[level_request] = slots[level_request] - 1

        # values are good and spell can be shown. Show new spell slots
        char_dictionary['active_spellslots'] = slots
        string_slots = "```"+emojis["STARS"]+"Current Spell Slots: {"
        for x in slots:
            string_slots = string_slots + str(x) + ", "
        string_slots = string_slots[:-2] + "}```"
        save_char_file(char_dictionary)
        tfile = separate_long_text(tfile)
        for i in tfile:
            await ctx.send("```diff\n-" + i + "```")
        await ctx.send(string_slots)


# TO BE COMPLETED
def short_rest(character_dictionary, hit_dice):
    # checks character class and constitution and number of hit_dice
    # roll hit_dice*(class_dice+constitution)
    # replenish some features/spells
    pass


# TO BE COMPLETED
def long_rest(character_dictionary):
    pass


# TO BE COMPLETED
# Induce damage to a target character
def damage(damage_amount, target):
    pass
