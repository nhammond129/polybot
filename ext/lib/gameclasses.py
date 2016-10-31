import asyncio
import math

def digest(message,bot):
    pass # this interface should be fully impl. in game.py

_CLASSLIST=[]
class Class():
    def __init__(self,name,hitdie=6):
        _CLASSLIST.append(self)
        self.name=name
        self.hitdie=hitdie # hp per level, roll 1d(hitdie) + CON mod


class Attribute():
    def __init__(self,base=10):
        self.base=base
        self.bonuses=[]
    def get(self):
        return self.base+sum(self.bonuses)
    def getmod(self):
        return math.floor(((self.get())-10)/2)

class Item():
    def __init__(self,rarity=0):
        self.rarity=rarity
    def rarityname(self):
        if self.rarity<-1:
            return "worthless"
        elif self.rarity==-1:
            return "poor"
        elif self.rarity==0:
            return "common"
        elif self.rarity==1:
            return "uncommon"
        elif self.rarity==2:
            return "rare"
        elif self.rarity==3:
            return "epic"
        elif self.rarity>3:
            return "legendary"

class Character():
    def __init__(self,name,user,classname,):
        # discord-related
        self.user=user # for discord -- the actual user class. Hopefully it works?

        # character atomics
        self.name=name
        self.classname=classname
        self.level=0

        # character stats
        self.attributes={
            "str":Attribute(),
            "int":Attribute(),
            "wis":Attribute(),
            "dex":Attribute(),
            "con":Attribute(),
            "cha":Attribute()
        }
        self.inventory=[]
        self.skills={}

if __name__=="__main__":
        Class(
                        name="cleric",
                        hitdie=8
                )
        Class(
                        name="warrior",
                        hitdie=12
                )
        for c in _CLASSLIST:
                print(  "-"*16, "\n",
                                "CLASS: %s"%(c.name,), "\n",
                                ""
                        )
        print("Tests completed.")
