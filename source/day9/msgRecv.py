class msgRecv:
	def __init__(self):
		self.fileTypeList = ["photo","video","document"]
		self.commandDict = {
			"newUser":command.newUser,
			"greetings":command.greetings
		}

	def handle(self,rowMsg):
		msg = jValue(rowMsg)
		uid = "%s" % msg.get("from", "id")
		userName = "%s %s\nusername : @%s" % (msg.get("from","first_name"),msg.get("from","last_name"),msg.get("from","username"))
		rid = "%s" % msg.get("chat", "id")
		msgID = "%s" % msg.get("message_id")
		chatTitle = "%s" % msg.get("chat","title")
		text = msg.get("text")
		isCommand = text and text.startswith("/")
		isPrivate = msg.get("chat", "type") == "private"
		isFile = False
		isAnimate = False
		isChannel = msg.get("chat", "type") == "channel"
		isForward = msg.get("forward_date")

		if isCommand:
			commandText = text.replace("/", "").split(" ")[0]
			if self.commandDict.get(commandText):

				if commandText in ["block","unblock"]:
					replyToCapt = msg.get("reply_to_message","caption") or msg.get("reply_to_message","text")
					self.commandDict[commandText](uid,rid,text,replyToCapt)
				else:
					self.commandDict[commandText](uid,rid,text)
				

		for i in self.fileTypeList:
			if msg.get(i):
				ttype = i
				files = msg.get(i)
				isFile = True

from command import functions as command

functions = msgRecv()

from botActions import functions as botActions
from jValue import jValue
import time,const