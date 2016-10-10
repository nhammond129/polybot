import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

async def digest(message,bot):
    bot.logger.info(
            "#%s on %s\n  [%s]: %s"%(
                message.channel.name,
                message.channel.server.name,
                message.author.name,
                message.content
                )
            )

    msgcount=bot.userDB.read_userdata(
            message.author.id,
            "message count"
            )
    if not msgcount:
        msgcount=0
    bot.userDB.write_userdata(
            message.author.id,
            "message count",
            msgcount+1
            )

