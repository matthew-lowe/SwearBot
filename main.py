import discord
from discord.ext import commands
import json
import os

config = json.loads(open("config.json", "r").read())

bot = commands.Bot(command_prefix=config["prefix"])


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} successfully!")

    # Load files in extensions folder
    for file in os.listdir("./extensions"):
        if file.endswith(".py"):
            bot.load_extension("extensions." + file.split(".")[0])

    print("Loaded extensions!")


if __name__ == "__main__":
    token = open("token.txt", "r").read()
    bot.run(token)
