import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

import random


HELP="""\
`ext.pdilemma`
```bash
pd cooperate | coop | c
    Play a game of prisoner's dilemma, cooperating.
pd defect | def | 
    Play a game of prisoner's dilemma, defecting.
pd status | stat | s
    See how well you've done in iterated prisoner's dilemma so far.

example:
    You:     !pd coop
    Polybot: 
```
"""

def getPayout(CoopOne,CoopTwo):
    if CoopOne and CoopTwo:
        return (3,3)
    if CoopOne and not CoopTwo:
        return (0,5)
    if not CoopOne and CoopTwo:
        return (5,0)
    if not CoopOne and not CoopTwo:
        return (1,1)
    return (0,0) # should never be seen

def getData(bot,user,field):
    return bot.gameDB.read("%s:pd:%s"%(user,field))
def setData(bot,user,field,val):
    bot.gameDB.write("%s:pd:%s"%(user,field),val)

def pdStrategy(bot,user): # true = cooperate, false = defect
    naughty=getData(bot,user,"naughty")
    nice=getData(bot,user,"nice")
    last=getData(bot,user,"last")
    if naughty is None:
        naughty = 0
    if nice is None:
        nice = 0

    if last is None:
        return True # cooperate first

    if last is True:
        if random.random() < (nice / (1+naughty+nice))/2:
            return False # abuse them if they're really nice, sometimes.
        return True # just cooperate if they did
    else:
        if random.random() < (naughty / (1+naughty+nice)):
            return False # don't forgive repeat offenders
        else:
            return True  # sometimes we forgive them

async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        user=message.author.id
        botuser=bot.user.id
        if isMatch(tokens[0],"pd"):
            if isMatch(tokens[1],("coop","c","cooperate")):
                botThrow = pdStrategy(bot,user)
                payout = getPayout(botThrow,True)

                plyScore = getData(bot,user,"score")
                plyIters = getData(bot,user,"iterations")
                if plyScore is None: plyScore = 0
                if plyIters is None: plyIters = 0
                plyScore+=payout[1]
                plyIters+=1
                setData(bot,user,"score",plyScore)
                setData(bot,user,"iterations",plyIters)

                botScore = getData(bot,botuser,"score")
                botIterations = getData(bot,botuser,"iterations")
                if botScore is None: botScore = 0
                if botIterations is None: botIterations = 0
                botScore+=payout[0]
                botIterations+=1
                setData(bot,botuser,"score",botScore)
                setData(bot,botuser,"iterations",botIterations)

                if botThrow: botThrowWord = "cooperated"
                else: botThrowWord = "defected"

                await bot.send_message(
                        message.channel,
                        "I %s, you cooperated.\n"%(botThrowWord,) +
                        "I get %d points, you get %d points."%(payout[0],payout[1])
                        )

                setData(bot,user,"last",True)
                nice = getData(bot,user,"nice")
                if nice is None:
                    nice = 0
                setData(bot,user,"nice",nice+1)

            elif isMatch(tokens[1],("defect","d","def")):
                botThrow = pdStrategy(bot,user)
                payout = getPayout(botThrow,False)

                plyScore = getData(bot,user,"score")
                plyIters = getData(bot,user,"iterations")
                if plyScore is None: plyScore = 0
                if plyIters is None: plyIters = 0
                plyScore+=payout[1]
                plyIters+=1
                setData(bot,user,"score",plyScore)
                setData(bot,user,"iterations",plyIters)

                botScore = getData(bot,botuser,"score")
                botIterations = getData(bot,botuser,"iterations")
                if botScore is None: botScore = 0
                if botIterations is None: botIterations = 0
                botScore+=payout[0]
                botIterations+=1
                setData(bot,botuser,"score",botScore)
                setData(bot,botuser,"iterations",botIterations)

                if botThrow: botThrowWord = "cooperated"
                else: botThrowWord = "defected"

                await bot.send_message(
                        message.channel,
                        "I %s, you defected.\n"%(botThrowWord,) +
                        "I get %d points, you get %d points."%payout
                        )

                setData(bot,user,"last",False)
                naughty = getData(bot,user,"naughty")
                if naughty is None:
                    naughty = 0
                setData(bot,user,"naughty",naughty+2)

            elif isMatch(tokens[1],("status","stat","s")):
                plyScore = getData(bot,user,"score")
                plyIters = getData(bot,user,"iterations")
                botScore = getData(bot,botuser,"score")
                botIters = getData(bot,botuser,"iterations")
                if plyScore is None:
                    plyScore = 0
                if plyIters is None:
                    plyIters = 0
                if botScore is None:
                    botScore = 0
                if botIters is None:
                    botIters = 0
                await bot.send_message(
                    message.channel,
                    "You've scored a total `%d` out of `%d` iterations,"%(plyScore,plyIters) +
                    "for an average score of `%d`.\n"%(plyScore/((plyIters==0)+plyIters),) +
                    "I scored an average of `%d` over `%d` iterations."%(botScore/((botIters==0)+botIters),botIters)
                    )
        else:
            await bot.send_message(
                    message.channel,
                    HELP
                    )
