import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

HELP="""\
`ext.logger`
```bash
Just a logging module.
No commands here.
```
"""
async def digest(message,bot):
    if message.channel.is_private:
        bot.logger.info(
                "(private)\n\t[%s]: %s"%(
                    message.author.name,
                    message.content
                    )
                )
    else:
        bot.logger.info(
                    "#%s on %s\n\t[%s]: %s"%(
                    message.channel.name,
                    message.channel.server.name,
                    message.author.name,
                    message.content
                    )
                )
