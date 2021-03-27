from discord.ext import commands
from Utilities import open_character, save_char_file


class Bag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["bag", "backpack"], help="Example: !bag Legolas or !backpack Legolas")
    async def bag_management(self, ctx, character, *args):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        for ar in args:
            if ar != "":
                character = character + " " + ar

        file = open_character(character)
        items = file[8]
        weapons = file[7]

        await ctx.send("```🏹Current Weapons: " + weapons + "```")
        await ctx.send("```👜Current Items: " + items + "```")

        await ctx.send(f"``Do you want to add or remove a weapon or item? Yes/No``")
        while True:
            try:
                response = (await self.bot.wait_for("message", check=check)).content
                if response.lower() == "yes":
                    await ctx.send(f"``Do you want to edit your weapons or items? Weapons/Items``")
                    response = (await self.bot.wait_for("message", check=check)).content

                    # weapons here
                    if response.lower() == "weapons":
                        await ctx.send(f"``Do you want to remove or add a weapon? Add/Remove``")
                        response = (await self.bot.wait_for("message", check=check)).content

                        # add weapon
                        if response.lower() == "add":
                            await ctx.send(f"``Enter the weapon you want to add``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            await ctx.send("In what quantity?")
                            quantity = int((await self.bot.wait_for("message", check=check)).content)
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
                                file[7] = result[1:]
                                save_char_file(file)
                                await ctx.send("```🏹CCurrent Weapons: " + weapons + "```")

                            else:
                                response = str(quantity) + " " + response.capitalize()
                                weapons = weapons + "," + response
                                file[7] = weapons
                                save_char_file(file)
                                await ctx.send("```🏹CCurrent Weapons: " + weapons + "```")

                        # remove weapon
                        elif response.lower() == "remove":
                            await ctx.send(f"``Enter the weapon you want to remove``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            await ctx.send("In what quantity?")
                            quantity = int((await self.bot.wait_for("message", check=check)).content)
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
                            file[7] = result[1:]
                            save_char_file(file)
                            await ctx.send("```🏹CCurrent Weapons: " + weapons + "```")
                        else:
                            raise ValueError("bad entry")

                    # items here
                    elif response.lower() == "items":
                        await ctx.send(f"``Do you want to remove or add an item? Add/Remove``")
                        response = (await self.bot.wait_for("message", check=check)).content

                        # add item
                        if response.lower() == "add":
                            await ctx.send(f"``Enter the item you want to add``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            await ctx.send("In what quantity?")
                            quantity = int((await self.bot.wait_for("message", check=check)).content)
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
                                file[8] = result[1:]
                                save_char_file(file)
                                await ctx.send("```👜Current Items: " + items + "```")

                            else:
                                response = str(quantity) + " " + response.capitalize()
                                items = items + "," + response
                                file[8] = items
                                save_char_file(file)
                                await ctx.send("```👜Current Items: " + items + "```")

                        # remove item
                        elif response.lower() == "remove":
                            await ctx.send(f"``Enter the item you want to remove``")
                            response = (await self.bot.wait_for("message", check=check)).content
                            await ctx.send("In what quantity?")
                            quantity = int((await self.bot.wait_for("message", check=check)).content)
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
                            file[8] = result[1:]
                            save_char_file(file)
                            await ctx.send("```👜Current Items: " + items + "```")
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
