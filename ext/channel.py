import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

HELP="""\
`ext.channel`
```bash
channel purge
    Purge the channel -- owner only
    NOTE: only works if bot is a mod
channel createdat
    See when the channel was created
```
"""

async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"channel"):
            if isMatch(tokens[1],"purge") and isOwner(message):
                msgtmp = await bot.send_message(
                        message.channel,
                        "Purging channel..."
                        )
                await bot.purge_from(
                    message.channel,
                    limit=1000,
                    before=msgtmp
                    )
                await bot.edit_message(
                        msgtmp,
                        "Channel purged!"
                        )
            elif isMatch(tokens[1],"created-at"):
                await bot.send_message(
                        message.channel,
                        "#%s created at %s"%(
                            message.channel.name,
                            message.channel.created_at()
                            )
                        )
    else:
        pass


