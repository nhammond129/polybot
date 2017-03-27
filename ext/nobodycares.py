import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

async def digest(message,bot):
    if not message.channel.name=="no_one_cares":
        return
    if message.author.id in ["122069277758062593", "147938126269120512"]:
        await bot.send_message(
                message.channel,
                "no one cares"
                )
