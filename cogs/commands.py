import discord
from discord.ext import commands


class Commands(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(
    name="serverinfo",
    description="test"
  )
  async def serverinfo(self, ctx):
   embed = discord.Embed(
    title=guild.name
   )

   await ctx.send(embed=embed)







def setup(bot):
    bot.add_cog(Commands(bot))