import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

import emoji
from fuzzywuzzy import fuzz

def emjDist(token,emjstr):
    tot_ratio=0
    tkns=0
    for i in emjstr.replace(":","").split("_"):
        tot_ratio+=fuzz.ratio(token.lower(),i.lower())
        tkns+=1
    return tot_ratio/tkns

async def digest(message,bot):
    return
    elist=list(emoji.unicode_codes.EMOJI_UNICODE.keys())
    possible=[]
    for token in message.content.split(" "):
        elist.sort(key=lambda x: emjDist(token,x))
        if emjDist(token,elist[-1])<90:
            continue
        possible.append(
                elist[-1]
                )
    for e in possible[:3]:
        await bot.add_reaction(
                message,
                emoji.unicode_codes.EMOJI_UNICODE[e]
                )

    return
    if message.content!="edeath":
        return
    elist=list(emoji.unicode_codes.EMOJI_UNICODE.values())
            #"\U0001F44C"
    for e in random.sample(set(elist),20):
        await bot.add_reaction(message,
                e
                )
    bot.logger.info(
            "(emoji)\n %s"%(e,)
            )
    return
