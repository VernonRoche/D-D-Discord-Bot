import discord
from discord.utils import get


async def private_DM(ctx, message=None):
    message = message or "This Message is sent via DM"
    return await ctx.author.send(message)


async def add_reaction(ctx, message,emoji):
    return await message.add_reaction(emoji)


async def send_cancelable_message(ctx,message):
    sent_message=await private_DM(ctx,message)
    await add_reaction(ctx, sent_message,"❌")

def is_private_channel(ctx):
    if isinstance(ctx.channel, discord.channel.DMChannel):
        return True
    return False
