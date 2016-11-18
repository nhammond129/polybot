import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

import random


HELP="""\
`ext.dice`
```bash
roll xdy
    Roll x dice with y sides
```
"""




def roll(die_string):
    q,s = map(int, die_string.split('d'))
    return [random.randint(1,s) for asfd in range(q)]


async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"roll"):
            r=roll(tokens[1])
            await bot.send_message(
                    message.channel,
                    "Rolling %s gives you %s = %d!"%(tokens[1],repr(r),sum(r))
                    )
        else:
            pass
    else:
        pass


