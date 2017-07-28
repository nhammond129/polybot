import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))).replace("ext/",""))
from utils import *

from collections import Counter

HELP="""\
`ext.fridge`
```bash
Global fridges = { server, channel }

fridge list|fridges
    List your personal fridges
fridge view|see $FRIDGE
    List fridge contents
fridge add|put $FRIDGE $ITEM
    Add $ITEM to $FRIDGE
fridge remove|take $FRIDGE $ITEM
    Remove $ITEM from $FRIDGE
fridge clear|purge
    Remove all items from $FRIDGE
```
"""

class Fridge(object):
    def __init__(self,capacity=64,name="<FRIDGE NAME>"):
        self.capacity=capacity
        self.name=name
        self.items=[]
    def getCounts(self):
        return Counter(self.items)
    def add(self,item):
        if len(self.getCounts().keys())<self.capacity:
            self.items.append(item)
            return 1
        else:
            return 0
    def remove(self,item):
        if item in self.items:
            self.items.remove(item)
            return 1
        else:
            return 0
    def purge(self):
        self.items=[]

async def digest(message,bot):
    if message.content[0] in bot.commandPrefix:
        tokens=tokenize(message)
        tokens[0]=tokens[0][1:]
        if isMatch(tokens[0],"fridge"):
            userfridges=getUserData(
                    message.author.id,
                    "fridges"
                    )
            serverfridge=getData(
					"fridge.dat",
                    str(message.server.id)
                    )
            channelfridge=getData(
					"fridge.dat",
                    str(message.server.id)+str(message.channel.id)
                    )

            if serverfridge==None:
                serverfridge=Fridge(name=message.server.name)
            if channelfridge==None:
                channelfridge=Fridge(name="#"+message.channel.name)
            if userfridges==None:
                userfridges={}
            whichUserFridge=""

            try:
                if tokens[1]: pass
            except: return

            if isMatch(tokens[1],('list','fridges')):
                if not len(userfridges.keys()):
                    await bot.send_message(
                            message.channel,
                            "You do not have any fridges.\n"
                            "If you add something to a fridge you don't have,"
                            " it'll be dynamically created for you."
                            " If a fridge is empty, it'll be dynamically removed."
                            )
                    return
                await bot.send_message(
                        message.channel,
                        " ".join(['`%s`'%k for k in userfridges.keys()])
                        )
                return
            elif isMatch(tokens[1],('purge','clear')):
                if isMatch(tokens[2],'server'):
                    thisfridge=serverfridge
                elif isMatch(tokens[2],'channel'):
                    thisfridge=channelfridge
                else:
                    try:
                        if tokens[2] in userfridges:
                            thisfridge=userfridges[tokens[2]]
                        else:
                            thisfridge=Fridge(name=tokens[2])
                        whichUserFridge=tokens[2]
                    except:
                        if "default" in userfridges:
                            thisfridge=userfridges['default']
                        else:
                            thisfridge=Fridge(name='default')
                        whichUserFridge="default"
                if not len(thisfridge.items):
                    await bot.send_message(
                            message.channel,
                            "This fridge doesn't have anything in it yet."
                            )
                    return
                thisfridge.purge()
                await bot.send_message(
                        message.channel,
                        "`%s` is now empty."%thisfridge.name
                        )
            elif isMatch(tokens[1],('view','see')):
                if isMatch(tokens[2],'server'):
                    thisfridge=serverfridge
                elif isMatch(tokens[2],'channel'):
                    thisfridge=channelfridge
                else:
                    try:
                        if tokens[2] in userfridges:
                            thisfridge=userfridges[tokens[2]]
                        else:
                            thisfridge=Fridge(name=tokens[2])
                        whichUserFridge=tokens[2]
                    except:
                        if "default" in userfridges:
                            thisfridge=userfridges['default']
                        else:
                            thisfridge=Fridge(name='default')
                        whichUserFridge="default"
                if not len(thisfridge.items):
                    await bot.send_message(
                            message.channel,
                            "This fridge doesn't have anything in it yet."
                            )
                    return
                counts=thisfridge.getCounts()
                await bot.send_message(
                        message.channel,
                        "`%s` contents:\n"%(thisfridge.name,)+(
                        " ".join(
                        [   "`"+
                                (("%dx "%(counts[j])))
                            +"%s`"%(j)
                            for j in thisfridge.getCounts() ]
                        )))
            elif isMatch(tokens[1],('add','put')):
                if isMatch(tokens[2],'server'):
                    thisfridge=serverfridge
                elif isMatch(tokens[2],'channel'):
                    thisfridge=channelfridge
                else:
                    try:
                        if tokens[2] in userfridges:
                            thisfridge=userfridges[tokens[2]]
                        else:
                            thisfridge=Fridge(name=tokens[2])
                        whichUserFridge=tokens[2]
                    except:
                        if "default" in userfridges:
                            thisfridge=userfridges['default']
                        else:
                            thisfridge=Fridge(name='default')
                        whichUserFridge="default"
                try:
                    if tokens[3]: pass
                except:
                    await bot.send_message(
                            message.channel,
                            "Specify something to add!"
                            )
                    return
                state=0
                for i in range(len(tokens)-3):
                    state+=thisfridge.add(tokens[3+i])
                if not state:
                    await bot.send_message(
                            message.channel,
                            "This fridge cannot hold any more item types."
                            )
                    return
                else:
                    counts=thisfridge.getCounts()
                    await bot.send_message(
                            message.channel,
                            "`%s` now contains:\n"%(thisfridge.name,)+(
                            " ".join(
                            [   "`"+
                                    (("%dx "%(counts[j])))
                                +"%s`"%(j)
                                for j in thisfridge.getCounts() ]
                            )))
                if whichUserFridge:
                    userfridges[whichUserFridge]=thisfridge
            elif isMatch(tokens[1],('remove','take')):
                if isMatch(tokens[2],'server'):
                    thisfridge=serverfridge
                elif isMatch(tokens[2],'channel'):
                    thisfridge=channelfridge
                else:
                    try:
                        if tokens[2] in userfridges:
                            thisfridge=userfridges[tokens[2]]
                        else:
                            thisfridge=Fridge(name=tokens[2])
                        whichUserFridge=tokens[2]
                    except:
                        if "default" in userfridges:
                            thisfridge=userfridges['default']
                        else:
                            thisfridge=Fridge(name='default')
                        whichUserFridge="default"
                try:
                    if tokens[3]: pass
                except:
                    await bot.send_message(
                            message.channel,
                            "Specify something to remove!"
                            )
                    return
                state=0
                for i in range(len(tokens)-3):
                    state+=thisfridge.remove(tokens[3+i])
                if state:
                    counts=thisfridge.getCounts()
                    await bot.send_message(
                            message.channel,
                            "`%s` now contains:\n"%(thisfridge.name,)+(
                            " ".join(
                            [   "`"+
                                    (("%dx "%(counts[j])))
                                +"%s`"%(j)
                                for j in thisfridge.getCounts() ]
                            )))
                else:
                    await bot.send_message(
                            message.channel,
                            "Was not able to remove `%s`"%tokens[3]
                            )
                if whichUserFridge:
                    if not len(thisfridge.items)==0:
                        userfridges[whichUserFridge]=thisfridge
                    else:
                        userfridges.pop(whichUserFridge,None)
            else:
                pass
            setUserData(
                    message.author.id,
                    "fridges",
                    userfridges
                    )
            setData(
					"fridge.dat",
                    str(message.server.id),
                    serverfridge
                    )
            setData(
					"fridge.dat",
                    str(message.server.id)+str(message.channel.id),
                    channelfridge
                    )
        else:
            return
        return
