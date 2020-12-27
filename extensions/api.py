import discord
from discord.ext import commands
import aiohttp
import json
from typing import Optional


class API(commands.Cog):
    BASE_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

    def __init__(self, bot: commands.bot, key: str):
        self.bot = bot
        self._key = key
        self._url = API.BASE_URL + "?key=" + self._key

    async def get_score(self, comment: str) -> Optional[float]:
        data = {
            "comment": {
                "text": comment
            },
            "requestedAttributes": {
                "PROFANITY": {}
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self._url, data=json.dumps(data)) as response:
                if response.status != 200:
                    return None

                res_json = json.loads(await response.text())
                score = res_json["attributeScores"]["PROFANITY"]["summaryScore"]["value"]

                return float(score)


def setup(bot):
    bot.add_cog(API(bot, "AIzaSyAhjVOb95ojQ__2CW9xy86DVFvynTeCtvA"))
