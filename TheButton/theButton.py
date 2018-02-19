import mraa
from VoiceRecog.speech import SpeechRecognition
import time

class TheButton:
	def __init__(self):
		self.pin = mraa.Gpio(8)
		self.difficulty = 1
		self.button_time = 5

	def start(self):
		timeout_start = time.time()
		#5 seconds to press the red button to initiate bonus sequence
		while time.time() < timeout_start + self.button_time:
			if self.pin.read() == 1:
				g = SpeechRecognition()
				result = g.start_bonus()
				return result
		return(0)
		#result = 0:no bonus, 1:add score, 2:add time

	def select_difficulty(self):
		#select difficulty level, hold less than 3 seconds for easy, 4-5 for medium, longer for hard
		while True:
			if self.pin.read() == 1:
				time_start = time.time()
				while self.pin.read() == 1:
					if time.time() - time_start < 3:
						#easy
						self.difficulty = 1
						print("Easy")
					elif time.time()-time_start < 5:
						#medium
						self.difficulty = 2
						print("Medium")
					elif time.time()-time_start < 7:
						#hard
						self.difficulty = 3
						print("Hard")
					else:
						#loop back
						time_start = time.time()
					time.sleep(0.3)
				break
			time.sleep(0.2)
		return self.difficulty


if __name__ == '__main__':
	b = theButton()
	result = b.select_difficulty()
	print result
