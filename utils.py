import shelve
import os
import logging
import shlex

logger = logging.getLogger("polybot")
dir_path = os.path.dirname(os.path.realpath(__file__))

class InvalidFileIO(Exception):
	pass

def getData(filename,key):
	with shelve.open(dir_path+"/data/"+filename) as db:
		db.sync()
		if key in db.keys():
			return db[key]
		else:
			return None

def setData(filename,key,value):
	with shelve.open(dir_path+"/data/"+filename,writeback=True) as db:
		db[key]=value
		db.sync()


def getUserData(ID,key):
	with shelve.open(dir_path+"/data/users/"+ID+".user") as db:
		db.sync()
		if key in db.keys():
			return db[key]
		else:
			return None

def setUserData(ID,key,value):
	with shelve.open(dir_path+"/data/users/"+ID+".user",writeback=True) as db:
		db[key]=value
		db.sync()

def tokenize(message):
	return shlex.split(message.content)

def isMatch(s1,s2):
	if type(s2) in (list,tuple):
		return s1.lower() in [k.lower() for k in s2]
	else:
		return s1.lower() == s2.lower()

def isOwner(message):
	return message.author.id=="152273482846175234"
