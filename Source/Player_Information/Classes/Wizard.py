from Source.Player_Information.Class import Class


class Wizard(Class):
    name = "Wizard"

    hit_points = 4

    hit_dice = 6
    # The number of proficiencies they will be able to choose at level 1
    proficiency_number: 2

    ability_score_improvement_levels = [4, 8, 12, 16, 19]

    spellcasting = True

    spellcasting_ability = "Intelligence"

    proficiencies = {
        'Armor': [],
        'Weapons': ["Daggers", "Darts", "Slings", "Quarterstaffs", "Light Crossbows"],
        'Tools': [],
        'Saving Throws': ["Intelligence", "Wisdom"],
        'Skills': ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
    }

    # TO BE IMPLEMENTED
    class_features = {
        'Spellbook': "",
        'Preparing and Casting Spells': "",
        'Arcane Recovery': "",
        'Arcane Tradition': "",
        'Spell Mastery': "",
        'Signature Spells': "",
    }

    spell_slots_per_level = {
        "1": [2, 0, 0, 0, 0, 0, 0, 0, 0],
        "2": [3, 0, 0, 0, 0, 0, 0, 0, 0],
        "3": [4, 2, 0, 0, 0, 0, 0, 0, 0],
        "4": [4, 3, 0, 0, 0, 0, 0, 0, 0],
        "5": [4, 3, 2, 0, 0, 0, 0, 0, 0],
        "6": [4, 3, 3, 0, 0, 0, 0, 0, 0],
        "7": [4, 3, 3, 1, 0, 0, 0, 0, 0],
        "8": [4, 3, 3, 2, 0, 0, 0, 0, 0],
        "9": [4, 3, 3, 3, 1, 0, 0, 0, 0],
        "10": [4, 3, 3, 3, 2, 0, 0, 0, 0],
        "11": [4, 3, 3, 3, 2, 1, 0, 0, 0],
        "12": [4, 3, 3, 3, 2, 1, 0, 0, 0],
        "13": [4, 3, 3, 3, 2, 1, 1, 0, 0],
        "14": [4, 3, 3, 3, 2, 1, 1, 0, 0],
        "15": [4, 3, 3, 3, 2, 1, 1, 0, 0],
        "16": [4, 3, 3, 3, 2, 1, 1, 1, 0],
        "17": [4, 3, 3, 3, 2, 1, 1, 1, 0],
        "18": [4, 3, 3, 3, 3, 1, 1, 1, 1],
        "19": [4, 3, 3, 3, 3, 2, 1, 1, 1],
        "20": [4, 3, 3, 3, 3, 2, 2, 1, 1],
    }

    def get_spell_slots(self, level):
        return self.spell_slots_per_level[str(level)]

    def get_levelup_hp(self, constitution):
        return self.hit_points + constitution

    def get_initial_equipment(self):
        # TO BE FURTHER IMPLEMENTED
        return [["Quarterstaff", "Dagger"], ["Component Pouch", "Arcane Focus"], ["Scholar's Pack", "Explorer's Pack"],
                "Spellbook"]

    def to_string(self):
        return "Wizard"
