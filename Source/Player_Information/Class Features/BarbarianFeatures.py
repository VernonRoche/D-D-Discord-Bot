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
        # add missing features from available_features and add them to player dictionary
        # save character
        pass

    def available_features(self, level):
        # for each level where you gain a feature check the available ones and create a list
        return []

    def to_string(self):
        result=""
        for x in self.feature_list:
            result=result+" "+x
        result=result[1:]
        return result