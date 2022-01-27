import discord
from discord.ext import commands


class help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief="Returns all commands", help="Sends all the commands!")
  async def help(self, ctx, cog=None):
    if not cog:
      embed = discord.Embed(
        title="All Cogs:",
        description = "Type `help {cogname}` for all of its commands!",
        color=discord.Color.random()
      )
      for cog in self.bot.cogs:
        embed.add_field(name=cog, value=f"All commands for {cog}!", inline=True)
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(
        title = f"{cog}'s Commands:",
        color = discord.Color.random()
      )
      embed.set_footer(text="This is all of the commands for this cog!")
      coga = self.bot.get_cog(cog)
      commands = coga.get_commands()
      for command in commands:
        embed.add_field(name = command.name, value=command.brief)
      await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(help(bot))
