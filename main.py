from discord.ext import commands
from CharacterCog import CharacterCommands
from DiceCog import DiceRoller
from BankCog import Bank
from BagCog import Bag
from Weapon import WeaponCommands
from Messaging import *

import random

import glob

from Utilities import this_is_some_alien_bababouy
from Utilities import separate_long_text

bot = commands.Bot(command_prefix="!")

bot.add_cog(CharacterCommands(bot))
bot.add_cog(DiceRoller(bot))
bot.add_cog(Bank(bot))
bot.add_cog(Bag(bot))
bot.add_cog(WeaponCommands(bot))

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


@bot.event
async def on_reaction_add(reaction,user):
    if reaction.emoji=="❌" and reaction.count>1:
        print("VALHALLA")


@bot.command(name="help")
async def help(ctx):
    await ctx.send("```This is a list of possible commands:\n"
                   "!help  (Bring up this message)\n"
                   "!create  (Create a character)\n"
                   "!delete <character>  (Deletes a character)\n"
                   "!list  (List all created characters)\n"
                   "!show <character>  (Shows the character's sheet)\n"
                   "!dice <amount>d<sides> <modifier>  (Throws the given amount of dices, with specific sides. Modifier parameter is optional. Example: 3d6)\n"
                   "!dice  (Throws 1d20)\n"
                   "!init <character> or !initiative <character> (Rolls an initiative roll for the given character)\n"
                   "!roll <skill> <character>  (Rolls 1d20 for a specific skill with the given character)\n"
                   "!bag <character>  (Opens up the bag management tab for the character)\n"
                   "!bank <character> or !money <character> (Opens up the bank)\n"
                   "!spells  (Lists all available spells)\n"
                   "!spellbook <character>  (Shows all the spells the character knows)\n"
                   "!spell <name of spell>  (Shows information on the asked spell)\n"
                   "!cast <spell> <character>  (Casts a given spell for the specific character. He must know it and have enough spell slots)\n"
                   "!bababouy  (Vibe check)```")


@bot.command(name="bababouy")
async def bababouy(ctx):
    await this_is_some_alien_bababouy(ctx)


@bot.command(name="roshambo")
async def shifoumi(ctx, finger=False):
    Lp = [random.randint(1, 4), random.randint(1, 4)]
    Lshif = ["",""]
    for i in range(0, 2):
        if Lp[i] == 1:
            Lshif[i] = "✊"
        elif Lp[i] == 2:
            Lshif[i] = "✋"
        else:
            if finger:
                Lshif[i] = "🖕"
            else:
                Lshif[i] = "✌️"
    await ctx.send("```Player 1: " + Lshif[0] + "\nPlayer 2: " + Lshif[1] + "```")


@bot.command(aliases=["list"], help="Example: !characters")
async def list_characters(ctx):
    files = [f for f in glob.glob("Characters/" + "**/*.txt", recursive=True)]
    result = ""
    for f in files:
        result = result + "," + f[11:-4]
    result = result[1:]
    await ctx.send(f"```" + result + "```")


@bot.command(aliases=["spells"], help="Example: !spells")
async def list_spells(ctx):
    tempspells = [f for f in glob.glob("Spells/" + "**/*.txt", recursive=True)]
    spells = ""
    for f in tempspells:
        spells = spells + "," + f[7:-4]
    spells = spells[1:]
    spells = separate_long_text(spells)
    for i in spells:
        await ctx.send("```" + i + "```")


@bot.command(aliases=["spell"], help="Example: !spell eldritch-blast")
async def show_spell(ctx, spellname):
    path = "Spells/" + spellname + ".txt"
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
bot.run("NzY2NjQyMjU3NDczNDM3NzE2.X4mVPQ.KtnqUWBlSGKan2VcR5Y4TJiMe2k")
