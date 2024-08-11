import discord
from discord.ext import commands
from kdotpy import q

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def save_attachment(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"attachments/{attachment.filename}")
            # await ctx.send(f"Attachment saved as {attachment.filename}!")
            await ctx.send(q(f"attachments/{attachment.filename}"))
    else:
        await ctx.send("No attachment found!")

bot.run("token")
