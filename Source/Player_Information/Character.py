class Character():
    def __init__(self, name, race, myclass, level, hp, coin, attributes, weapons, items, initiative, proficiencies,spells,feats,spellslots):
        self.name = name
        self.race = race
        self.myclass = myclass
        self.attributes = attributes
        self.coin = coin
        self.level = level
        self.hp = hp
        self.weapons = weapons
        self.items = items
        self.initiative = initiative
        self.proficiencies = proficiencies
        self.spells=spells
        self.feats=feats
        self.spellslots=spellslots
    async def save(self):
        filename = "../../Characters/" + self.name + ".txt"
        saves = open(filename, "w+")
        saves.write(self.name + "$")
        saves.write(self.race + "$")
        saves.write(self.myclass + "$")
        saves.write(str(self.level) + "$")
        saves.write(str(self.hp) + "$")
        saves.write(str(self.coin) + "$")
        for i in self.attributes:
            saves.write(str(i) + ",")
        saves.write("$")
        saves.write(self.weapons + "$")
        saves.write(self.items + "$")
        saves.write(str(self.initiative) + "$")
        for i in self.proficiencies:
            saves.write(i + ",")
        saves.write("$")
        saves.write("@")

        saves.write(self.spells +"$")
        saves.write(self.feats +"$")
        for i in self.spellslots:
            saves.write(str(i)+",")
        saves.close()
