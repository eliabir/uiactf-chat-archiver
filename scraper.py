#!/usr/bin/env python3

import os
import discord
from dotenv import load_dotenv

load_dotenv()

DISCORD_API = os.environ.get("DISCORD_API")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

client = MyClient()
client.run(DISCORD_API)

