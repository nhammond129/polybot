import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

async def digest(message,bot):
    if not message.channel.name=="botdev":
        return
    if message.content.startswith(".example"):
        await bot.send_message(
                message.channel,
                "This an example command."
                )
