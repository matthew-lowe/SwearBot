import discord
from discord.ext import commands
import datetime


class Util(commands.Cog):
    def __init__(self, bot: commands.bot):
        self.bot = bot

    def style_embed(self, embed, ctx: commands.Context):
        embed.timestamp = datetime.datetime.utcnow()

        member = ctx.message.guild.get_member(ctx.author.id)
        embed.set_footer(text=f"Requested by {member.display_name}#{ctx.author.discriminator}",
                         icon_url=ctx.message.author.avatar_url_as(format='png'))
        roles = member.roles
        color = roles[len(roles) - 1].color
        embed.color = color


def setup(bot):
    bot.add_cog(Util(bot))