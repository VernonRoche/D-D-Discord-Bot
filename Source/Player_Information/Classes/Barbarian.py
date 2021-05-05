from Source.Player_Information.Class import Class


class Barbarian(Class):
    name = "Barbarian"
    hit_points = 7
    profiencies = {
        'Armor': ["Light Armor", "Medium Armor", "Shields"],
        'Weapons': ["Simple Weapons", "Martial Weapons"],
        'Tools': [],
        'Saving Throws': ["Strength", "Constitution"],
        'Skills': ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
    }
    spellcasting = False
    spellcasting_ability = ""
    # TO BE IMPLEMENTED
    class_features = {
        'Rage': "",
        'Unarmored Defense': "",
        'Reckless Attack': "",
        'Danger Sense': "",
        'Primal Path': "",
        'Extra Attack': "",
        'Fast Movement': "",
        'Feral Instinct': "",
        'Brutal Critical': "",
        'Relentless Rage': "",
        'Brutal Critical Upgrade': "",
        'Persistent Rage': "",
        'Brutal Critical Upgrade 2': "",
        'Indomitable Might': "",
        'Primal Champion': ""
    }
    proficiency_number = 2
    ability_score_improvement_levels = [4, 8, 12, 16, 19]

    def __init__(self, name):
        self.name = name

    def get_spell_slots(self, level):
        return 0

    def get_levelup_hp(self, constitution):
        return self.hit_points + constitution

    def initial_equipment(self):
        # TO BE FURTHER IMPLEMENTED
        return [["Greataxe", "Martial Weapon"], ["2 Handaxe", "Simple Weapon"]]

    def to_string(self):
        return "Barbarian"
