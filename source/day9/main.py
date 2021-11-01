from msgRecv import functions as msgRecv
from telepot.loop import MessageLoop
from botActions import bot
import threading as td
import time

MessageLoop(bot, {"chat": msgRecv.handle}).run_as_thread()

# ------- auto work block ------
def background_work():
	while True:
		time.sleep(300)

t = td.Thread(target=background_work)
t.start()
# ------- auto work block ------

# ------- success depoly block ------
print("====== ALL METHODS RUNNING ======")
# ------- success depoly block ------

while 1:
	pass