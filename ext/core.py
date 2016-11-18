import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

HELP="""\
`ext.core`
```bash
help $EXTENSION
    Get the help message for $EXTENSION
whoami
    NONE OF YOUR BUSINESS
ping
    pong
uptime
    Get bot uptime
msgcount
    See how many times Polybot has seen you shitpost
msgcount top
    See who Polybot has seen shitpost the most
extensions
    Get a list of loaded extensions
```
"""

async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        if isMatch(tokens[0],"help") | isMatch(tokens[0],"helb"):
            if len(tokens)==1:
                await bot.send_message(
                        message.channel,
                        "Try passing an extension to see the **help** message for it.\n"
                        "_Example:_ `!help channel`\n"
                        "You can use `!extensions` to get a list of loaded extensions."
                        )
            else:
                if not tokens[1][:4]=="ext.":
                    tokens[1]="ext."+tokens[1]
                try:
                    hlpmsg=bot.extensions[tokens[1]].HELP
                except:
                    hlpmsg="Could not parse extension `%s`."%tokens[1]
                await bot.send_message(
                        message.channel,
                        hlpmsg
                        )
        elif isMatch(tokens[0],"whoami"):
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


