from ..bot import commands

def generate_object_list(guilds):
    server = [x for x in guilds if x.name == "UiA-CTF"][0]

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