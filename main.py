
import time
from random import shuffle
import threading
import thread
from ImageRecognition.detectShapes import DetectShapes
import sys
import os
import webbrowser
from WireCutting.WireCutting import WireCutting
from VoiceRecog.speech.speech.speech import SpeechRecognition
from Display.screen import Display

class GameInstance:

	def __init__(self, diff = -1):
		while diff < 1 or diff > 3:
			diff = raw_input("Please choose a difficulty level (1-3): ")
			diff = int(diff)
		self.difficulty = diff
		self.time = 240/self.difficulty #time left in seconds
		self.timeleft = self.time+3
		self.errorPenalty = 10*self.difficulty
		self.complete = False
		self.minigames = ['buttons', 'images', 'gestures', 'voice']
		shuffle(self.minigames)
		self.minigames.append('wirecutting')
		self.thread = threading.Thread(target = self.timer, args = ())
		self.thread.daemon = True
		self.topText = ""
		self.prevTopText = ""
		self.botText = ""
		self.prevBotText = ""
		self.lcd = Display()


	def kill(self):
		del self

	def writeTop(self, text):
		self.prevTopText = self.topText
		self.topText = self.lcd.writeTop(text)

	def writeBot(self, text):
		self.prevBotText = self.botText
		self.botText = self.lcd.writeBot(text)

	def get_difficulty(self):
		print "Difficulty level: " + str(self.difficulty)
		self.writeTop("Difficulty level: " + str(self.difficulty))
		return self.difficulty

	def get_time(self):
		print "\nTime left: " + str(int(self.timeleft))
		self.writeBot("\nTime left: " + str(int(self.timeleft)))
		return int(self.timeleft)

	def timer(self):
		startTime = int(time.time())
		oldtimeleft = self.timeleft
		while True:
			timeDiff = int(time.time()) - startTime
			self.timeleft = self.time - timeDiff
			self.get_time()
			time.sleep(1)
			if(self.timeleft <= 0):
				print "BOOM!"
				self.writeTop("BOOM!")
				webbrowser.open("https://www.youtube.com/watch?v=wdXU4R8JBe4", new=0, autoraise=True)
				thread.interrupt_main()
				sys.exit(0)


	def intro(self):
		print "Welcome to the bomb defusal training module!"
		self.writeTop("Welcome!")
		time.sleep(3)
		print "You have chose the difficulty level: " + str(self.difficulty)
		self.writeTop("Difficulty: " + str(self.difficulty))
		time.sleep(1)
		print "That means you have exactly " + str(self.time) + "s to defuse this bomb!"
		self.writeTop("You have " + str(self.time) + "s")
		time.sleep(2)
		print "I hope you are ready because it's about to get intense in here!"
		time.sleep(3)
		print "3"
		self.writeTop("3")
		time.sleep(1)
		print "2"
		self.writeTop("2")
		time.sleep(1)
		print "1"
		self.writeTop("1")
		time.sleep(1)
		print "0"
		self.writeTop("0")

	def start_game(self):
		#self.intro()
		currGame = 1
		self.thread.start()
		while(not self.complete and self.timeleft > 0):
				#Also write new time to LCD screen

			print "\nTime to play: " + self.minigames[0]
			result = self.start_minigame(self.minigames[0])
			if result == 1:
				print "Congratulations you passed the first level"

			print "\nTime to play: " + self.minigames[1]
			result = self.start_minigame(self.minigames[1])
			if result == 1:
				print "Congratulations you passed the second level"	

			print "\nTime to play: " + self.minigames[2]
			result = self.start_minigame(self.minigames[2])
			if result == 1:
				print "Congratulations you passed the third level"

			print "\nTime to play: " + self.minigames[3]
			result = self.start_minigame(self.minigames[3])
			if result == 1:
				print "Congratulations you passed the fourth level"

			print "\nTime to play: " + self.minigames[4]
			result = self.start_minigame(self.minigames[4])
			if result == 1:
				print "Congratulations you passed the last level"
			self.complete = True


		if self.timeleft == 0:
			print "BOOM"
		else:
			print "Congratulations you've defused the bomb"

	def get_minigames(self):
		print '[%s]'%', '.join(map(str, self.minigames))
		return self.minigames

	def start_minigame(self, game_name):
		result = 0
		if game_name == "images":
			d = DetectShapes()
			print "Draw a " + d.get_target_color() + ' ' + d.get_target_shape() + "!"
			result = d.start_minigame()

		elif game_name == "buttons":
			result = 1
			time.sleep(5)

		elif game_name == "gestures":	
			result = 1
			time.sleep(5)

		elif game_name == "voice":
			v = SpeechRecognition()
			result = v.startrecording()

		elif game_name == "wirecutting":
			while result == 0:
				w = WireCutting()
				result = w.startGame()
				if result == 0:
					self.time -= self.errorPenalty
					print "Error! Reconnect that wire within 5 seconds!"
					time.sleep(5)

		return result	


if __name__ == '__main__':
	g = GameInstance()
	g.get_minigames()
	g.start_game()		
