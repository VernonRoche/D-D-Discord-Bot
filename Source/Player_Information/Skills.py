from Source.Utility.Utilities import open_character


def calculate_passive_skills(character, *args):
    for ar in args:
        if ar != "":
            character = character + " " + ar
    file = open_character(character)
    proficiency = calculate_level_proficiency(file[3]) + 10
    attributes = file[6]
    return [proficiency + calculate_attribute_bonus(attributes[4]),
            proficiency + calculate_attribute_bonus(attributes[3])]


def calculate_level_proficiency(level):
    if level >= 1 and level < 5:
        return 2
    if level >= 5 and level < 9:
        return 3
    if level >= 9 and level < 13:
        return 4
    if level >= 13 and level < 17:
        return 5
    if level >= 17:
        return 6


def calculate_attribute_bonus(attr):
    if attr >= 10:
        attr -= 10
        return attr // 2
    else:
        attr -= 10
        return attr // 2


def skill_modifier(character, skill, *args):
    for ar in args:
        if ar != "":
            character = character + " " + ar

    file = open_character(character)
    proficiency = file[10]
    prof = calculate_level_proficiency(file[3])

    # check which skill is called and if it's in the proficiency array, used to show which proficiences the character has
    if skill.lower() == "athletics" and ("Athletics" in proficiency):
        return calculate_attribute_bonus(file[6][0]) + prof
    if skill.lower() == "athletics":
        return calculate_attribute_bonus(file[6][0])

    if (skill.lower() == "acrobatics" and ("Acrobatics" in proficiency)) or (skill.lower() == "sleight of hand" and (
            ("Sleight of hand" in proficiency) or ("Sleight of Hand" in proficiency))) or (
            skill.lower() == "stealth" and ("Stealth" in proficiency)):
        return calculate_attribute_bonus(file[6][1]) + prof
    if skill.lower() == "acrobatics" or skill.lower() == "sleight of hand" or skill.lower() == "stealth":
        return calculate_attribute_bonus(file[6][1])

    if (skill.lower() == "arcana" and ("Arcana" in proficiency)) or (
            skill.lower() == "history" and ("History" in proficiency)) or (
            skill.lower() == "investigation" and ("Investigation" in proficiency)) or (
            skill.lower() == "nature" and ("Nature" in proficiency)) or (
            skill.lower() == "religion" and ("Religion" in proficiency)):
        return calculate_attribute_bonus(file[6][3]) + prof
    if skill.lower() == "arcana" or skill.lower() == "history" or skill.lower() == "investigation" or skill.lower() == "nature" or skill.lower() == "religion":
        return calculate_attribute_bonus(file[6][3])

    if (skill.lower() == "animal handling" and (
            ("Animal handling" in proficiency) or ("Animal Handling" in proficiency))) or (
            skill.lower() == "insight" and ("Insight" in proficiency)) or (
            skill.lower() == "medicine" and ("Medicine" in proficiency)) or (
            skill.lower() == "perception" and ("Perception" in proficiency)) or (
            skill.lower() == "survival" and ("Survival" in proficiency)):
        return calculate_attribute_bonus(file[6][4]) + prof
    if skill.lower() == "animal handling" or skill.lower() == "insight" or skill.lower() == "medicine" or skill.lower() == "perception" or skill.lower() == "survival":
        return calculate_attribute_bonus(file[6][4])

    if (skill.lower() == "deception" and ("Deception" in proficiency)) or (
            skill.lower() == "intimidation" and ("Intimidation" in proficiency)) or (
            skill.lower() == "performance" and ("Performance" in proficiency)) or (
            skill.lower() == "persuasion" and ("Persuasion" in proficiency)):
        return calculate_attribute_bonus(file[6][5]) + prof
    if skill.lower() == "deception" or skill.lower() == "intimidation" or skill.lower() == "performance" or skill.lower() == "persuasion":
        return calculate_attribute_bonus(file[6][5])

    else:
        return "error"
