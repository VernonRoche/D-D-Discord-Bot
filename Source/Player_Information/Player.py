from discord.ext import commands


class Player(commands.Cog):
    def __init__(self, bot, id, ensembles):
        self.bot = bot
        self.id = id
        self.ensembles = ensembles

    # Roll a dice
    @commands.command(aliases=["player"],
                      help="Example: !dice 2 6. If you want to add a modifier use instead !dice 2 6 3.")
    async def add_ensemble(self, ctx, times=1, roll=20, modifier=0):
        None
