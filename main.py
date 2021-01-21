import discord
from discord.ext import commands
import os
from os import environ


bot = commands.Bot(command_prefix=environ.get("PREFIX"))
bot.remove_command("help")


@bot.event
async def on_ready():
 await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Zyphon fish 🎣"))


for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")





bot.run(environ.get("TOKEN"))