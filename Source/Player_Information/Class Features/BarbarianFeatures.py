from Source.Player_Information.ClassFeatures import ClassFeatures


class BarbarianFeatures(ClassFeatures):
    classname = "Barbarian"
    feature_list = ["Rage", "Unarmored Defense", "Reckless Attack", "Danger Sense", "Primal Path", "Extra Attack",
                    "Fast Movement", "Feral Instict", "Brutal Critical", "Relentless Rage", "Brutal Critical Upgrade 2",
                    "Indomitable Might", "Primal Champion"]

    def __init__(self, name):
        self.name = name

    def add_to_available_features(self, feature_dictionary):
        # get level
        # check current features
        # add missing features
        pass

    def available_features(self, level):
        # for each level where you gain a feature check the available ones and create a list
        return []
