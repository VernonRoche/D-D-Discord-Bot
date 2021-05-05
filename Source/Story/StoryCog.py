from discord.ext import commands
import random

from Source.Utility.Globals import stories_enum


class Story(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["story", "story_time", "story-time", "storytime", "joke"], help="Example: !story")
    async def tell_a_story(self, ctx, story_name="None", *args):
        # Check if a specific story is requested
        if story_name != "None":
            for ar in args:
                if ar != "":
                    story_name = story_name + ar
            story_name = story_name.upper()
            story_name = story_name.replace(" ", "")
        # If no story is requested, pick a random from the enum
        else:
            story_name = random.choice(list(stories_enum))
            print(story_name)

        # Generate the story
        await stories_enum[story_name](ctx)
