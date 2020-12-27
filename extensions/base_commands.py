import discord
from discord.ext import commands
import math


class BaseCommands(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    @commands.command(name="score")
    async def score(self, ctx, *args):
        message = ""

        for arg in args:
            message += arg + " "

        api = self.bot.get_cog("API")
        score = await api.get_score(message.lower())

        if score is None:
            print("rate limited!")
            return

        await ctx.send(str(math.floor(score * 100)) + "%")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.content[:6].lower() == ">score":
            return

        api = self.bot.get_cog("API")
        score = await api.get_score(message.content.lower())

        if score is None:
            print("Rate limited!")
            return

        if score > 0.65:
            await message.delete()
            await message.channel.send("{0} Inappropriate message ({1}% chance)".format(message.author.mention, int(score * 100)))


def setup(bot):
    bot.add_cog(BaseCommands(bot))
