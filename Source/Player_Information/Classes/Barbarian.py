from Source.Player_Information.Class import Class


class Barbarian(Class):
    name = "Barbarian"
    hit_points = 7
    hit_dice = 12
    proficiency_number = 2
    ability_score_improvement_levels = [4, 8, 12, 16, 19]
    spellcasting = False
    spellcasting_ability = ""
    profiencies = {
        'Armor': ["Light Armor", "Medium Armor", "Shields"],
        'Weapons': ["Simple Weapons", "Martial Weapons"],
        'Tools': [],
        'Saving Throws': ["Strength", "Constitution"],
        'Skills': ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
    }
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

    def get_spell_slots(self, level):
        return 0

    def get_levelup_hp(self, constitution):
        return self.hit_points + constitution

    def get_initial_equipment(self):
        # TO BE FURTHER IMPLEMENTED
        return [["Greataxe", "Martial Weapon"], ["2 Handaxe", "Simple Weapon"]]

    def to_string(self):
        return "Barbarian"

    def get_rage_points(self, level):
        if level < 2:
            return 2
        elif 2 < level < 6:
            return 3
        elif 5 < level < 12:
            return 4
        elif 12 < level < 17:
            return 5
        elif 17 < level < 20:
            return 6
        else:
            return 50

    def get_rage_damage(self, level):
        if level < 9:
            return 2
        elif 9 < level < 16:
            return 3
        else:
            return 4
