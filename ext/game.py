import sys
import asyncio
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *
from .lib import gameclasses

HELP="""\
`ext.game`
```bash
Hey, look away.
This shit is still in development, yo.
```
"""

async def getResponse(self,bot,message,responsecheck):
    uid=message.author.id
    answer = await bot.wait_for_message(
            timeout=15.0,
            author=message.author,
            check=responsecheck
            )
    if answer is None:
        await bot.send_message(
                message.channel,
                "Sorry, I got bored waiting. You'll have to be faster next time."
                )
    return answer

async def digest(message,bot):
    if not (message.channel.name=="botdev" or message.channel.is_private):
        return
    if message.content[0] in bot.commandPrefix:
        user=message.author.id
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
		# do stuff here
    return
