

class Class():
    def __init__(self,name):
        pass
class Character():
    def __init__(self,name,userid,classname,):
        # discord-related
        self.userid=userid # for discord

        # character atomics
        self.name=name
        self.classname=classname
        self.level=0

        # character stats
        self.attributes={
                "str":10,
                "int":10,
                "wis":10,
                "dex":10,
                "con":10,
                "cha":10
                }
        self.skills={}
