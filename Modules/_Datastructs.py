from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Message:
    timestamp: datetime
    author: str
    content: str


@dataclass
class Channel:
    channelname: str
    messages: list[Message]