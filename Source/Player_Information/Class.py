from abc import ABC, abstractmethod


class Class(ABC):

    name: str

    hit_points: int

    hit_dice: int
    # The number of proficiencies they will be able to choose at level 1
    proficiency_number: int

    ability_score_improvement_levels: list

    spellcasting: bool

    spellcasting_ability: str

    proficiencies: dict

    class_features: dict

    @abstractmethod
    def get_spell_slots(self, level):
        return NotImplementedError

    @abstractmethod
    def get_levelup_hp(self,constitution):
        return NotImplementedError

    @abstractmethod
    def to_string(self):
        return NotImplementedError

    @abstractmethod
    def get_initial_equipment(self):
        return NotImplementedError



