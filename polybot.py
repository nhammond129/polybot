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

# Fix relative paths
sys.path.append(os.path.realpath('..'))

def ensure_dir(directory):
	if not os.path.exists(directory):
		print(directory)
		os.makedirs(directory)

ensured_dirs=[
	"./data",
	"./data/logs",
	"./data/media",
	"./data/users"
	]
for d in ensured_dirs: # make sure some directories exist
	ensure_dir(d)

class Bot(discord.Client):
    def __init__(self,
            commandPrefix=['~','!','#','/',':','-','?',';','|','.'],
            **options
            ):
        super().__init__(**options)

        self.startTime=time.time() # for uptime checking

		# setup logging
        self.logger=logging.getLogger("polybot")
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler( # log to file
                filename='./data/logs/%sdiscord.log'%(
                    datetime.now().strftime("[%b %d %Y] ")
                    ),
                encoding='utf-8',
                mode='a+'
                )
        handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(levelname)s] : %(message)s',
            datefmt="[%d/%m/%y %H:%M:%S]"
            ))
        self.logger.addHandler(handler)
        handler = logging.StreamHandler() # log to stdout
        handler.setFormatter(logging.Formatter(
            '%(asctime)s [%(levelname)s] : %(message)s',
            datefmt="[%d/%m/%y %H:%M:%S]"
            ))
        self.logger.addHandler(handler)

        self.commandPrefix=commandPrefix
        self.extensions={}
        self.load_all_extensions()

    async def message_handler(self,message):
		# heart and soul: for each extension, handle the new message.
        for ext in self.extensions.values():
            await ext.digest(message,self)

    def getUptime(self):
        return str(timedelta(seconds=(time.time()-self.startTime)))

	# warning: literal h*ckin magic beyond this point.
	# I don't really know why it works, exactly. Or why it's not 100% working, either.

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
            ext = ext.replace("/", "\\") # Linux fix (gross)
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
