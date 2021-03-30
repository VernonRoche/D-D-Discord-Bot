from discord.utils import get


async def private_DM(ctx, message=None):
    message = message or "This Message is sent via DM"
    return await ctx.author.send(message)


async def add_reaction(ctx, message, emoji="❌"):
    return await message.add_reaction(emoji)


async def create_exit_reactions(ctx, message):
    for emoji in ('🇪', '🇽', '🇮', '🇹', '❌'):
        await add_reaction(ctx, message, emoji)

async def send_cancelable_message(ctx,message):
    sent_message=await private_DM(ctx,message)
    await create_exit_reactions(ctx,sent_message)
