import random
from discord.ext import commands
from Source.Utility.Utilities import open_character
from Player_Information.Skills import skill_modifier
from Source.Utility.Utilities import separate_long_text


class DiceRoller(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Roll a dice
    @commands.command(aliases=["dice"],
                      help="Example: !dice 2d6. If you want to add a modifier use instead !dice 2d6 3. Default is 1d20.")
    async def dice_roll(self, ctx, dice="1d20", modifier=0):
        dice = dice.split('d')
        times = int(dice[0])
        roll = int(dice[1])

        if times <= 0 or roll <= 0:
            await ctx.send("``You creative muppet....check again your dice and enter a correct value!``")
            return
        i = 0
        L = "🎲["
        while i < times:
            i += 1
            outcome = random.randint(1, roll)
            if outcome == roll:
                L = L + "Critical!, "

            elif outcome == 1:
                L = L + "Critical Failure!, "
            else:
                outcome = outcome + modifier
                L = L + str(outcome) + ", "
        L = L[:-2] + "]🎲"

        # checks if length is supported for one Discord message. If not, it recursively splits the string by blocks of 1900 chars.
        if len(L) <= 1900:
            L = "```" + L + "```"
            await ctx.send(L)
        else:
            result = separate_long_text(L)
            for i in result:
                i = "```" + i + "```"
                await ctx.send(i)

    @commands.command(aliases=["initiative", "init"],
                      help="Example: !roll initiative Gandalf or !initiative Gandalf or !init Gandalf")
    async def initiative_roll(self, ctx, character, *args):
        for ar in args:
            if ar != "":
                character = character + " " + ar

        file = open_character(character)
        await self.dice_roll(ctx, 1, 20, file[9])

    @commands.command(aliases=["roll"],
                      help="Example: !roll Perception Sauron or !roll skill stealth Gandalf")
    # takes a skill roll. character is first word of name and the optname parameters are optional, in case the name is multi-word
    async def skill_roll(self, ctx, skill, character, *args):
        for ar in args:
            if ar != "":
                character = character + " " + ar

        modifier = skill_modifier(character, skill)
        await self.dice_roll(ctx,"1d20", modifier)
