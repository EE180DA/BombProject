
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
		self.errorPenalty = 5*self.difficulty
		self.minigames = ['buttons', 'images', 'gestures', 'voice']
		self.move_time = 30/self.difficulty
		shuffle(self.minigames)
		self.minigames.append('wirecutting')
		self.thread = threading.Thread(target = self.timer, args = ())
		self.wire_thread = threading.Thread(target = self.wire_server_code, args = ())
		self.gesture_thread = threading.Thread(target = self.gesture_server_code, args = ())
		self.display_thread = threading.Thread(target = self.display_server_code, args = ())
		self.buzz_thread = threading.Thread(target = self.buzz, args = ())
		self.thread.daemon = True
		self.wire_thread.daemon = True
		self.gesture_thread.daemon = True
		self.display_thread.daemon = True
		self.buzz_thread.daemon = True
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
		self.time = self.time - self.errorPenalty
		self.lcd.flash(1, r)
		self.buzzer.play("wrong")

	def correct(self):
		self.lcd.flash(1, g)
		self.buzzer.play("right")

	def success(self):
		self.lcd.flash(2, g)
		self.buzzer.play("win")

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

	def flash_morse(self, text):
		message = 'm'+text
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


	def buzz(self):
		while self.timeleft > 0:
			if timeleft > 90:
				sleeptime = 1
			elif timeleft > 60:
				sleeptime = 0.7
			elif timeleft > 20:
				sleeptime = 0.5
			elif timeleft > 10:
				sleeptime = 0.3
			else:
				sleeptime = 0.1
			self.buzzer.play("beep")
			time.sleep(sleeptime)

	def move(self, color):
		print "Move to defusal area!"
		self.write_top("Move to {}!".format(color))
		l = Localize()
		result = l.find(self.move_time)
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
		self.buzz_thread.start()
		self.move(red)
		
		print "\nTime to play: " + self.minigames[0]
		result = self.start_minigame(self.minigames[0])
		print "Congratulations you passed the first level"
		self.write_top("Passed")
		time.sleep(0.5)

		print "\nTime to play: " + self.minigames[1]
		result = self.start_minigame(self.minigames[1])
		print "Congratulations you passed the second level"	
		self.write_top("Passed")
		time.sleep(0.5)

		print "\nTime to play: " + self.minigames[2]
		result = self.start_minigame(self.minigames[2])
		print "Congratulations you passed the third level"
		self.write_top("Passed")
		time.sleep(0.5)

		print "\nTime to play: " + self.minigames[3]
		result = self.start_minigame(self.minigames[3])
		print "Congratulations you passed the fourth level"
		self.write_top("Passed")
		time.sleep(0.5)

		print "\nTime to play: " + self.minigames[4]
		result = self.start_minigame(self.minigames[4])
		print "Congratulations you passed the last level"
		self.write_top("Passed")
		time.sleep(0.5)

		print "Congratulations you've defused the bomb"
		self.write_top("Congratulations!")
		self.lcd.flash(5)


	def get_minigames(self):
		print '[%s]'%', '.join(map(str, self.minigames))
		return self.minigames

	def start_minigame(self, game_name):
		if game_name == "images":
			image_game()

		elif game_name == "buttons":
			self.write_top("Buttons")
			buttons_game()

		elif game_name == "gestures":
			self.write_top("Gestures")
			gestures_game()

		elif game_name == "wirecutting":
			self.write_top("Wirecutting")
			wires_game()
				

	def image_game(self):
		self.write_top("Images")
		d = DetectShapes()
		shape = d.get_target_color()
		color = d.get_target_shape()
		shape_morse = d.get_shape_morse()
		color_morse = d.get_color_morse()
		print "Draw a " + color + ' ' + shape + "!"
		if self.difficulty == 1:
			self.write_top2("Draw a")
			self.write_bot2("{} {}".format(color, shape))
		elif self.difficulty == 2:
			self.write_top2("Shape: {}".format(shape_morse))
			self.write_bot2("Color: {}".format(color_morse))
		else:
			self.flash_morse("{} {}".format(color_morse, shape_morse))
		d.start_minigame()
		if self.difficulty == 3:
			self.server_display.send("#")
		self.success()
		

	def buttons_game(self):
		msg = "B"+str(self.difficulty)
		self.server_wire.send(msg)
		while(server_wire.get_result() != 2):
			result = server_wire.get_result()
			if(result == 0):
				self.penalize()
			if(result == 1):
				self.correct()
			else:
				self.write_top2(result)
		self.success()
		
	def gestures_game(self):
		msg = "G"+str(self.difficulty)
		self.server_gesture.send(msg)
		while(server_gesture.get_result() != 2):
			result = server_gesture.get_result()
			if(result == 0):
				self.penalize()
			if(result == 1):
				self.correct()
			else:
				self.write_top2(result)
		self.success()

	def wires_game(self):
		msg = "W"+str(self.difficulty)
		self.server_wire.send(msg)
		while(server_wire.get_result() != 2):
			result = server_wire.get_result()
			if(result == 0):
				self.penalize()
			if(result == 1):
				self.correct()
			else:
				self.write_top2(result)
		self.success()




if __name__ == '__main__':
	g = GameInstance()
	g.get_minigames()
	g.start_game()		
