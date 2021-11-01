class botActions:
	def __init__(self):
		self.fileTypeDict = {
			"photo": bot.sendPhoto,
			"video": bot.sendVideo,
			"document": bot.sendDocument,
		}

	def sendMessage(self,gid,text):
		return bot.sendMessage(gid,text)

	def sendFile(self,chatID,ttype,acid,caption=None):
		return self.fileTypeDict[ttype](chatID,acid,caption=caption)

import const,telepot

bot = telepot.Bot(const.BOT["token"])
functions = botActions()

import numpy as np