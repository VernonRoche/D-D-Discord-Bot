from Source.Player_Information.Decorators import feature, playable
from Source.Player_Information.PlayerClass import PlayerClass
from Source.Utility.Utilities import get_value_between_values

rage_per_level_in = [1, 2, 5, 12, 17, 20]
rage_per_level_out = [1, 2, 3, 4, 5, 6]
rage_dmg_per_level_in = [1, 9, 16]
rage_dmg_per_level_out = [2, 3, 4]


barbarian_class_features = {
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


@playable
class Barbarian(PlayerClass):
    class_name = "Barbarian"
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

    def __init__(self):
        super().__init__()

    # for testing only
    def simulate_on_level_up(self, new_level: int):
        self.on_level_up(new_level)

    def get_spell_slots(self):
        return 0

    def get_levelup_hp(self, constitution):
        return self.hit_points + constitution

    def get_initial_equipment(self):
        # TO BE FURTHER IMPLEMENTED
        return [["Greataxe", "Martial Weapon"], ["2 Handaxe", "Simple Weapon"]]

    @property
    def get_rage_points(self):
        return get_value_between_values(self.level, rage_per_level_in, rage_per_level_out, 50)

    @property
    def get_rage_damage(self):
        return get_value_between_values(self.level, rage_dmg_per_level_in, rage_dmg_per_level_out, 5)

    @feature("Rage", level=10)
    def rage(self):
        print("do raging stuff")

