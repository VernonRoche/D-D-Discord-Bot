from discord.ext import commands

from Source.Utility import Globals
from Source.Utility.Messaging import *
from Source.Utility.Utilities import open_character_file, save_char_file, merge_name
from Source.Utility.ChecksAndHelp import should_exit_command, is_value_valid, is_coin_valid


class Bank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["money", "banker", "bank"], help="Example: !banker Gimli or !money Gimli")
    async def bank_management(self, ctx, character, *args):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        # Check if the command is called in the private discussion
        await redirect_to_private(ctx)
        character = merge_name(character, args)

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
                    if should_exit_command("!bank", response):
                        return
                    if response.lower() == "deposit":
                        await send_cancelable_message(ctx, f"``Enter the amount of coins you want to deposit``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!bank", response):
                            return
                        char_dictionary['coins'] = char_dictionary['coins'] + int(response)
                        save_char_file(char_dictionary)
                        await ctx.send("```💰Current Coins: " + str(coins) + "```")

                    else:
                        await send_cancelable_message(ctx, f"``Enter the amount of coins you want to withdraw``")
                        response = (await self.bot.wait_for("message", check=check)).content
                        if should_exit_command("!bank", response):
                            return
                        if not is_value_valid(char_dictionary['coins'] - int(response), "coins"):
                            await ctx.send("``This is way more than what you can afford!``")
                            raise ValueError
                        char_dictionary['coins'] = char_dictionary['coins'] - int(response)
                        save_char_file(char_dictionary)
                        await ctx.send("```💰Current Coins: " + str(coins) + "```")

                else:
                    break

            except ValueError:
                await ctx.send("``Put a correct value!``")

    @commands.command(aliases=["convert"], help="Example: !convert Aragorn")
    async def convert_coins(self, ctx, character, *args):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        # Check if the command is called in the private discussion
        await redirect_to_private(ctx)
        character = merge_name(character, args)

        char_dictionary = open_character_file(character)
        coins = char_dictionary['coins']
        await ctx.send("```💰Current Coins: " + str(coins) + "```")
        await ctx.send_cancelable_message(
            f"``Do you want to convert to a higher type of coin or lower? Type higher/lower``")
        response = (await self.bot.wait_for("message", check=check)).content
        if should_exit_command("!convert", response):
            return
        if response.lower() == "higher":
            await ctx.send_cancelable_message(
                f"``What type of coin do you want to create? Type silver/electrum/gold/platinum")
            response = (await self.bot.wait_for("message", check=check)).content
            if should_exit_command("!convert", response):
                return
            if not is_coin_valid(response):
                await ctx.send("``This type of coin does not exist``")
                return
            if response.lower() == "platinum":
                await ctx.send("You cannot convert platinum to a higher value coin")
                return
            # Get the quantity he wants to create
            await ctx.send_cancelable_message(
                f"``How many of them do you want to be converted from your treasury?")
            response = (await self.bot.wait_for("message", check=check)).content
            if should_exit_command("!convert", response) or int(response) < 0:
                return
            # TO BE IMPLEMENTED
            # Converts coins

        if response.lower() == "lower":
            await ctx.send_cancelable_message(
                f"``What type of coin do you want to create? Type silver/electrum/gold/platinum")
            response = (await self.bot.wait_for("message", check=check)).content
            if should_exit_command("!convert", response):
                return
            if not is_coin_valid(response):
                await ctx.send("``This type of coin does not exist``")
                return
            if response.lower() == "copper":
                await ctx.send("You cannot convert copper to a lower value coin")
                return
            # Get the quantity he wants to create
            await ctx.send_cancelable_message(
                f"``How many of them do you want to be converted from your treasury?")
            response = (await self.bot.wait_for("message", check=check)).content
            if should_exit_command("!convert", response) or int(response) < 0:
                return
            # TO BE IMPLEMENTED
            # Converts coins
        else:
            await ctx.send("Please enter a correct answer next time")
            return
