import json

json_dict = {}
message_list = []

def generate_json(messages):
    for channel in messages:
        message_list.clear
        
        for message in channel.messages:
            message_dict = {message.author: message.content}
            message_list.append(message_dict)
        
        if channel.channelname not in json_dict:
            json_dict[channel.channelname] = message_list
        else:
            json_dict[channel.channelname].extend(message_list)

    json_data = json.dumps(json_dict, indent=4)

    return json_dict
