import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"whoami"):
            print("someone")
            await bot.send_message(
                message.channel,
                "%s,\n"
                "Your ID is `%s` \n"
                "Your discriminator is `%s` \n"
                "You are %sa bot."%(
                    message.author.name,
                    message.author.id,
                    message.author.discriminator,
                    "not "*(1-message.author.bot)
                    )
                )
        elif isMatch(tokens[0],"ping"):
            await bot.send_message(
                message.channel,
                "pong"
                )
        elif isMatch(tokens[0],"uptime"):
            bot.logger.info("DEBUG: "+bot.getUptime())
            await bot.send_message(
                message.channel,
                "I've been up for %s"%bot.getUptime()
                )
        elif isMatch(tokens[0],"help") or isMatch(tokens[0],"helb"):
            await bot.send_message(
                message.channel,
                "go fuck yourself"
                )
        elif isMatch(tokens[0],"msgcount"):
            if len(tokens)<2:
                await bot.send_message(
                    message.channel,
                    "I've seen you shitpost %d times."%(
                        bot.userDB.read_userdata(
                            message.author.id,
                            "message count"
                            )
                        )
                    )
            if isMatch(tokens[1],"top"):
                await bot.send_message(
                        message.channel,
                        "%s has shitposted the most at %d."%bot.configPO.read(
                            "largest message count"
                            )
                        )
            elif isMatch(tokens[1],"bottom"):
                pass
        elif isMatch(tokens[0],"extensions"):
            await bot.send_message(
                message.channel,
                "```%s```"%("\n".join(bot.extensions.keys()))
                )
    else:
        pass


