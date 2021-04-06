from discord.ext import commands

from Source.Utility import Globals
from Source.Utility.Messaging import *
from Source.Utility.Utilities import open_character_file, save_char_file
from Source.Utility.ChecksAndHelp import is_command_rerun_requested


class Bank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_valid(self, ctx, arg, name):
        if name == "coins" and arg < 0:
            await ctx.send("``You can't afford this you pleb! You try to buy something too expensive!``")
            raise ValueError("bad coins")

    @commands.command(aliases=["money", "banker", "bank"], help="Example: !banker Gimli or !money Gimli")
    async def bank_management(self, ctx, character, *args):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        # Check if the command is called in the private discussion
        if not (is_private_channel(ctx)):
            await ctx.send("``Send this command in our little private chit chat ;)``")
            await private_DM(ctx, "Please execute this command here.")
            return
        for ar in args:
            if ar != "":
                character = character + " " + ar

        char_dictionary = open_character_file(character)
        coins = char_dictionary['coins']
        await ctx.send("```💰Current Coins: " + str(coins) + "```")

        await ctx.send(f"``Do you want to deposit or withdraw coins? Yes/No``")
        while True:
            try:
                response = (await self.bot.wait_for("message", check=check)).content
                if response.lower() == "yes":
                    await send_cancelable_message(ctx,
                                                  f"``What change in your coins do you wish to make? Deposit/Withdraw``")
                    response = (await self.bot.wait_for("message", check=check)).content
                    if is_command_rerun_requested("!bank", response):
                        return
                    if Globals.is_cancel_requested:
                        Globals.is_cancel_requested = False
                        return
                    if response.lower() == "deposit":
                        await send_cancelable_message(ctx, f"``Enter the amount of coins you want to deposit``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if is_command_rerun_requested("!bank", response):
                            return
                        if Globals.is_cancel_requested:
                            Globals.is_cancel_requested = False
                            return
                        char_dictionary['coins'] = char_dictionary['coins'] + int(response)
                        save_char_file(char_dictionary)
                        await ctx.send("```💰Current Coins: " + str(coins) + "```")

                    else:
                        await send_cancelable_message(ctx, f"``Enter the amount of coins you want to withdraw``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if is_command_rerun_requested("!bank", response):
                            return
                        if Globals.is_cancel_requested:
                            Globals.is_cancel_requested = False
                            return
                        char_dictionary['coins'] = char_dictionary['coins'] - int(response)
                        await self.is_valid(ctx, char_dictionary['coins'], "coins")
                        save_char_file(char_dictionary)
                        await ctx.send("```💰Current Coins: " + str(coins) + "```")

                else:
                    break

            except ValueError:
                await ctx.send("``You must put a number you donkey! Try again.``")
