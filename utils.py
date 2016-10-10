import shelve
import os
import logging

class InvalidFileIO(Exception):
    pass

class PersistenceObject:
    def __init__(self,filename):
        self.logger = logging.getLogger("dotbot")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.filepath=dir_path+"/data/"+filename

    def read(self,key):
        with shelve.open(self.filepath) as db:
            db.sync()
            if key in db.keys():
                return db[key]
            else:
                return None

    def write(self,key,value):
        with shelve.open(self.filepath,writeback=True) as db:
            db[key]=value
            db.sync()

class UserDB():
    def __init__(self,directory="/data/users/"):
        self.logger = logging.getLogger("dotbot")
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.path=dir_path+directory

    def read_userdata(self,ID,key):
        with shelve.open(self.path+ID+".user") as db:
            db.sync()
            if key in db.keys():
                return db[key]
            else:
                return None

    def write_userdata(self,ID,key,value):
        with shelve.open(self.path+ID+".user",writeback=True) as db:
            db[key]=value
            db.sync()

def tokenize(message):
    return message.content.split(" ")

def isMatch(s1,s2):
    return s1.lower() == s2.lower()

def isOwner(message):
    return message.author.id=="152273482846175234"
