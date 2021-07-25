from Source.Items_And_Actions.Armor import *
from Source.Utility.Utilities import open_character_file


def calculate_passive_skills(character, *args):
    for ar in args:
        if ar != "":
            character = character + " " + ar
    char_dictionary = open_character_file(character)
    proficiency = calculate_level_proficiency(char_dictionary['level']) + 10
    attributes = char_dictionary['attributes']
    return [proficiency + calculate_attribute_bonus(attributes['wisdom']),
            proficiency + calculate_attribute_bonus(attributes['intelligence'])]


def calculate_level_proficiency(level):
    return ((level - 1) // 4) + 2


def calculate_attribute_bonus(attr):
    attr -= 10
    return attr // 2


def skill_modifier(character, skill, *args):
    for ar in args:
        if ar != "":
            character = character + " " + ar

    char_dictionary = open_character_file(character)
    proficiency = char_dictionary['proficiencies']
    prof = calculate_level_proficiency(char_dictionary['level'])
    skill = skill.lower()
    str_skills = ["strength", ["Athletics"]]
    dex_skills = ["dexterity", ["Acrobatics", "Sleight of Hand", "Stealth"]]
    int_skills = ["intelligence", ["Arcana", "History", "Investigation", "Nature", "Religion"]]
    wis_skills = ["wisdom", ["Animal Handling", "Insight", "Medicine", "Perception", "Survival"]]
    cha_skills = ["charisma", ["Deception", "Intimidation", "Persuasion", "Performance"]]
    skills_list = [str_skills, dex_skills, int_skills, wis_skills, cha_skills]

    # check which skill is called and if it's in the proficiency array, used to show which proficiencies the character
    # has
    for skill_category in skills_list:
        for x in skill_category[1]:
            lower_x = x.lower()
            if skill == lower_x and x in proficiency:
                return calculate_attribute_bonus(char_dictionary['attributes'][skill_category[0]]) + prof
            if skill == lower_x:
                return calculate_attribute_bonus(char_dictionary['attributes'][skill_category[0]])
    return "error"


def calculate_armor_class(dexterity, armor):
    if armor is None:
        return dexterity
    if armor.name in medium_armors:
        if dexterity > 2:
            dexterity = 2
        return armor.armor_class + dexterity
    if armor.name in heavy_armors:
        return armor.armor_class
    return dexterity + armor.armor_class
