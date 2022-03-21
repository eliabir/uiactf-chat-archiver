#!/usr/bin/env python3

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_API = os.environ.get("DISCORD_API")

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    print("="*100)

    print(bot.guilds)

    emote_server = bot.guilds[1]
    print(f'EMOTE SERVER: {emote_server}')

    print(f'EMOTE CHANNEL: {emote_server}')

    test_channels = []
    for channel in emote_server:
        if "archive" in channel.name:
            test_channels.append(channel)

    print(f'TEST CHANNELS: {test_channels}')


bot.run(DISCORD_API)