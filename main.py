import discord
from discord.ext import commands
import music
import os
from dotenv import load_dotenv

cogs = [music]

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)

load_dotenv()
@client.event
async def on_ready():
    print(f"{client.user.name} has connected to Discord.")

@client.Command()
async def ping(ctx):
    await ctx.send("Pong")

client.run(os.getenv("DISCORD_TOKEN"))
