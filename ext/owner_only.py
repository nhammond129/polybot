import sys
from os import path,system
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

HELP="""\
`ext.owner_only`
```bash
reload
shell
purge
sudoku
```
"""

async def digest(message,bot):
    if isOwner(message) and message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"reload"):
            MSG = await bot.send_message(
                    message.channel,
                    "Reloading all extensions..."
                    )
            bot.purge_all_extensions()
            bot.load_all_extensions()
            await bot.edit_message(
                    MSG,
                    "Reloaded all extensions successfully!"
                    )
        elif isMatch(tokens[0],"shell"):
            await bot.send_message(
                    message.channel,
                    exec(" ".join(tokens[1:]))
                    )
        elif isMatch(tokens[0],"purge"):
            bot.purge_all_extensions()
            await bot.send_message(
                    message.channel,
                    "Purged all extensions in cleansing fire."
                    )
        elif isMatch(tokens[0],"sudoku"):
            await bot.send_message(
                    message.channel,
                    "Committing honourable and mathematical sudoku..."
                    )
            bot.loop.run_until_complete(bot.logout())
            bot.loop.close()
    else:
        pass


