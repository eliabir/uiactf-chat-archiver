#!/usr/bin/env python3

from itertools import count
import os
from ssl import create_default_context
from unicodedata import name
from attr import asdict
import discord

from datetime import date, datetime
from dataclasses import dataclass
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_API = os.environ.get("DISCORD_API")

bot = commands.Bot(command_prefix='!')


@dataclass
class Message:
    timestamp: datetime
    author: str
    content: str


@dataclass
class Channel:
    channelname: str
    messages: list[Message]


messages_list = []

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    
    server = [x for x in bot.guilds if x.name == "UiA-CTF"][0]

    channels = [x for x in server.channels if "archive" in str(x.category)]

    for cid, channel in enumerate(channels):
        channel_messages = await channel.history().flatten()

        message_object_list = []
        for message in channel_messages:
            message_object_list.append(
                Message(
                    timestamp=message.created_at,
                    author=message.author.name,
                    content=message.content
                )
            )
        messages_list.append(
            Channel(
                channelname=channel.name,
                messages=message_object_list
            )
        )

    print(f'Time: {messages_list[0].messages[0].timestamp.strftime("%m/%d/%Y, %H:%M:%S")}')
    print(f'Author: {messages_list[0].messages[0].author}')
    print(f'Content: {messages_list[0].messages[0].content}')
    

bot.run(DISCORD_API)
