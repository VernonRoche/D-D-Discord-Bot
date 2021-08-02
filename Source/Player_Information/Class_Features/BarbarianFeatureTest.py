from Source.Player_Information.ClassFeature import ClassFeature


class BarbarianFeatureTest(ClassFeature):
    classname = "Barbarian"
    feature_list = ["Rage", "Unarmored Defense", "Reckless Attack", "Danger Sense", "Primal Path", "Extra Attack",
                    "Fast Movement", "Feral Instict", "Brutal Critical", "Relentless Rage", "Brutal Critical Upgrade 2",
                    "Indomitable Might", "Primal Champion"]

    def add_to_available_features(self, feature_dictionary):
        # get level
        # check current features
        # add missing features from available_features and add them to player dictionary
        # save character
        pass

    def available_features(self, level):
        # for each level where you gain a feature check the available ones and create a list
        return []

    def to_dict(self):
        # generate a key for each feature in feature_list and put it's corresponding function in the dict value
        return {}

    def to_string(self):
        result = "Barbarian features: "
        for x in self.feature_list:
            result = result + " " + x
        return result
