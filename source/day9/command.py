class command:

	def newUser(self,uid,rid,text):
		details = text.split(" ")
		if len(details) == 2:
			userOperate.newUser(uid,details[1])
			botActions.sendMessage(rid,"success")

	def greetings(self,uid,rid,text):
		try:
			username = userOperate.getUser(uid,"name")[0]
			botActions.sendMessage(rid,"%s hello"%username)
		except:
			botActions.sendMessage(rid,"use /newUser <username> to setup username")
		

functions = command()

from botActions import functions as botActions
from userOperate import functions as userOperate