import sys
import asyncio
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

class Game:
    def __init__(self):
        pass
    def getvar(self,bot,user,var):
        return bot.gameDB.read("%s:%s"%(user,str(var)))
    def setvar(self,bot,user,var,value):
        bot.gameDB.write("%s:%s"%(user,str(var)),value)
    async def getstatus(self,bot,message):
        user=message.author.id
        status = self.getvar(bot,user,'status')
        if status==None:
            status = {"HP":100,"Mana":0,"Location":(0,0)}
            self.setvar(bot,user,'status',status)
        await bot.send_message(
            message.channel,
            "\n".join(
                [key+":%s"%str(status[key]) for key in status.keys()]
                )
            )
    async def getclass(self,bot,message):
        user=message.author.id
        def class_check(m):
            return (
                    m.content.split(" ")[0].lower() in
                    ["fighter","mage","cleric","bard"]
                )
        classvar = self.getvar(bot,user,'class')
        if classvar==None:
            await bot.send_message(
                message.channel,
                "You don't have a class yet. Choose one!\n"
                "fighter mage cleric bard"
                )
            ans = await bot.wait_for_message(
                timeout=60.0,
                author=message.author,
                check=class_check
                )
            if ans is None:
                await bot.send_message(
                    message.channel,
                    "Sorry, you took too long. Try again."
                    )
            else:
                classvar=ans.content.lower()
                self.setvar(bot,user,'class',classvar)
                await bot.send_message(
                    message.channel,
                    "Your class is now \"%s\"."%(classvar)
                    )
        else:
            await bot.send_message(
                message.channel,
                "Your class is \"%s\"."%(classvar)
                )
        return

SG=Game()

async def digest(message,bot):
    if not message.channel.name=="botdev":
        return
    if message.content[0] in bot.commandPrefix:
        user=message.author.id
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        if isMatch(tokens[0],"game"):
            if isMatch(tokens[1],"help"):
                await bot.send_message(
                        message.channel,
                        "Help msg for gamething\n"
                        "help, status, class\n"
                        "You are user <%s>"%(
                            user
                            )
                        )
            elif isMatch(tokens[1],"status"):
                await SG.getstatus(bot,message)
            elif isMatch(tokens[1],"class"):
                await SG.getclass(bot,message)
            else:
                pass
        else:
            pass
    return
