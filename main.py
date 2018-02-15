
import time
from random import shuffle
import threading
import thread
from ImageRecognition.detectShapes import DetectShapes
import sys
import os
import webbrowser
from VoiceRecog.speech import SpeechRecognition
from Display.screen import Display
from Server.server_test import Server
from PositionLocalization.localize import Localize
from Buzzer.Buzzer import Buzzer

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
		self.wire_thread = threading.Thread(target = self.wire_server_code, args = ())
		self.gesture_thread = threading.Thread(target = self.gesture_server_code, args = ())
		self.display_thread = threading.Thread(target = self.display_server_code, args = ())
		self.thread.daemon = True
		self.wire_thread.daemon = True
		self.gesture_thread.daemon = True
		self.display_thread.daemon = True
		self.topText = ""
		self.prevTopText = ""
		self.botText = ""
		self.prevBotText = ""
		self.lcd = Display()
		self.buzzer = Buzzer()
		self.write_top("")
		self.write_bot("")
		self.server_gesture = Server(0)
		self.server_wire = Server(1)
		self.server_display = Server(2)

	def kill(self):
		del self

	def write_top(self, text):
		self.prevTopText = self.topText
		self.topText = self.lcd.write_top(text)

	def write_bot(self, text):
		self.prevBotText = self.botText
		self.botText = self.lcd.write_bot(text)

	def get_difficulty(self):
		print "Difficulty level: " + str(self.difficulty)
		self.write_top("Difficulty level: " + str(self.difficulty))
		return self.difficulty

	def get_time(self):
		print "\nTime left: " + str(int(self.timeleft))
		self.write_bot("\nTime left: " + str(int(self.timeleft)))
		return int(self.timeleft)

	def penalize(self):
		self.time = self.time - self.difficulty*5
		self.lcd.flash(1, r)
		self.buzzer.play("wrong")

	def correct(self):
		self.lcd.flash(1, g)
		self.buzzer.play("right")

	def success(self):
		self.lcd.flash(2, g)
		

	def explode(self):
		print "BOOM!"
		self.write_top("BOOOOM!!")
		self.write_bot("")
		self.lcd.flash(5)
		webbrowser.open("https://www.youtube.com/watch?v=wdXU4R8JBe4", new=0, autoraise=True)
		thread.interrupt_main()
		sys.exit(0)

	def wire_server_code(self):
		self.server_wire.start_server("")

	def gesture_server_code(self):
		self.server_gesture.start_server("")

	def display_server_code(self):
		self.server_display.start_server("")

	def write_top2(self, text):
		message = 't'+text
		self.server_display.send(message)

	def write_bot2(self, text):
		message = 'b'+text
		self.server_display.send(message)

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
		print "Move to defusal area!"
		l = Localize()
		result = l.find(10)
		if result == "boom":
			self.explode
		elif result == color:
			print "Passed"		

	def intro(self):
		print "Welcome to the bomb defusal training module!"
		self.write_top("Welcome!")
		time.sleep(3)
		print "You have chose the difficulty level: " + str(self.difficulty)
		self.write_top("Difficulty: " + str(self.difficulty))
		time.sleep(1)
		print "That means you have exactly " + str(self.time) + "s to defuse this bomb!"
		self.write_top("You have " + str(self.time) + "s")
		time.sleep(2)
		print "I hope you are ready because it's about to get intense in here!"
		time.sleep(3)
		print "3"
		self.write_top("3")
		time.sleep(1)
		print "2"
		self.write_top("2")
		time.sleep(1)
		print "1"
		self.write_top("1")
		time.sleep(1)
		print "0"
		self.write_top("0")

	def start_game(self):
		self.intro()
		currGame = 1
		self.thread.start()
		self.wire_thread.start()
		self.gesture_thread.start()
		self.display_thread.start()

		self.move(red)
		
		while(not self.complete and self.timeleft > 0):
				#Also write new time to LCD screen

			print "\nTime to play: " + self.minigames[0]
			result = self.start_minigame(self.minigames[0])
			if result == 1:
				print "Congratulations you passed the first level"
				self.write_top("Passed")
				time.sleep(0.5)

			print "\nTime to play: " + self.minigames[1]
			result = self.start_minigame(self.minigames[1])
			if result == 1:
				print "Congratulations you passed the second level"	
				self.write_top("Passed")
				time.sleep(0.5)

			print "\nTime to play: " + self.minigames[2]
			result = self.start_minigame(self.minigames[2])
			if result == 1:
				print "Congratulations you passed the third level"
				self.write_top("Passed")
				time.sleep(0.5)

			print "\nTime to play: " + self.minigames[3]
			result = self.start_minigame(self.minigames[3])
			if result == 1:
				print "Congratulations you passed the fourth level"
				self.write_top("Passed")
				time.sleep(0.5)
			print "\nTime to play: " + self.minigames[4]
			result = self.start_minigame(self.minigames[4])
			if result == 1:
				print "Congratulations you passed the last level"
				self.write_top("Passed")
				time.sleep(0.5)
			self.complete = True


		if self.timeleft == 0:
			print "BOOM"
			self.write_top("BOOOOM!!")
			self.write_bot("")
			self.lcd.flash(5)
		else:
			print "Congratulations you've defused the bomb"
			self.write_top("Congratulations!")
			self.lcd.flash(5)

	def get_minigames(self):
		print '[%s]'%', '.join(map(str, self.minigames))
		return self.minigames

	def start_minigame(self, game_name):
		result = 0
		if game_name == "images":
			return image_game()

		elif game_name == "buttons":
			self.write_top("Buttons")
			self.server_wire.send("B1")
			while True:

			time.sleep(5)

		elif game_name == "gestures":
			self.write_top("Gestures")
			self.write_bot("NOD!!")
			while result == 0:
				result = self.server_gesture.start_server("1234")
				if result == 0:
					self.time -= self.errorPenalty
					self.write_top("Error")
					print "Error!"
					time.sleep(1)
					self.write_top("Gestures")

		elif game_name == "voice":
			self.write_top("Voice")
			self.write_bot("ORANGE")
			v = SpeechRecognition()
			result = v.startrecording(2)

		elif game_name == "wirecutting":
			self.write_top("Wirecutting")
			self.write_bot("Cut Blk-Blk")
			while result == 0:
				result = self.server_wire.start_server("BlBl")
				if result == 0:
					self.time -= self.errorPenalty
					self.write_top("Error")
					print "Error! You failed"
					time.sleep(1)
					self.write_top("Wirecutting")
			
		return result	

	def image_game(self):
		self.write_top("Images")
		d = DetectShapes()
		print "Draw a " + d.get_target_color() + ' ' + d.get_target_shape() + "!"
		if difficulty == 1:
			self.write_top2
		#Add morse code here for harder difficulty
		result = d.start_minigame()
		return result

	def buttons_game(self):
		msg = "B"+str(self.difficulty)
		self.server_wire.send(msg)
		while(server_wire.get_result() != 2):
			result = server_wire.get_result()
			if(result == 0):
				self.penalize()
			if(result == 1):




if __name__ == '__main__':
	g = GameInstance()
	g.get_minigames()
	g.start_game()		
