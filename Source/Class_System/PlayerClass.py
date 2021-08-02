from abc import ABC, abstractmethod

from Source.Class_System.ClassFeature import ClassFeature


class PlayerClass(ABC):
    name: str

    hit_points: int

    hit_dice: int
    # The number of proficiencies they will be able to choose at level 1
    proficiency_number: int

    ability_score_improvement_levels: list

    spellcasting: bool

    spellcasting_ability: str

    proficiencies: dict

    def __init__(self):
        self.level = 1

    def on_level_up(self, new_level):
        """Updates the level attribute, prints and saves unlocked features"""
        self.level = new_level

        new_features = ""

        for feat in self.__all_features():
            if feat.level == new_level:
                new_features += f"Unlocked {feat.name} with min level of {feat.level}"

        print("new features:", new_features)

    @property
    def available_features(self):
        return {
            feat.name: feat
            for feat in self.__all_features()
            if self.level >= feat.level
        }

    def __all_features(self):
        return [feat for feat in self.__dict__.values() if isinstance(feat, ClassFeature)]

    @abstractmethod
    def get_spell_slots(self):
        return NotImplementedError

    @abstractmethod
    def get_levelup_hp(self, constitution):
        return NotImplementedError

    @abstractmethod
    def get_initial_equipment(self):
        return NotImplementedError
