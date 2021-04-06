import os

from discord.ext import commands

from Source.Player_Information.Skills import calculate_passive_skills
from Source.Utility.ChecksAndHelp import *
from Source.Utility.Messaging import *
from Source.Utility.Utilities import open_character_file
from Source.Utility.Utilities import populate_character_dictionary
from Source.Utility.Utilities import save_char_file
from Source.Utility.Utilities import separate_long_text


class CharacterCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["create character", "create"], help="Example: !create character or !create")
    async def char_creation(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        # Check if the command is called in the private discussion
        if not (is_private_channel(ctx)):
            await ctx.send("``Send this command in our little private chit chat ;)``")
            await private_DM(ctx, "Please execute this command here.")
            return
        """
        # checks name and capitalizes all words of the name
        await send_cancelable_message(ctx, f"``Enter your character's name: ``")
        response = (await self.bot.wait_for("message", check=check)).content
        if should_exit_command("!create", response):
            return
        if ' ' in response:
            name = ""
            response = response.split(' ')
            for i in response:
                i = (i.lower()).capitalize()
                name = name + i + " "
            name = name[:-1]
        else:
            name = (response.lower()).capitalize()

        # checks race and capitalizes everything
        while True:
            try:
                await send_cancelable_message(ctx, f"``Enter your character's race: ``")
                response = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", response):
                    return
                if ' ' in response:
                    race = ""
                    response = response.split(' ')
                    for i in response:
                        i = (i.lower()).capitalize()
                        race = race + i + " "
                    race = race[:-1]
                else:
                    race = (response.lower()).capitalize()
                if is_race_valid(race):
                    break
                raise ValueError
            except ValueError:
                await send_cancelable_message(ctx, "``Enter a correct race!``")

        # checks class and capitalizes everything
        await send_cancelable_message(ctx, f"``Enter your character's class: ``")
        while True:
            try:
                response = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", response):
                    return
                if ' ' in response:
                    myclass = ""
                    response = response.split(' ')
                    for i in response:
                        i = (i.lower()).capitalize()
                        myclass = myclass + i + " "
                    myclass = myclass[:-1]
                else:
                    myclass = (response.lower()).capitalize()
                if is_class_valid(myclass):
                    break
                raise ValueError
            except ValueError:
                await send_cancelable_message(ctx, "``Enter a correct class!``")

        # takes and checks level
        await send_cancelable_message(ctx, f"``Enter your starting level: ``")
        while True:
            try:
                level = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", level):
                    return
                level = int(level)
                if not is_value_valid(level, "level"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct level!``")

        # takes and checks initiative
        await send_cancelable_message(ctx, f"``Enter your Initiative: ``")
        while True:
            try:
                initiative = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", initiative):
                    return
                initiative = int(initiative)
                if not is_value_valid(initiative, "initiative"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct initiative!``")

        # takes and checks hp
        await send_cancelable_message(ctx, f"``Enter your starting hp: ``")
        while True:
            try:
                hp = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", hp):
                    return
                hp = int(hp)
                if not is_value_valid(hp, "hp"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct HP value!``")

        # takes and checks coins
        await send_cancelable_message(ctx, f"``Enter your starting coins: ``")
        while True:
            try:
                coin = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", coin):
                    return
                coin = int(coin)
                if not is_value_valid(coin, "coins"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put some correct coin amount!``")

        # checks attributes
        await send_cancelable_message(ctx, f"``Enter your strength: ``")
        while True:
            try:
                str = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", str):
                    return
                str = int(str)
                if not is_value_valid(str, "attribute"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct value!``")

        await send_cancelable_message(ctx, f"``Enter your dexterity: ``")
        while True:
            try:
                dex = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", dex):
                    return
                dex = int(dex)
                if not is_value_valid(dex, "attribute"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct value!``")

        await send_cancelable_message(ctx, f"``Enter your constitution: ``")
        while True:
            try:
                con = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", con):
                    return
                con = int(con)
                if not is_value_valid(con, "attribute"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct value!``")

        await send_cancelable_message(ctx, f"``Enter your intelligence: ``")
        while True:
            try:
                intel = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", intel):
                    return
                intel = int(intel)
                if not is_value_valid(intel, "attribute"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct value!``")

        await send_cancelable_message(ctx, f"``Enter your wisdom: ``")
        while True:
            try:
                wis = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", wis):
                    return
                wis = int(wis)
                if not is_value_valid(wis, "attribute"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct value!``")

        await send_cancelable_message(ctx, f"``Enter your charisma: ``")
        while True:
            try:
                cha = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", cha):
                    return
                cha = int(cha)
                if not is_value_valid(cha, "attribute"):
                    raise ValueError
                break
            except ValueError:
                await ctx.send("``Put a correct value!``")

        attributes = [str, dex, con, intel, wis, cha]
        proficiencies = []

        await send_cancelable_message(ctx,
                                      f"``Are you proficient with a skill?? When finished type dnd (Example: Acrobatics)``")
        while True:
            try:
                if proficiencies == []:
                    response = (await self.bot.wait_for("message", check=check)).content
                    if should_exit_command("!create", response):
                        return
                    if not is_value_valid(response.lower(), "skill"):
                        raise ValueError
                    proficiencies = [(response.lower()).capitalize()]
                while proficiencies[-1] != "Dnd":
                    await send_cancelable_message(ctx,
                                                  f"``Are you proficient with another skill?? When finished type dnd (Example: Acrobatics)``")
                    response = (await self.bot.wait_for("message", check=check)).content
                    if should_exit_command("!create", response):
                        return
                    if not is_value_valid(response.lower(), "skill"):
                        raise ValueError
                    if (response.lower()).capitalize() in proficiencies:
                        None
                    else:
                        proficiencies.append((response.lower()).capitalize())
                del proficiencies[-1]
                break
            except ValueError:
                await ctx.send("``You must put a correct skillname!``")
        """
        weapons = ""
        weapon_dictionary = Weapons().weapon_dictionary
        while True:
            try:
                await send_cancelable_message(ctx,
                                              f"``Enter your weapons if you have any and it's quantity, "
                                              f"you will be prompted again if you have another weapon. "
                                              f"When finished type dnd (example: 2 Mace): ``")
                response = (await self.bot.wait_for("message", check=check)).content
                if should_exit_command("!create", response):
                    return

                index = 0
                quantity_index = []
                quantity = 0
                if not response[0].isnumeric():
                    response = "1 " + response
                while response[index].isnumeric():
                    quantity_index.append(int(response[index]))
                    index += 1

                response = response[index + 1:]
                for x in quantity_index:
                    quantity = quantity + x * (10 ** (index - 1))
                    index -= 1

                print(response)
                if not is_weapon_valid(response, weapon_dictionary):
                    raise ValueError

                weapons = str(quantity) + " " + (response.lower()).capitalize()

                while "Dnd" not in weapons:
                    await send_cancelable_message(ctx,
                                                  f"``Enter your weapons if you have any and it's quantity, you will be prompted again if you have another weapon. When finished type dnd (example: 2 Mace): ``")
                    response = (await self.bot.wait_for("message", check=check)).content
                    if should_exit_command("!create", response):
                        return

                    index = 0
                    quantity_index = []
                    quantity = 0

                    if not response[0].isnumeric():
                        response = "1 " + response

                    while response[index].isnumeric():
                        quantity_index.append(int(response[index]))
                        index += 1

                    response = response[index + 1:]
                    for x in quantity_index:
                        quantity = quantity + x * (10 ** (index - 1))
                        index -= 1

                    print(response)
                    if not is_weapon_valid(response, weapon_dictionary):
                        raise ValueError

                    if (response.lower()).capitalize() in weapons:
                        pivot_char = weapons.find(
                            (response.lower()).capitalize())  # pivot_char einai to m apo to "326 mace"
                        last_int = pivot_char - 2 # last_int to prwto int pou sunandame to 6 apo to "3256 mace"
                        shift_char = []  # shift_char ta psifia pou theloyume na alla3oume
                        old_quantity = int(response[0])

                        temp_index = 1
                        if last_int == 0:
                            None
                        else:
                            search_int = weapons[pivot_char - 2 - temp_index]  # search_int 3ekiname me afto na
                                                                               # phgainoume pros ta pisw sto string
                            while search_int.isnumeric():
                                shift_char.append(weapons[search_int])
                                temp_index += 1
                                if pivot_char - 2 -temp_index <0:
                                    break
                                search_int = weapons[pivot_char - 2 - temp_index]
                        shift_char.reverse()

                        index=len(shift_char)
                        for x in quantity_index:
                            old_quantity = old_quantity + x * (10 ** (index-1))
                            index -= 1
                        quantity=quantity+old_quantity

                        weapons = weapons[:pivot_char - 2 - temp_index] + str(quantity) + weapons[pivot_char:]

                    else:
                        weapons = weapons + "," + str(quantity) + " " + (response.lower()).capitalize()

                weapons = weapons.replace("1 Dnd", "")
                weapons = weapons[:-1]
                print(weapons)
                break
            except ValueError:
                await ctx.send("``You must enter a correct weapon!``")

        await send_cancelable_message(ctx,
                                      f"``Enter your items if you have any and it's quantity, you will be prompted again if you have another item. When finished type dnd (example: 5 Arrow): ``")
        response = (await self.bot.wait_for("message", check=check)).content
        if should_exit_command("!create", response):
            return
        response = response.split(' ')
        if len(response) == 1 or response[0].isnumeric() == False:
            response.insert(0, "1")

        items = response[0] + " " + (response[1].lower()).capitalize()
        while "Dnd" not in items:
            await send_cancelable_message(ctx,
                                          f"``Enter your items if you have any and it's quantity, you will be prompted again if you have another item. When finished type dnd (example: 5 Arrow): ``")
            response = (await self.bot.wait_for("message", check=check)).content
            if should_exit_command("!create", response):
                return
            response = response.split(' ')
            if len(response) == 1 or response[0].isnumeric() == False:
                response.insert(0, "1")
            items = items + "," + response[0] + " " + (response[1].lower()).capitalize()

        items = items.replace("1 Dnd", "")
        items = items[:-1]

        # Checks if spell is in char_dictionary list, lowercases everything and capitalizes each separate word.
        await send_cancelable_message(ctx, f"``Do you know any spells? Yes/No``")
        response = (await self.bot.wait_for("message", check=check)).content
        if should_exit_command("!create", response):
            return
        listspells = []
        spells = ""
        if response.lower() == "no":
            None
        else:
            while True:
                try:
                    if listspells == []:
                        await send_cancelable_message(ctx,
                                                      f"``Which spell do you know?? When finished type dnd (Example: Astral-Projection)``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!create", response):
                            return
                        if not is_spell_valid(response):
                            raise ValueError
                        if "-" not in response:
                            listspells.append((response.lower()).capitalize())
                        else:
                            response = response.split('-')
                            listspells.append("")
                            for i in response:
                                listspells[-1] = listspells[-1] + ((i.lower()).capitalize() + "-")
                            listspells[-1] = listspells[-1][:-1]

                    while "Dnd" not in listspells:
                        await send_cancelable_message(ctx,
                                                      f"``Do you know any other spell?? When finished type dnd (Example: Aid)``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!create", response):
                            return
                        if not is_spell_valid(response):
                            raise ValueError
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
                    await ctx.send("``You must put a correct spell!``")
            listspells = list(set(listspells))
            for i in listspells:
                spells = spells + i + ","
            spells = spells[:-1]

        await send_cancelable_message(ctx, f"``Do you have any feat? Yes/No``")
        response = (await self.bot.wait_for("message", check=check)).content
        if should_exit_command("!create", response):
            return
        feats = ""
        if response.lower() == "no":
            None
        else:
            while True:
                try:
                    if feats == "":
                        await send_cancelable_message(ctx,
                                                      f"``Which feat do you have?? When finished type dnd (Example: Polearm Master)``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!create", response):
                            return
                        if not is_feat_valid(response):
                            raise ValueError
                        feats = feats + "," + (response.lower()).capitalize()
                    while "Dnd" not in feats:
                        await send_cancelable_message(ctx,
                                                      f"``Do you know any other feat?? When finished type dnd (Example: War Caster)``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!create", response):
                            return
                        if not is_feat_valid(response):
                            raise ValueError
                        if (response.lower()).capitalize() in feats:
                            None
                        else:
                            feats = feats + "," + (response.lower()).capitalize()
                    feats = feats[1:-4]
                    break
                except ValueError:
                    await ctx.send("``You must put a correct feat!``")

        spellslots = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        await send_cancelable_message(ctx, f"``Can you cast Level 1+ spells? Yes/No``")
        response = (await self.bot.wait_for("message", check=check)).content
        if should_exit_command("!create", response):
            return
        if response.lower() == "no":
            None
        else:
            while True:
                try:
                    await send_cancelable_message(ctx,
                                                  "``Enter the level and amount of slots (Levels are 1-9, max slots are 20). Example: 1 5 (5 Level 1 slots). When finished type dnd``")
                    response = (await self.bot.wait_for("message", check=check)).content
                    if should_exit_command("!create", response):
                        return
                    if response.lower() == "dnd":
                        break
                    response = response.split(' ')
                    response = [int(x) for x in response]
                    if not is_value_valid(response[1], "spellslot"):
                        raise ValueError
                    if response[0] >= 1 and response[0] <= 9:
                        spellslots[response[0] - 1] = response[1]
                    else:
                        await ctx.send("Enter a correct spell slot level!")
                        raise ValueError

                except ValueError:
                    await ctx.send("``Put a correct value!``")

        save_char_file(
            populate_character_dictionary(name, race, myclass, level, hp, coin, attributes, weapons, items, initiative,
                                          proficiencies, spells, feats, spellslots))
        await self.char_display(ctx, name)
        return

    @commands.command(aliases=["show character", "show"], help="Example: !show character Sauron or !show Sauron")
    async def char_display(self, ctx, character, *args):
        for ar in args:
            if ar != "":
                character = character + " " + ar
        char_dictionary = open_character_file(character)
        result = f"```ml\n"
        passive_skills = calculate_passive_skills(character)

        # Name level, race and class
        result = result + "     '" + char_dictionary['name'] + "'     \n" + "🔰Level " + str(char_dictionary['level']) \
                 + " " + char_dictionary['race'] + " " + char_dictionary['class'] + "\n"

        # HP, Initiative and Coins
        result = result + "🩸Current HP: " + str(char_dictionary['hp']) + "\n🔱Initiative: " \
                 + str(char_dictionary['initiative']) + "\n💰Current Coins: " \
                 + str(char_dictionary['coins']) + "\n"

        # Attributes and passive skills to the right side
        attributes = char_dictionary['attributes']
        result = result + "💥Strength: " + str(attributes['strength']) + "\n🎯Dexterity: " \
                 + str(attributes['dexterity']) + "\n💖Constitution: " + \
                 str(attributes['constitution']) + "\n💫Intelligence: " + str(attributes[
                                                                                  'intelligence']) + "\n💡Wisdom: " + str(
            attributes['wisdom']) + "\n🎭Charisma: " + \
                 str(attributes['charisma']) + "\n"
        # Proficiencies
        result = result + "🎲Proficiencies: " + char_dictionary['proficiencies'][
                                                :-1] + "\n" + "🔍Passive Investigation: " + str(
            passive_skills[1]) + "\n" + \
                 "🗣️Passive Insight: " + str(passive_skills[0]) + "\n" + \
                 "❗Passive Perception: " + str(passive_skills[0]) + "\n"

        # Weapons and Items
        result = result + "🏹Weapons: " + char_dictionary['weapons'] + "\n👜Items: " + char_dictionary['items'] + "\n"

        # Feats
        result = result + "🔰Feats: " + char_dictionary['feats'] + "```"

        await ctx.send(result)

    @commands.command(aliases=["delete"], help="Example: !delete Gandalf")
    async def delete_character(self, ctx, character, *args):
        for ar in args:
            if ar != "":
                character = character + " " + ar
        if os.path.exists("../Characters/" + character + ".json"):
            os.remove("../Characters/" + character + ".json")
            await ctx.send("``Good riddance``")
        else:
            await ctx.send("``This character does not exist``")

    @commands.command(aliases=["spellbook"], help="Example: !spellbook Ulric")
    async def spell_book(self, ctx, character, *args):
        char_dictionary = open_character_file(character, *args)
        result = "```\n"
        result = result + char_dictionary['spells'] + "\n"
        result = result + "Spell Slots: ["
        for i in char_dictionary['spellslots']:
            result = result + str(i) + ", "
        result = result[:-2] + "]```\n"
        await ctx.send(result)

    @commands.command(aliases=["cast"], help="Example: !cast eldritch-blast Gandalf")
    async def cast_spell(self, ctx, spellname, character, *args):
        char_dictionary = open_character_file(character, *args)
        char_dictionary['spells'] = char_dictionary['spells'].split(',')
        is_owned = map(lambda i: i.lower(), char_dictionary['spells'])
        if spellname.lower() not in is_owned:
            await ctx.send("You do not have this spell!")
        else:
            slots = char_dictionary['spellslots']
            path = "../Spells/" + spellname + ".txt"
            ftemp = open(path, "r")
            tfile = ftemp.read()
            ftemp.close()
            t2file = tfile.split('\n')
            level = t2file[1][-3]
            if level.isnumeric():
                level = int(level) - 1
                if slots[level] == 0:
                    while level <= 8:
                        if slots[level] > 0:
                            slots[level] = slots[level] - 1
                            break
                        level = level + 1
                else:
                    slots[level] = slots[level] - 1
                if level == 9:
                    await ctx.send("You can't use any spell slot to cast this spell!")
                    return

            # values are good and spell can be shown
            char_dictionary['spellslots'] = slots
            save_char_file(char_dictionary)
            tfile = separate_long_text(tfile)
            for i in tfile:
                await ctx.send("```diff\n-" + i + "```")
