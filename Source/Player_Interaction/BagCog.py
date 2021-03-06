from discord.ext import commands

from Source.Items_And_Actions.Weapon import Weapons
from Source.Utility.Globals import emojis
from Source.Utility.Messaging import *
from Source.Utility.Utilities import open_character_file, save_char_file, merge_name
from Source.Utility.ChecksAndHelp import should_exit_command, is_weapon_valid


class Bag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bag"], help="Example: !bag Legolas or !backpack Legolas")
    async def bag_management(self, ctx, character, *args):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        # Check if the command is called in the private discussion
        await redirect_to_private(ctx)

        character = merge_name(character, args)

        char_dictionary = open_character_file(character)
        items = char_dictionary['items']
        weapons = char_dictionary['weapons']

        await ctx.send("```"+emojis["BOW"]+"Current Weapons: " + weapons + "```")
        await ctx.send("```"+emojis["BAG"]+"Current Items: " + items + "```")

        await ctx.send(f"``Do you want to add or remove a weapon or item? Yes/No``")
        while True:
            try:
                response = (await self.bot.wait_for("message", check=check)).content
                if response.lower() == "yes":
                    await send_cancelable_message(ctx, f"``Do you want to edit your weapons or items? Weapons/Items``")
                    response = (await self.bot.wait_for("message", check=check)).content
                    if should_exit_command("!bag", response):
                        return

                    # weapons here
                    if response.lower() == "weapons":
                        await send_cancelable_message(ctx, f"``Do you want to remove or add a weapon? Add/Remove``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!bag", response):
                            return

                        # add weapon
                        if response.lower() == "add":
                            await send_cancelable_message(ctx, f"``Enter the weapon you want to add``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", response):
                                return
                            weapon_dictionary = Weapons().weapon_dictionary
                            if not is_weapon_valid(response, weapon_dictionary):
                                raise ValueError
                            await send_cancelable_message(ctx, "In what quantity?")
                            quantity = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", quantity):
                                return
                            quantity = int(quantity)
                            if quantity == 0:
                                return
                            if response.lower() in weapons.lower():
                                weapons = weapons.split(',')
                                for n, i in enumerate(weapons):
                                    if response.lower() in i.lower():
                                        old_quantity = int(i[:-len(i) + 1])
                                        i = i[1:]
                                        quantity += old_quantity
                                        weapons[n] = str(quantity) + i

                                result = ""
                                print(weapons)
                                for i in weapons:
                                    result = result + "," + i
                                    print(i)
                                char_dictionary['weapons'] = result[1:]
                                save_char_file(char_dictionary)
                                await ctx.send("```"+emojis["BOW"]+"Current Weapons: " + weapons + "```")

                            else:
                                response = str(quantity) + " " + (response.lower()).capitalize()
                                weapons = weapons + "," + response
                                char_dictionary['weapons'] = weapons
                                save_char_file(char_dictionary)
                                await ctx.send("```"+emojis["BOW"]+"Current Weapons: " + weapons + "```")

                        # remove weapon
                        elif response.lower() == "remove":
                            await send_cancelable_message(ctx, f"``Enter the weapon you want to remove``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", response):
                                return
                            await send_cancelable_message(ctx, "In what quantity?")
                            quantity = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", quantity):
                                return
                            quantity = int(quantity)
                            if quantity == 0:
                                return
                            if response.lower() in weapons.lower():
                                weapons = weapons.split(',')
                                for n, i in enumerate(weapons):
                                    if response.lower() in i.lower():
                                        old_quantity = int(i[:-len(i) + 1])
                                        i = i[1:]
                                        old_quantity -= quantity
                                        if old_quantity <= 0:
                                            weapons.remove(weapons[n])
                                        else:
                                            weapons[n] = str(quantity) + i
                            else:
                                await ctx.send("You do not have this weapon")
                                return
                            result = ""
                            for i in weapons:
                                result = result + "," + i
                            char_dictionary['weapons'] = result[1:]
                            save_char_file(char_dictionary)
                            await ctx.send("```"+emojis["BOW"]+"Current Weapons: " + weapons + "```")
                        else:
                            raise ValueError("bad entry")

                    # items here
                    elif response.lower() == "items":
                        await send_cancelable_message(ctx, f"``Do you want to remove or add an item? Add/Remove``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!bag", response):
                            return

                        # add item
                        if response.lower() == "add":
                            await send_cancelable_message(ctx, f"``Enter the item you want to add``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", response):
                                return
                            await send_cancelable_message(ctx, "In what quantity?")
                            quantity = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", quantity):
                                return
                            quantity = int(quantity)
                            if quantity == 0:
                                return
                            if response.lower() in items.lower():
                                items = items.split(',')
                                for n, i in enumerate(items):
                                    if response.lower() in i.lower():
                                        old_quantity = int(i[:-len(i) + 1])
                                        i = i[1:]
                                        quantity += old_quantity
                                        items[n] = str(quantity) + i
                                result = ""
                                for i in items:
                                    result = result + "," + i
                                char_dictionary['items'] = result[1:]
                                save_char_file(char_dictionary)
                                await ctx.send("```"+emojis["BAG"]+"Current Items: " + items + "```")

                            else:
                                response = str(quantity) + " " + (response.lower()).capitalize()
                                items = items + "," + response
                                char_dictionary['items'] = items
                                save_char_file(char_dictionary)
                                await ctx.send("```"+emojis["BAG"]+"Current Items: " + items + "```")

                        # remove item
                        elif response.lower() == "remove":
                            await send_cancelable_message(ctx, f"``Enter the item you want to remove``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", response):
                                return
                            await send_cancelable_message(ctx, "In what quantity?")
                            quantity = (await self.bot.wait_for("message", check=check)).content
                            if should_exit_command("!bag", quantity):
                                return
                            quantity = int(quantity)
                            if quantity == 0:
                                return
                            if response.lower() in items.lower():
                                items = items.split(',')
                                for n, i in enumerate(items):
                                    if response.lower() in i.lower():
                                        old_quantity = int(i[:-len(i) + 1])
                                        i = i[1:]
                                        old_quantity -= quantity
                                        if old_quantity <= 0:
                                            items.remove(items[n])
                                        else:
                                            items[n] = str(quantity) + i
                            else:
                                await ctx.send("You do not have this item")
                                return
                            result = ""
                            for i in items:
                                result = result + "," + i
                            char_dictionary['items'] = result[1:]
                            save_char_file(char_dictionary)
                            await ctx.send("```"+emojis["BAG"]+"Current Items: " + items + "```")
                        else:
                            raise ValueError("bad entry")
                    else:
                        raise ValueError("bad entry")


                # no changes
                else:
                    break

            except ValueError:
                await ctx.send(
                    "``Something went wrong with your input! Are you sure you wrote one of the parameters asked?``")

    @commands.command(aliases=["equip_armor", "manage_armor", "equip"], help="Example: !equip_armor Gimli or !equip "
                                                                             "Gimli")
    async def bag_armor_equip(self, ctx, character, *args):
        pass
