from abc import ABC, abstractmethod


class Class(ABC):

    name: str

    hit_points: int

    proficiencies: dict

    spellcasting: bool

    spellcasting_ability: str

    class_features: dict

    ability_score_improvement_levels: list
# The number of proficiencies they will be able to choose at level 1
    proficiency_number: int

    @abstractmethod
    def get_spell_slots(self, level):
        return NotImplementedError

    @abstractmethod
    def get_levelup_hp(self,constitution):
        return NotImplementedError

    @abstractmethod
    def to_string(self):
        return NotImplementedError



