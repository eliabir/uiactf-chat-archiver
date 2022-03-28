#!/usr/bin/env python3

import os
import codecs

from discord.ext import commands
from dotenv import load_dotenv

from Modules._Datastructs import Message, Channel, date, datetime
from Modules._JSONgenerator import generate_json, json

load_dotenv()

DISCORD_API = os.environ.get("DISCORD_API")

bot = commands.Bot(command_prefix='!')

messages_list = []

channel_index = 3
message_index = 3

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

    #generate_object_list(bot.guilds)
    
    server = [x for x in bot.guilds if x.name == "UiA-CTF"][0]

    channels = [x for x in server.channels if "archive" in str(x.category)]

    for channel in channels:
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

    json_data = generate_json(messages_list)

    with open("json_data.json", "w") as file:
        json.dump(json_data, file, indent=4)


    #print(f'Channel: {messages_list[channel_index].channelname}')
    #print(f'Time: {messages_list[channel_index].messages[message_index].timestamp.strftime("%m/%d/%Y, %H:%M:%S")}')
    #print(f'Author: {messages_list[channel_index].messages[message_index].author}')
    #print(f'Content: {messages_list[channel_index].messages[message_index].content}')
    

bot.run(DISCORD_API)
