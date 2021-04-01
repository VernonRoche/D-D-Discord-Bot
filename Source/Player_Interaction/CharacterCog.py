import glob
from discord.ext import commands
from Source.Player_Information.Character import Character
from Source.Player_Information.Skills import calculate_passive_skills
from Source.Utility.Utilities import open_character
from Source.Utility.Utilities import separate_long_text
from Source.Utility.Utilities import save_char_file
import os
from Source.Utility.Messaging import *
from Source.Utility import Globals


class CharacterCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_valid(self, ctx, arg, name):
        tempspells = [f for f in glob.glob("../../Spells/" + "**/*.txt", recursive=True)]
        spells = ""
        for f in tempspells:
            f = f.lower()
            spells = spells + "," + f[7:-4]
        spells = spells[1:]

        tempclasses = [f for f in glob.glob("../../Character Classes/" + "**/*.txt", recursive=True)]
        classes = ""
        for f in tempclasses:
            f = f.lower()
            classes = classes + "," + f[18:-4]
        classes = classes[1:]

        if name == "hp" and arg <= 0:
            await ctx.send("``You donkey! You are not dead yet!``")
            raise ValueError("bad hp")
        if (name == "attribute" or name == "level") and (arg <= 0 or arg > 20):
            await ctx.send("``You master donkey! Put an attribute value between 0 and 20!``")
            raise ValueError("bad attr or level")
        if name == "coins" and arg < 0:
            await ctx.send("``Good news for you, you are not indebted, so get that negative money away from my eyes!``")
            raise ValueError("bad coins")
        if name == "initiative" and (arg < -10 or arg > 10):
            await ctx.send("``What is even this initiative value you donkey?!``")
            raise ValueError("bad init")
        if name == "skill" and (arg != "dnd" and
                                arg != "acrobatics" and arg != "athletics" and arg != "sleight of hand" and arg != "stealth" and
                                arg != "arcana" and arg != "history" and arg != "investigation" and arg != "nature" and
                                arg != "religion" and arg != "animal handling" and arg != "insight" and arg != "medicine" and
                                arg != "perception" and arg != "survival" and arg != "deception" and arg != "intimidation" and
                                arg != "performance" and arg != "persuasion"):
            await ctx.send("``Enter a correct skill name!``")
            raise ValueError("bad skillname")
        if name == "spell" and (arg not in spells) and arg != "dnd":
            await ctx.send("``This spell does not exist! If your spell has 2 or more words, separate them with -``")
            raise ValueError("bad spell")
        if name == "class" and (arg not in classes):
            await ctx.send("``This class does not exist!``")
            raise ValueError("bad class")

    @commands.command(aliases=["create character", "create"], help="Example: !create character or !create")
    async def char_creation(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        #Check if the command is called in the private discussion
        if not(is_private_channel(ctx)):
            await ctx.send("``Send this command in our little private chit chat ;)``")
            await private_DM(ctx,"Please execute this command here.")
            return

        # checks name and capitalizes all words of the name
        await send_cancelable_message(ctx,f"``Enter your character's name: ``")
        result = (await self.bot.wait_for("message", check=check)).content
        if Globals.is_cancel_requested:
            Globals.is_cancel_requested=False
            return
        if ' ' in result:
            name = ""
            result = result.split(' ')
            for i in result:
                i.capitalize()
                name = name + i + " "
            name = name[:-1]
        else:
            name = result.capitalize()

        # checks race and capitalizes everything
        await send_cancelable_message(ctx, f"``Enter your character's race: ``")
        result = (await self.bot.wait_for("message", check=check)).content
        if ' ' in result:
            race = ""
            result = result.split(' ')
            for i in result:
                i.capitalize()
                race = race + i + " "
            race = race[:-1]
        else:
            race = result.capitalize()

        # checks class and capitalizes everything
        await send_cancelable_message(ctx, f"``Enter your character's class: ``")
        while True:
            try:
                result = (await self.bot.wait_for("message", check=check)).content
                if ' ' in result:
                    myclass = ""
                    result = result.split(' ')
                    for i in result:
                        (i.lower()).capitalize()
                        myclass = myclass + i + " "
                    myclass = myclass[:-1]
                else:
                    myclass = (result.lower()).capitalize()
                await self.is_valid(ctx, myclass.lower(), "class")
                break
            except ValueError:
                await ctx.send("``Enter a correct class!``")

        # takes and checks level
        await send_cancelable_message(ctx, f"``Enter your starting level: ``")
        while True:
            try:
                level = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, level, "level")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        # takes and checks initiative
        await send_cancelable_message(ctx, f"``Enter your Initiative: ``")
        while True:
            try:
                initiative = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, initiative, "initiative")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        # takes and checks hp
        await send_cancelable_message(ctx, f"``Enter your starting hp: ``")
        while True:
            try:
                hp = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, hp, "hp")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        # takes and checks coins
        await send_cancelable_message(ctx, f"``Enter your starting coins: ``")
        while True:
            try:
                coin = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, coin, "coins")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        # checks attributes
        await send_cancelable_message(ctx, f"``Enter your strength: ``")
        while True:
            try:
                str = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, str, "attribute")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        await send_cancelable_message(ctx, f"``Enter your dexterity: ``")
        while True:
            try:
                dex = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, dex, "attribute")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        await send_cancelable_message(ctx, f"``Enter your constitution: ``")
        while True:
            try:
                con = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, con, "attribute")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        await send_cancelable_message(ctx, f"``Enter your intellect: ``")
        while True:
            try:
                intel = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, intel, "attribute")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        await send_cancelable_message(ctx, f"``Enter your wisdom: ``")
        while True:
            try:
                wis = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, wis, "attribute")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        await send_cancelable_message(ctx, f"``Enter your charisma: ``")
        while True:
            try:
                cha = int((await self.bot.wait_for("message", check=check)).content)
                await self.is_valid(ctx, cha, "attribute")
                break
            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")

        attributes = [str, dex, con, intel, wis, cha]
        proficiencies = []

        await send_cancelable_message(ctx, f"``Are you proficient with a skill?? When finished type dnd (Example: Acrobatics)``")
        while True:
            try:
                if proficiencies == []:
                    response = (await self.bot.wait_for("message", check=check)).content
                    await self.is_valid(ctx, response.lower(), "skill")
                    proficiencies = [response.capitalize()]
                while proficiencies[-1] != "Dnd":
                    await send_cancelable_message(ctx, f"``Are you proficient with another skill?? When finished type dnd (Example: Acrobatics)``")
                    response = (await self.bot.wait_for("message", check=check)).content
                    await self.is_valid(ctx, response.lower(), "skill")
                    if response.capitalize() in proficiencies:
                        None
                    else:
                        proficiencies.append(response.capitalize())
                del proficiencies[-1]
                break
            except ValueError:
                await ctx.send("``You must put a skillname!``")

        await send_cancelable_message(ctx, f"``Enter your weapons if you have any and it's quantity, you will be prompted again if you have another weapon. When finished type dnd (example: 2 Mace): ``")
        response = ((await self.bot.wait_for("message", check=check)).content).split(' ')
        if len(response) == 1 or response[0].isnumeric() == False:
            response.insert(0, "1")

        weapons = response[0] + " " + response[1].capitalize()
        while "Dnd" not in weapons:
            await send_cancelable_message(ctx, f"``Enter your weapons if you have any and it's quantity, you will be prompted again if you have another weapon. When finished type dnd (example: 2 Mace): ``")
            response = ((await self.bot.wait_for("message", check=check)).content).split(' ')
            if len(response) == 1 or response[0].isnumeric() == False:
                response.insert(0, "1")
            weapons = weapons + "," + response[0] + " " + response[1].capitalize()

        weapons = weapons.replace("1 Dnd", "")
        weapons = weapons[:-1]

        await send_cancelable_message(ctx, f"``Enter your items if you have any and it's quantity, you will be prompted again if you have another item. When finished type dnd (example: 5 Arrow): ``")
        response = ((await self.bot.wait_for("message", check=check)).content).split(' ')
        if len(response) == 1 or response[0].isnumeric() == False:
            response.insert(0, "1")

        items = response[0] + " " + response[1].capitalize()
        while "Dnd" not in items:
            await send_cancelable_message(ctx, f"``Enter your items if you have any and it's quantity, you will be prompted again if you have another item. When finished type dnd (example: 5 Arrow): ``")
            response = ((await self.bot.wait_for("message", check=check)).content).split(' ')
            if len(response) == 1 or response[0].isnumeric() == False:
                response.insert(0, "1")
            items = items + "," + response[0] + " " + response[1].capitalize()

        items = items.replace("1 Dnd", "")
        items = items[:-1]

        # Checks if spell is in file list, lowercases everything and capitalizes each separate word.
        await send_cancelable_message(ctx, f"``Do you know any spells? Yes/No``")
        response = (await self.bot.wait_for("message", check=check)).content
        listspells = []
        spells = ""
        if response.lower() == "no":
            None
        else:
            while True:
                try:
                    if listspells == []:
                        await send_cancelable_message(ctx, f"``Which spell do you know?? When finished type dnd (Example: Astral-Projection)``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        await self.is_valid(ctx, response.lower(), "spell")
                        if "-" not in response:
                            listspells.append((response.lower()).capitalize())
                        else:
                            response = response.split('-')
                            listspells.append("")
                            for i in response:
                                listspells[-1] = listspells[-1] + ((i.lower()).capitalize() + "-")
                            listspells[-1] = listspells[-1][:-1]

                    while "Dnd" not in listspells:
                        await send_cancelable_message(ctx, f"``Do you know any other spell?? When finished type dnd (Example: Aid)``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        await self.is_valid(ctx, response.lower(), "spell")
                        if response.lower() in listspells:
                            None
                        else:
                            if "-" not in response:
                                listspells.append((response.lower()).capitalize())
                            else:
                                response = response.split('-')
                                listspells.append("")
                                for i in response:
                                    listspells[-1] = listspells[-1] + (i.lower()).capitalize() + "-"
                                listspells[-1] = listspells[-1][:-1]

                    del listspells[-1]
                    break
                except ValueError:
                    await ctx.send("``You must put a spell!``")
            listspells = list(set(listspells))
            for i in listspells:
                spells = spells + i + ","
            spells = spells[:-1]
        """
        await ctx.send(f"``Do you have any feat? Yes/No")
        response = (await self.bot.wait_for("message", check=check)).content
        feats = ""
        if response == "No":
            None
        else:
            while True:
                try:
                    if feats == "":
                        await ctx.send(
                            f"``Which feat do you have?? When finished type dnd (Example: )``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        await self.is_valid(ctx, response.lower(), "feat")
                        spells = spells + "," + response.capitalize()
                    while "Dnd" not in spells:
                        await ctx.send(
                            f"``Do you know any other spell?? When finished type dnd (Example: Aid)``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        await self.is_valid(ctx, response.lower(), "feat")
                        if response.capitalize() in spells:
                            None
                        else:
                            spells = spells + "," + response.capitalize()
                    spells = spells[:-4]
                    break
                except ValueError:
                    await ctx.send("``You must put a feat!``")
        """
        feats = ""

        spellslots = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        await send_cancelable_message(ctx, f"``Can you cast Level 1+ spells? Yes/No``")
        response = (await self.bot.wait_for("message", check=check)).content
        if response.lower() == "no":
            None
        else:
            while True:
                try:
                    await send_cancelable_message(ctx, "``Enter the level and amount of slots (Levels are 1-9, max slots are 20). Example: 1 5 (5 Level 1 slots)``")
                    response = ((await self.bot.wait_for("message", check=check)).content).split(' ')
                    await self.is_valid(ctx, response[1], "attribute")
                    if response[0] >= 1 and response[0] <= 9:
                        spellslots[response[0] - 1] = response[1]
                    else:
                        await ctx.send("Enter a correct spell slot level!")
                        raise ValueError
                    break
                except ValueError:
                    await ctx.send("``You must put a number you donkey! Try again.``")

        char = Character(name, race, myclass, level, hp, coin, attributes, weapons, items, initiative, proficiencies,
                         spells, feats, spellslots)
        await char.save()
        await self.char_display(ctx, name)
        return

    @commands.command(aliases=["show character", "show"], help="Example: !show character Sauron or !show Sauron")
    async def char_display(self, ctx, character, *args):
        for ar in args:
            if ar != "":
                character = character + " " + ar
        filename = "../../Characters/" + character + ".txt"
        ftemp = open(filename, "r")
        file = ftemp.read()
        ftemp.close()
        result = f"```ml\n"
        file = file.split('$')
        passive_skills = calculate_passive_skills(character)

        # Name level, race and class
        result = result + "     '" + file[0] + "'     \n" + "🔰Level " + file[3] + " " + file[1] + " " + file[2] + "\n"

        # HP, Initiative and Coins
        result = result + "🩸Current HP: " + file[4] + "\n🔱Initiative: " + file[9] + "\n💰Current Coins: " + file[
            5] + "\n"

        # Attributes and passive skills to the right side
        attributes = file[6].split(',')
        result = result + "💥Strength: " + attributes[0] + "\n🎯Dexterity: " \
                 + attributes[1] + "\n💖Constitution: " + \
                 attributes[2] + "\n💫Intellect: " + attributes[
                     3] + "\n💡Wisdom: " + attributes[4] + "\n🎭Charisma: " + \
                 attributes[5] + "\n"
        # Proficiencies
        result = result + "🎲Proficiencies: " + file[10][:-1] + "\n" + "🔍Passive Investigation: " + str(
            passive_skills[1]) + "\n" + \
                 "🗣️Passive Insight: " + str(passive_skills[0]) + "\n" + \
                 "❗Passive Perception: " + str(passive_skills[0]) + "\n"

        # Weapons and Items
        result = result + "🏹Weapons: " + file[7] + "\n👜Items: " + file[8] + "\n"

        # Feats
        result = result + "🔰Feats: " + file[12] + "```"

        await ctx.send(result)

    @commands.command(aliases=["delete"], help="Example: !delete Gandalf")
    async def delete_character(self, ctx, character, *args):
        for ar in args:
            if ar != "":
                print(ar)
                character = character + " " + ar
        if os.path.exists("../../Characters/" + character + ".txt"):
            os.remove("../../Characters/" + character + ".txt")
            await ctx.send("``Good riddance``")
        else:
            await ctx.send("``This character does not exist``")

    @commands.command(aliases=["spellbook"], help="Example: !spellbook Ulric")
    async def spell_book(self, ctx, character, *args):
        file = open_character(character, *args)
        result = "```\n"
        result = result + file[11] + "\n"
        result = result + "Spell Slots: ["
        for i in file[13]:
            result=result+str(i)+", "
        result=result[:-2]+"]```\n"
        await ctx.send(result)

    @commands.command(aliases=["cast"], help="Example: !cast eldritch-blast Gandalf")
    async def cast_spell(self, ctx, spellname, character, *args):
        file = open_character(character, *args)
        file[11]=file[11].split(',')
        is_owned = map(lambda i: i.lower(), file[11])
        if spellname.lower() not in is_owned:
            await ctx.send("You do not have this spell!")
        else:
            slots = file[13]
            path = "../../Spells/" + spellname + ".txt"
            ftemp = open(path, "r")
            tfile = ftemp.read()
            ftemp.close()
            t2file = tfile.split('\n')
            level = t2file[1][-3]
            if level.isnumeric():
                level = int(level) -1
                if slots[level] == 0:
                    while level <= 8:
                        if slots[level] > 0:
                            slots[level] = slots[level]-1
                            break
                        level = level + 1
                else:
                    slots[level]= slots[level]-1
                if level == 9:
                    await ctx.send("You can't use any spell slot to cast this spell!")
                    return

            # values are good and spell can be shown
            file[13] = slots
            save_char_file(file)
            tfile = separate_long_text(tfile)
            for i in tfile:
                await ctx.send("```diff\n-" + i + "```")
