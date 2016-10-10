import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

class SpaceGame:
    def __init__(self):
        pass
    def getstats(self,bot,user):
        return bot.gameDB.read("stats")
    def setstats(self,bot,user,stats):
        bot.gameDB.write("%s:stats"%user,stats)

    def getastats(self,bot,user):
        return bot.gameDB.read("stats")
    def setastats(self,bot,user,stats):
        bot.gameDB.write("%s:stats"%user,stats)

SG=SpaceGame()

async def digest(message,bot):
    if not message.channel.name=="botdev":
        return
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        if isMatch(tokens[0],"sg"):
            if isMatch(tokens[1],"help"):
                await bot.send_message(
                        message.channel,
                        "Help msg for gamething\n"
                        "help stats\n"
                        "You are user <%s>"%(
                            message.author.id
                            )
                        )
            elif isMatch(tokens[1],"stats"):
                stats = SG.getstats(bot,message.author.id)
                bot.logger.info(str(stats))
                if stats==None:
                    stats = {"pos":(0,0,0),"vel":(0,0,0),"hull":"22%"}
                    SG.setstats(bot,message.author.id,stats)
                bot.logger.info(str(stats))
                await bot.send_message(
                        message.channel,
                        "\n".join(
                            [key+":%s"%str(stats[key]) for key in stats.keys()]
                            )
                        )
            else:
                pass
        else:
            pass
    return
    bot.gameDB.read(key)
    bot.gameDB.write(key,val)

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

