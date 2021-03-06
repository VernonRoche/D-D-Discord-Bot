import glob
import random

from discord.ext import commands

import Token
from DiceCog import DiceRoller

from Player_Interaction.BagCog import Bag
from Player_Interaction.BankCog import Bank
from Player_Interaction.CharacterCog import CharacterCommands

from Source.Items_And_Actions.Weapon import WeaponCommands
from Source.Items_And_Actions.Armor import ArmorCommands

from Source.Utility import Globals
from Source.Utility.ChecksAndHelp import is_spell_valid
from Source.Utility.Globals import emojis
from Source.Utility.Utilities import separate_long_text
from Source.Utility.Utilities import this_is_some_alien_bababouy

from Source.Story.StoryCog import Story

bot = commands.Bot(command_prefix="!")

bot.add_cog(CharacterCommands(bot))
bot.add_cog(DiceRoller(bot))
bot.add_cog(Bank(bot))
bot.add_cog(Bag(bot))
bot.add_cog(WeaponCommands(bot))
bot.add_cog(ArmorCommands(bot))
bot.add_cog(Story(bot))

bot.remove_command('help')


# bot is ready
@bot.event
async def on_ready():
    try:
        print("Barbie-kun")
        print(bot.user.name)
        print(bot.user.id)
    except Exception as e:
        print(e)


@bot.command(name="test")
async def test(ctx):
    return True


# Check if we want to cancel a command
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "❌" and reaction.count > 1:
        Globals.is_cancel_requested = True


@bot.command(name="help")
async def help(ctx):
    bot_manual = separate_long_text(Globals.bot_manual)
    for i in bot_manual:
        await ctx.send(i)


@bot.command(name="bababouy")
async def bababouy(ctx):
    await this_is_some_alien_bababouy(ctx)


@bot.command(name="roshambo")
async def shifoumi(ctx, finger=False):
    Lp = [random.randint(1, 4), random.randint(1, 4)]
    Lshif = ["", ""]
    for i in range(0, 2):
        if Lp[i] == 1:
            Lshif[i] = emojis["HAND STONE"]
        elif Lp[i] == 2:
            Lshif[i] = emojis["HAND PAPER"]
        else:
            if finger:
                Lshif[i] = emojis["HAND MIDDLE FINGER"]
            else:
                Lshif[i] = emojis["HAND SCISSORS"]
    await ctx.send("```Player 1: " + Lshif[0] + "\nPlayer 2: " + Lshif[1] + "```")


@bot.command(aliases=["list"], help="Example: !characters")
async def list_characters(ctx):
    files = [f for f in glob.glob("../Characters/" + "*.json")]
    result = ""
    for f in files:
        result = result + "," + f[14:-5]
    result = result[1:]
    await ctx.send(f"```" + result + "```")


@bot.command(aliases=["spells"], help="Example: !spells")
async def list_spells(ctx):
    tempspells = [f for f in glob.glob("../Spells/" + "*.txt")]
    spells = ""
    for f in tempspells:
        spells = spells + ", " + f[10:-4]
    spells = spells[1:]
    spells = separate_long_text(spells)
    for i in spells:
        await ctx.send("```" + i + "```")


@bot.command(aliases=["spell"], help="Example: !spell eldritch-blast")
async def show_spell(ctx, spellname):
    if not is_spell_valid(spellname):
        await ctx.send("``This spell does not exist!``")
        return
    path = "../Spells/" + spellname + ".txt"
    ftemp = open(path, "r")
    file = ftemp.read()
    ftemp.close()
    file = separate_long_text(file)
    for i in file:
        await ctx.send("```" + i + "```")


@bot.command(aliases=["fuckyou"], help="DO NOT DO THIS!")
async def fuck_you(ctx):
    while (1):
        await ctx.send("FUCK YOUUU!")


# start bot
bot.run(Token.bot_token)
