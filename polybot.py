import discord

import utils

import asyncio
import sys
import os
import time
import glob
import importlib
from datetime import datetime
from datetime import timedelta
import logging

class Bot(discord.Client):
    def __init__(self,
            commandPrefix=['~','!','#','/',':','-','?',';','|','.'],
            **options
            ):
        super().__init__(**options)

        self.startTime=time.time()

        dir_path = os.path.dirname(os.path.realpath(__file__))

        self.logger=logging.getLogger("dotbot")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler(
                filename=dir_path+'/data/logs/%sdiscord.log'%(
                    datetime.now().strftime("[%H:%M:%S] ")
                    ),
                encoding='utf-8',
                mode='a'
                )
        handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(levelname)s] : %(message)s',
            datefmt="[%d/%m/%y %H:%M:%S]"
            ))
        self.logger.addHandler(handler)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(levelname)s] : %(message)s',
            datefmt="[%d/%m/%y %H:%M:%S]"
            ))
        self.logger.addHandler(handler)

        self.userDB=utils.UserDB()
        self.gameDB=utils.PersistenceObject("gamedata.dat")
        self.fridgeDB=utils.PersistenceObject("fridge.dat")
        self.configPO=utils.PersistenceObject("config.dat")

        self.tempvars={}

        self.commandPrefix=commandPrefix

        self.extensions={}
        self.load_all_extensions()

    async def message_handler(self,message):
        for ext in self.extensions.values():
            await ext.digest(message,self)

    def getUptime(self):
        return str(timedelta(seconds=(time.time()-self.startTime)))

    def load_extension(self,extname):
        if extname in self.extensions:
            return

        lib=importlib.import_module(extname)
        if not hasattr(lib,'digest'):
            del lib
            del sys.modules[extname]
            raise Exception("Extension %s does not have a `digest` function."%extname)

        self.extensions[extname] = lib

    def purge_extension(self,extname):
        lib = self.extensions.get(extname)
        if lib is None:
            return
        del lib
        del self.extensions[extname]
        del sys.modules[extname]

    def list_extensions(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        exts = glob.glob(dir_path+"/ext/*.py")
        clean = []
        for ext in exts:
            ext = ext.replace("/", "\\") # Linux fix (hacky)
            clean.append("ext."+ext.split("\\")[-1].replace(".py",""))
        return clean

    def load_all_extensions(self):
        for ext in self.list_extensions():
            self.load_extension(ext)

    def purge_all_extensions(self):
        x = tuple(self.extensions.keys())
        for ext in x:
            self.purge_extension(x)

    def get_extension(self,extname):
        self.extensions.get(extname)
