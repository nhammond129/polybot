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
roll waifu {stat}
roll tactical {stat}
    Relevant 1d6 roll vs stat
```
"""




def roll(die_string):
    q,s = map(int, die_string.split('d'))
    if not 0<q<100:
        q=99
    return [random.randint(1,s) for asfd in range(q)]


async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"roll"):
            if len(tokens)>2 and isMatch(tokens[1],"tactical"):
                x = random.randint(1,6)
                success=x<=int(tokens[2])
                if success:
                    await bot.send_message(
                        message.channel,
                        "`%d <= %d`\nYou succeeded your tactical roll!"%(x,int(tokens[2]))
                        )
                else:
                    await bot.send_message(
                        message.channel,
                        "`%d > %d`\nYou failed your tactical roll!"%(x,int(tokens[2]))
                        )
            elif len(tokens)>2 and isMatch(tokens[1],"waifu"):
                x = random.randint(1,6)
                success=x>=int(tokens[2])
                if success:
                    await bot.send_message(
                        message.channel,
                        "`%d >= %d`\nYou succeeded your waifu roll!"%(x,int(tokens[2]))
                        )
                else:
                    await bot.send_message(
                        message.channel,
                        "`%d < %d`\nYou failed your waifu roll!"%(x,int(tokens[2]))
                        )
            elif len(tokens)>1 and isMatch(tokens[1],"pizza"):
                await bot.send_message(
                        message.channel,
                        "Mmmm... tasty."
                        )
            else:
                r=roll(tokens[1])
                await bot.send_message(
                        message.channel,
                        "Rolling %s gives you %s = %d!"%(tokens[1],repr(r),sum(r))
                    )
        else:
            pass
    else:
        pass


