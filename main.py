import time
from random import shuffle
import threading
import thread
from ImageRecognition.detectShapes import DetectShapes
import sys
import os
import webbrowser
class GameInstance:

	def __init__(self, diff = -1):
		while diff < 1 or diff > 3:
			diff = raw_input("Please choose a difficulty level (1-3): ")
			diff = int(diff)
		self.difficulty = diff
		self.time = 240/self.difficulty #time left in seconds
		self.timeleft = self.time+3
		
		self.complete = False
		self.minigames = ['buttons', 'images', 'gestures', 'voice']
		shuffle(self.minigames)
		self.minigames.append('wirecutting')
		self.thread = threading.Thread(target = self.timer, args = ())
		self.thread.daemon = True


	def kill(self):
		del self

	def get_difficulty(self):
		print "Difficulty level: " + str(self.difficulty)
		return self.difficulty

	def get_time(self):
		print "\nTime left: " + str(int(self.timeleft))
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
				webbrowser.open("https://www.youtube.com/watch?v=wdXU4R8JBe4", new=0, autoraise=True)
				thread.interrupt_main()
				sys.exit(0)


	def intro(self):
		print "Welcome to the bomb defusal training module!"
		time.sleep(3)
		print "You have chose the difficulty level: " + str(self.difficulty)
		time.sleep(1)
		print "That means you have exactly " + str(self.time) + "s to defuse this bomb!"
		time.sleep(2)
		print "I hope you are ready because it's about to get intense in here!"
		time.sleep(3)
		print "3"
		time.sleep(1)
		print "2"
		time.sleep(1)
		print "1"
		time.sleep(1)
		print "0"

	def start_game(self):
		self.intro()
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
		if game_name == "images":
			print "Draw a black triangle!"
			d = DetectShapes()
			result = d.start_minigame()
		elif game_name == "buttons":
			result = 1
			time.sleep(5)
		elif game_name == "gestures":	
			result = 1
			time.sleep(5)
		elif game_name == "voice":	
			result = 1
			time.sleep(5)
		elif game_name == "wirecutting":
			result = 1
			time.sleep(5)
		return result	


if __name__ == '__main__':
	g = GameInstance()
	g.get_minigames()
	g.start_game()