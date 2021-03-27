import difflib
import asyncio
from discord.ext import commands
from Utilities import separate_long_text


class Weapon:
    def __init__(self, name, cost, damage_die, damage_type, weight, properties):
        self.name = name
        self.cost = cost
        self.damage_die = damage_die
        self.damage_type = damage_type
        self.weight = weight
        self.properties = properties

    async def to_string(self):
        ret_string = f'''```diff
- {self.name} -
{self.damage_die}  {self.damage_type}
{self.properties}
{self.weight}, {self.cost}```'''

        if self.properties == " ":
            ret_string = f'''```diff
- {self.name} -
{self.damage_die}  {self.damage_type}
{self.weight}, {self.cost}```'''

        return ret_string


class Weapons:
    def __init__(self):
        self.weapon_dictionary = {}

        self.populate_dicitonary()

    def populate_dicitonary(self):
        club = Weapon("Club", "1sp", "1d4", "bludgeoning", "2 lb", "Light")
        self.weapon_dictionary[club.name] = club
        dagger = Weapon("Dagger", "2gp", "1d4", "piercing", "1 lb", "Finesse, light, thrown (range 20/60)")
        self.weapon_dictionary[dagger.name] = dagger
        greatclub = Weapon("Greatclub", "2sp", "1d8", "bludgeoning", "10 lb", "Two-handed")
        self.weapon_dictionary[greatclub.name] = greatclub
        handaxe = Weapon("Handaxe", "5gp", "1d6", "slashing", "2 lb", "Light, thrown (range 20/60)")
        self.weapon_dictionary[handaxe.name] = handaxe
        javelin = Weapon("Javelin", "5sp", "1d6", "piercing", "2 lb", "Thrown (range 30/120)")
        self.weapon_dictionary[javelin.name] = javelin
        light_hammer = Weapon("Light Hammer", "2gp", "1d4", "bludgeoning", "2 lb", "Light, thrown (range 20/60)")
        self.weapon_dictionary[light_hammer.name] = light_hammer
        mace = Weapon("Mace", "5gp", "1d6", "bludgeoning", "4 lb.", "-")
        self.weapon_dictionary[mace.name] = mace
        quarterstaff = Weapon("Quarterstaff", "2sp", "1d6", "bludgeoning", "4 lb", "Versatile (1d8")
        self.weapon_dictionary[quarterstaff.name] = quarterstaff
        sickle = Weapon("Sickle", "1gp", "1d4", "slashing", "2 lb", "Light")
        self.weapon_dictionary[sickle.name] = sickle
        spear = Weapon("Spear", "1gp", "1d4", "bludgeoning", "3 lb", "Thrown (range 20/60), versatile (1d8)")
        self.weapon_dictionary[spear.name] = spear
        crossbow = Weapon("Crossbow", "25gp", "1d8", "piercing", "5 lb",
                          "Ammunition (range 80/320), loading, two-handed")
        self.weapon_dictionary[crossbow.name] = crossbow
        dart = Weapon("Dart", "5cp", "1d4", "piercing", ".25 lb", "Finesse, thrown (range 20/60)")
        self.weapon_dictionary[dart.name] = dart
        shortbow = Weapon("Shortbow", "25gp", "1d6", "piercing", "2 lb", "Ammunition (range 80/320), two-handed")
        self.weapon_dictionary[shortbow.name] = shortbow
        sling = Weapon("Sling", "1sp", "1d4", "bludgeoning", " ", "Ammunition (range 30/120)")
        self.weapon_dictionary[sling.name] = sling

        battleaxe = Weapon("Battleaxe", "10gp", "1d8", "slashing", "4 lb", "Versatile (1d10)")
        self.weapon_dictionary[battleaxe.name] = battleaxe
        flail = Weapon("Flail", "10gp", "1d8", "bludgeoning", "2 lb", " ")
        self.weapon_dictionary[flail.name] = flail
        glaive = Weapon("Glaive", "20gp", "1d10", "slashing", "6 lb", "Heavy, two-handed")
        self.weapon_dictionary[glaive.name] = glaive
        greataxe = Weapon("Greataxe", "30gp", "1d12", "slashing", "7 lb", "Heavy, two-handed")
        self.weapon_dictionary[greataxe.name] = greataxe
        greatsword = Weapon("Greatsword", "50gp", "2d6", "slashing", "6 lb", "Heavy, two-handed")
        self.weapon_dictionary[greatsword.name] = greatsword
        halberd = Weapon("Halberd", "20gp", "1d10", "slashing", "6 lb", "Heavy, reach, two-handed")
        self.weapon_dictionary[halberd.name] = halberd
        lance = Weapon("Lance", "10gp", "1d12", "piercing", "6 lb", "Reach, special")
        self.weapon_dictionary[lance.name] = lance
        longsword = Weapon("Longsword", "15gp", "1d8", "slashing", "3 lb", "Versatile (1d10)")
        self.weapon_dictionary[longsword.name] = longsword
        maul = Weapon("Maul", "10gp", "2d6", "bludgeoning", "10 lb", "Heavy, two-handed")
        self.weapon_dictionary[maul.name] = maul
        morningstar = Weapon("Morningstar", "15gp", "1d8", "piercing", "4 lb", " ")
        self.weapon_dictionary[morningstar.name] = morningstar
        pike = Weapon("Pike", "5 gp", "1d10", "piericng", "18 lb", "Heavy, reach, two-handed")
        self.weapon_dictionary[pike.name] = pike
        rapier = Weapon("Rapier", "25gp", "1d8", "piercing", "2 lb", "Finesse")
        self.weapon_dictionary[rapier.name] = rapier
        scimitar = Weapon("Scimitar", "25gp", "1d6", "slashing", "3 lb", "Finesse, light")
        self.weapon_dictionary[scimitar.name] = scimitar
        shortsword = Weapon("Shortsword", "10gp", "1d6", "piercing", "2 lb", "Finesse, light")
        self.weapon_dictionary[shortsword.name] = shortsword
        trident = Weapon("Trident", "5gp", "1d6", "piercing", "4 lb", "Thrown (range 20/60), versatile (1d8)")
        self.weapon_dictionary[trident.name] = trident
        warpick = Weapon("War pick", "5gp", "1d8", "piercing", "2 lb", " ")
        self.weapon_dictionary[warpick.name] = warpick
        warhammer = Weapon("Warhammer", "15gp", "1d8", "bludgeoning", "2 lb", "Versatile (1d10)")
        self.weapon_dictionary[warhammer.name] = warhammer

        whip = Weapon("Whip", "2gp", "1d4", "slashing", "3 lb", "Finesse, reach")
        self.weapon_dictionary[whip.name] = whip
        blowgun = Weapon("Blowgun", "10gp", "1", "piercing", "1 lb", "Ammunition (range 25/100), loading")
        self.weapon_dictionary[blowgun.name] = blowgun
        crossbow_hand = Weapon("Hand Crossbow", "75gp", "1d6", "piercing", "3 lb",
                               "Ammunition (range 30/120), light, loading")
        self.weapon_dictionary[crossbow_hand.name] = crossbow_hand
        crossbow_heavy = Weapon("Heavy Crossbow", "50gp", "1d10", "piercing", "18 lb",
                                "Ammunition (range 100/400), heavy, loading, two-handed")
        self.weapon_dictionary[crossbow_heavy.name] = crossbow_heavy
        longbow = Weapon("Longbow", "50gp", "1d8", "piercing", "2 lb", "Ammunition (range 150/600), heavy, two-handed")
        self.weapon_dictionary[longbow.name] = longbow
        net = Weapon("Net", "1gp", " ", " ", "3 lb", "Special, thrown (range 5/15)")
        self.weapon_dictionary[net.name] = net
        chains_of_order = Weapon("Chains of Order", "500 gp", "2d6", "piercing", "2 lb",
                                 "Reach, finesse, critical (1d4 radiant)")
        self.weapon_dictionary[chains_of_order.name] = chains_of_order

    async def search(self, search):
        close_matches = difflib.get_close_matches(search, list(self.weapon_dictionary.keys()))

        if len(close_matches) == 0:
            return False

        return self.weapon_dictionary[close_matches[0]]


class WeaponCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["weapons"], help="Example: !weapons")
    async def list_weapons(self,ctx):
        weaplist=Weapons()
        result=""
        print(weaplist.weapon_dictionary)
        for i in weaplist.weapon_dictionary.values():
           result=result+(await i.to_string())+"\n"
        result=separate_long_text(result)
        for i in result:
            await ctx.send(i)

    @commands.command(aliases=["weapon"], help="Example: !weapon mace")
    async def search_weapon(self,ctx,weapon):
        weaplist=Weapons()
        dict_entry=await weaplist.search(weapon)
        result=await dict_entry.to_string()
        await ctx.send(result)
