
import time
from random import shuffle
import threading
import thread
from ImageRecognition.detectShapes import DetectShapes
import sys
import os
import webbrowser
from WireCutting.WireCutting import WireCutting
from VoiceRecog.speech import SpeechRecognition
from Display.screen import Display
from Server.server import Server
from PositionLocalization.localize import Localize

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
		self.move_time = 120/self.difficulty
		shuffle(self.minigames)
		self.minigames.append('wirecutting')
		self.thread = threading.Thread(target = self.timer, args = ())
		self.thread.daemon = True
		self.topText = ""
		self.prevTopText = ""
		self.botText = ""
		self.prevBotText = ""
		self.lcd = Display()
        		self.writeTop("")
                self.writeBot("")
       			self.server_gesture = Server(0)
        		self.server_wire = Server(1)

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

	def explode(self):
		print "BOOM!"
		self.writeTop("BOOOOM!!")
		self.writeBot("")
		self.lcd.flash(5)
		webbrowser.open("https://www.youtube.com/watch?v=wdXU4R8JBe4", new=0, autoraise=True)
		thread.interrupt_main()
		sys.exit(0)

	def timer(self):
		startTime = int(time.time())
		oldtimeleft = self.timeleft
		while True:
			timeDiff = int(time.time()) - startTime
			self.timeleft = self.time - timeDiff
			self.get_time()
			time.sleep(1)
			if(self.timeleft <= 0):
				self.explode()

	def move(self, color):
		l = Localize()
		result = l.find(10)
		if result == "boom":
			self.explode
		elif result == color:
			print "Passed"		

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
		self.intro()
		currGame = 1
		self.thread.start()
		self.move(red)
		print "Move to first defusal area!"
		result = l.find(10)
		if result == "boom":
			print "BOOM"
                        # self.writeTop("BOOOOM!!")
                        # self.writeBot("")
                        # self.lcd.flash(5)
        elif result == "red":
        	print "Passed"

		while(not self.complete and self.timeleft > 0):
				#Also write new time to LCD screen

			print "\nTime to play: " + self.minigames[0]
			result = self.start_minigame(self.minigames[0])
			if result == 1:
				print "Congratulations you passed the first level"
                                
                                self.writeTop("Passed")
                                time.sleep(0.5)

			print "\nTime to play: " + self.minigames[1]
			result = self.start_minigame(self.minigames[1])
			if result == 1:
				print "Congratulations you passed the second level"	
                                
                                self.writeTop("Passed")
                                time.sleep(0.5)

			print "\nTime to play: " + self.minigames[2]
			result = self.start_minigame(self.minigames[2])
			if result == 1:
				print "Congratulations you passed the third level"
                                
                                self.writeTop("Passed")
                                time.sleep(0.5)

			print "\nTime to play: " + self.minigames[3]
			result = self.start_minigame(self.minigames[3])
			if result == 1:
				print "Congratulations you passed the fourth level"
                                
                                self.writeTop("Passed")
                                time.sleep(0.5)
			print "\nTime to play: " + self.minigames[4]
			result = self.start_minigame(self.minigames[4])
			if result == 1:
				print "Congratulations you passed the last level"                               
                                self.writeTop("Passed")
                                time.sleep(0.5)
			self.complete = True


		if self.timeleft == 0:
			print "BOOM"
                        self.writeTop("BOOOOM!!")
                        self.writeBot("")
                        self.lcd.flash(5)
		else:
			print "Congratulations you've defused the bomb"
                        self.writeTop("Congratulations!")
                        self.lcd.flash(5)

	def get_minigames(self):
		print '[%s]'%', '.join(map(str, self.minigames))
		return self.minigames

	def start_minigame(self, game_name):
		result = 0
		if game_name == "images":
                        self.writeTop("Images")
			d = DetectShapes()
			print "Draw a " + d.get_target_color() + ' ' + d.get_target_shape() + "!"
			result = d.start_minigame()
		elif game_name == "buttons":
                        self.writeTop("Buttons")
			result = 1
			time.sleep(5)

		elif game_name == "gestures":
                        self.writeTop("Gestures")
                        self.writeBot("NOD!!")
                        while result == 0:
            	            result = self.server_gesture.start_server("1234")
			    if result == 0:
					self.time -= self.errorPenalty
					self.writeTop("Error")
					print "Error!"
					time.sleep(1)
					self.writeTop("Gestures")

		elif game_name == "voice":
                        self.writeTop("Voice")
                        self.writeBot("ORANGE")
			v = SpeechRecognition()
			result = v.startrecording(2)

		elif game_name == "wirecutting":
                        self.writeTop("Wirecutting")
                        self.writeBot("Cut Blk-Blk")
						while result == 0:
            	            result = self.server_wire.start_server("BlBl")
			    if result == 0:
					self.time -= self.errorPenalty
					self.writeTop("Error")
					print "Error! You failed"
					time.sleep(1)
					self.writeTop("Wirecutting")
			
			
		return result	


if __name__ == '__main__':
	g = GameInstance()
	g.get_minigames()
	g.start_game()		
