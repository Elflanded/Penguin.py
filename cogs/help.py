import discord
from discord.ext import commands
import time
import datetime

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(
   name="help"
   )
  async def help(self, ctx):
      help_embed = discord.Embed(
        title="Help",
        description="Choose a section `!help <section>`",
        color=0x04fcfc
      )

      help_embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/mx9ydy1KwKdsMA9t5jdzCsKfHLW-Y_uFqg7_3uD0nXc/https/cdn.discordapp.com/avatars/750884902727188542/4ad57be3c5b635a1d84e24efab0ea421.png?width=80&height=80")

      help_embed.add_field(name="Sections", value="● **__Commands__** - Normal commands\n● **__Levels__** - Level based commands\n● **__Music__** - Music based commands\n● **__Currency__** - Currency based commands")

      help_embed.timestamp = datetime.datetime.utcnow()
      help_embed.set_footer(text=f'Command issued by {ctx.author.name}#{ctx.author.discriminator}\u200b',icon_url=ctx.author.avatar_url)

      
      await ctx.send(embed=help_embed)


def setup(bot):
    bot.add_cog(Help(bot))
