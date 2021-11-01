class userOperate:

	def __init__(self):
		pass

	def newUser(self,uid,name):
		DBexec("INSERT INTO USER (ID,NAME) VALUES (?,?)",[uid,name])

	def getUser(self,uid,*args):
		data = DBqueryone("SELECT %s FROM USER WHERE ID=?" % 
			",".join(args),
			[uid]
		)
		if data:
			return data
		else:
			return [0 for i in range(len(args))]

from database import *
functions = userOperate()