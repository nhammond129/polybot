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
    0 < x < 101
    2 < y < 10001
roll waifu {stat} {rolls}
roll tactical {stat} {rolls}
    Relevant {rolls}d6 roll vs stat
roll pizza
    Why? Why would you do that?
```
"""


def roll(die_string):
    q,s = map(int, die_string.split('d'))
    if not 0<q<101:
        q=100
    if not 2<s<10001:
        s=6
    return [random.randint(1,s) for asfd in range(q)]


async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        print(tokens)
        if isMatch(tokens[0],"roll"):
            if len(tokens)>2 and isMatch(tokens[1],["tactical","t"]):
                if len(tokens)>3:
                    rolls=int(tokens[3])
                    if not 0<rolls<11:
                        rolls=1
                    # rolls bounded above by 11, exclusive
                else:
                    rolls=1
                while rolls:
                    x = random.randint(1,6)
                    if x==int(tokens[2]):
                        await bot.send_message(
                                message.channel,
                                "`%d=%d` You matched your waifu stat, ask a question."%(int(tokens[2]),int(tokens[2]))
                                )
                        continue
                    success=x<int(tokens[2])
                    if success:
                        await bot.send_message(
                            message.channel,
                            "`%d<%d`\nYou succeeded your tactical roll!"%(x,int(tokens[2]))
                            )
                    else:
                        await bot.send_message(
                            message.channel,
                            "`%d>%d`\nYou failed your tactical roll!"%(x,int(tokens[2]))
                            )
                    rolls-=1
            elif len(tokens)>2 and isMatch(tokens[1],["waifu","w"]):
                if len(tokens)>3:
                    rolls=int(tokens[3])
                    if not 0<rolls<11:
                        rolls=1
                    # rolls bounded above by 11, exclusive
                else:
                    rolls=1
                while rolls:
                    x = random.randint(1,6)
                    if x==int(tokens[2]):
                        await bot.send_message(
                                message.channel,
                                "`%d=%d` You matched your waifu stat, ask a question."%(int(tokens[2]),int(tokens[2]))
                                )
                        continue
                    success=x>int(tokens[2])
                    if success:
                        await bot.send_message(
                            message.channel,
                            "`%d>%d`\nYou succeeded your waifu roll!"%(x,int(tokens[2]))
                            )
                    else:
                        await bot.send_message(
                            message.channel,
                            "`%d<%d`\nYou failed your waifu roll!"%(x,int(tokens[2]))
                            )
                    rolls-=1
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


