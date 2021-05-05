from abc import ABC, abstractmethod


class ClassFeatures(ABC):
    classname: str

    feature_list: list

    @abstractmethod
    def add_to_available_features(self, feature_dictionary):
        return NotImplementedError

    @abstractmethod
    def available_features(self, level):
        return NotImplementedError
