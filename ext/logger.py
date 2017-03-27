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
    # Logging Begins
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
    # Logging ends. Put the rest of this in another module?
    said=bot.userDB.read_userdata(
            message.author.id,
            "said"
            )
    if not said:
        said=[]
    said.append(message.content)
    bot.userDB.write_userdata(
            message.author.id,
            "said",
            said
            )

