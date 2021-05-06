import difflib

from discord.ext import commands

from Source.Utility.Utilities import separate_long_text

light_armors = ["Padded", "Leather", "Studded Leather"]

medium_armors = ["Hide", "Chain Shirt", "Scale Mail", "Breastplate", "Half Plate"]

heavy_armors = ["Ring Mail", "Chain Mail", "Splint", "Plate"]


class Armor:
    def __init__(self, name, cost, armor_class, weight, minimum_strength, stealth_disadvantage):
        self.name = name
        self.cost = cost
        self.armor_class = armor_class
        self.weight = weight
        self.minimum_strength = minimum_strength
        self.stealth_disadvantage = stealth_disadvantage

    async def to_string(self):
        ret_string = f'''```diff
- {self.name} -
{self.armor_class}
Stealth Disadvantage: {self.stealth_disadvantage}
{self.minimum_strength}
{self.weight}, {self.cost}```'''

        if self.minimum_strength == " ":
            ret_string = f'''```diff
- {self.name} -
{self.armor_class}
Stealth Disadvantage: {self.stealth_disadvantage}
{self.weight}, {self.cost}```'''

        return ret_string


class Armors:
    def __init__(self):
        self.armor_dictionary = {}

        self.populate_dictionary()

    def populate_dictionary(self):
        # Light armors
        padded = Armor("Padded", "5gp", "11", "8 lb", " ", "Yes")
        self.armor_dictionary[padded.name] = padded
        leather = Armor("Leather", "10gp", "11", "10 lb", " ", "No")
        self.armor_dictionary[leather.name] = leather
        studded_leather = Armor("Studded Leather", "45gp", "12", "13 lb", " ", "No")
        self.armor_dictionary[studded_leather.name] = studded_leather

        # Medium armors
        hide = Armor("Hide", "10gp", "12", "12 lb", " ", "No")
        self.armor_dictionary[hide.name] = hide
        chain_shirt = Armor("Chain Shirt", "50gp", "13", "20 lb", " ", "No")
        self.armor_dictionary[chain_shirt.name] = chain_shirt
        scale_mail = Armor("Scale Mail", "50gp", "14", "45 lb", " ", "Yes")
        self.armor_dictionary[scale_mail.name] = scale_mail
        breastplate = Armor("Breastplate", "400gp", "14", "20 lb", " ", "No")
        self.armor_dictionary[breastplate.name] = breastplate
        half_plate = Armor("Half Plate", "750gp", "15", "40 lb", " ", "Yes")
        self.armor_dictionary[half_plate.name] = half_plate

        # Heavy armors
        ring_mail = Armor("Ring Mail", "30gp", "14", "40 lb", " ", "Yes")
        self.armor_dictionary[ring_mail.name] = ring_mail
        chain_mail = Armor("Chain Mail", "75gp", "16", "55 lb", "13", "Yes")
        self.armor_dictionary[chain_mail.name] = chain_mail
        splint = Armor("Splint", "200gp", "17", "60 lb", "15", "Yes")
        self.armor_dictionary[splint.name] = splint
        plate = Armor("Plate", "1500gp", "18", "65 lb", "18", "Yes")
        self.armor_dictionary[plate.name] = plate

        # Shield
        shield = Armor("Shield", "10gp", "2", "6 lb", " ", "No")
        self.armor_dictionary[shield.name] = shield

    async def search(self, search):
        close_matches = difflib.get_close_matches(search, list(self.armor_dictionary.keys()))

        if len(close_matches) == 0:
            return False

        return self.armor_dictionary[close_matches[0]]


class ArmorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["weapons"], help="Example: !weapons")
    async def list_weapons(self, ctx):
        armorlist = Armors().armor_dictionary
        result = ""
        for i in armorlist.values():
            result = result + (await i.to_string()) + "\n"
        result = separate_long_text(result, True)
        for i in result:
            await ctx.send(i)

    @commands.command(aliases=["weapon"], help="Example: !weapon mace")
    async def search_weapon(self, ctx, weapon):
        armorlist = Armors()
        dict_entry = await armorlist.search(weapon)
        result = await dict_entry.to_string()
        await ctx.send(result)
