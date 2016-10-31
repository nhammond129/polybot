import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

async def digest(message,bot):
    if message.channel.is_private:
        bot.logger.info(
                "(private)\n [%s]: %s"%(
                    message.author.name,
                    message.content
                    )
                )
    else:
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

    lgstMC=bot.configPO.read("largest message count")
    if not lgstMC:
        lgstMC=(message.author.name,msgcount+1)
    else:
        if lgstMC[1]<(msgcount+1):
            lgstMC=(message.author.name,msgcount+1)
    bot.configPO.write("largest message count",lgstMC)

    bot.userDB.write_userdata(
            message.author.id,
            "message count",
            msgcount+1
            )

