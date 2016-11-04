import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

async def digest(message,bot):
    return
    emoji="\U0001F44C"
    print("AM TRYING TO EMOJI")
    await bot.add_reaction(message,
            emoji
            )
    bot.logger.info(
            "(emoji)\n %s"%(emoji,)
            )
    return
