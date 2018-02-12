import mraa
import time
from random import randint

class Buttons:
	def __init__(self, diff):
		self.d0 = mraa.Gpio(0)
		self.d1 = mraa.Gpio(1)
		self.d2 = mraa.Gpio(2)
		self.d3 = mraa.Gpio(3)
		self.d4 = mraa.Gpio(4)
		self.d5 = mraa.Gpio(5)
		self.d6 = mraa.Gpio(6)
		self.d7 = mraa.Gpio(7)
		self.CorrectSequence = [0, 0, 0, 0, 0, 0, 0, 0]
		self.CheckSequence = [0, 1, 2, 3, 4, 5, 6, 7]
		self.ScreenDisplay = [0, 0, 0, 0, 0, 0, 0, 0]
		self.StageSequence = randint(1, 4)
		self.difficulty = diff
		self.setCorrectSequence(diff, 4)#self.StageSequence)
		
	#Sets correct button sequence based on the difficulty -
	# -and randomly generated stage sequence
	def setCorrectSequence(self, diff, stage_seq):
		if diff == 0: #Easy
			self.CorrectSequence = [1, 5, 3, 0, 4, 6, 7, 2]
		elif diff == 1: #Medium
			if stage_seq == 1: #Stage Display numbers 3, 1, 4
				self.CorrectSequence = [1, 2, 0, 7, 8, 8, 8, 8]
				self.ScreenDisplay = [3, 1, 4, 4, 8, 8, 8, 8]
			elif stage_seq == 2: #Stage Display numbers 2, 4, 1
				self.CorrectSequence = [6, 4, 5, 4, 8, 8, 8, 8]
				self.ScreenDisplay = [2, 4, 1, 1, 8, 8, 8, 8]
			elif stage_seq == 3: #Stage Display numbers 1, 4, 3
				self.CorrectSequence = [3, 4, 3, 1, 8, 8, 8, 8]
				self.ScreenDisplay = [1, 4, 3, 3, 8, 8, 8, 8]
			elif stage_seq == 4: #Stage Display numbers 4, 3, 2
				self.CorrectSequence = [0, 1, 3, 5, 8, 8, 8, 8]
				self.ScreenDisplay = [4, 3, 2, 2, 8, 8, 8, 8]
		elif diff == 2: #Hard
			if stage_seq == 1: #Stage Display numbers 3, 1, 4, 2, 2 CHECKED
				self.CorrectSequence = [1, 2, 0, 7, 3, 6, 0, 6]
				self.ScreenDisplay = [3, 1, 4, 4, 8, 8, 8, 8]
			elif stage_seq == 2: #Stage Display numbers 2, 4, 1, 3, 3 CHECKED
				self.CorrectSequence = [6, 4, 5, 4, 6, 1, 6, 6]
				self.ScreenDisplay = [2, 4, 1, 1, 3, 3, 3, 3]
			elif stage_seq == 3: #Stage Display numbers 1, 4, 3, 2, 4 CHECKED
				self.CorrectSequence = [3, 4, 3, 1, 5, 6, 1, 5]
				self.ScreenDisplay = [1, 4, 3, 3, 2, 2, 4, 4]
			elif stage_seq == 4: #Stage Display numbers 4, 3, 2, 1, 4 CHECKED
				self.CorrectSequence = [0, 1, 3, 5, 1, 4, 5, 1]
				self.ScreenDisplay = [4, 3, 2, 2, 1, 1, 4, 4]
	def startGame(self):
		i = 0
		while i < 8:
			print "Correct button:", self.CorrectSequence[i]+1
			print "Screen display number:", self.ScreenDisplay[i]
			x = self.CorrectSequence[i]
			#if medium difficiulty, only 4 button presses are required
			if self.difficulty == 1:
				if i >= 4:
					break			
			while True:
				#if correct button is pressed, move on to next iteration of i (next stage)
				if mraa.Gpio(self.CorrectSequence[i]).read() == 1:
					print "Next Stage"
					time.sleep(0.5)
					i = i + 1
					break
				time.sleep(0.2)
				#if incorrect button is pressed, reset back to the first stage (subtract time if needed)
				if mraa.Gpio(self.CheckSequence[(x+9)%8]).read() == 1 or mraa.Gpio(self.CheckSequence[(x+10)%8]).read() == 1 or mraa.Gpio(self.CheckSequence[(x+11)%8]).read() == 1 or \
					mraa.Gpio(self.CheckSequence[(x+12)%8]).read() == 1 or mraa.Gpio(self.CheckSequence[(x+13)%8]).read() == 1 or mraa.Gpio(self.CheckSequence[(x+14)%8]).read() == 1 or \
					mraa.Gpio(self.CheckSequence[(x+15)%8]).read() == 1:
					print "Incorrect Answer, Stage Reset"
					i = 0
					time.sleep(0.5)
					break
		print "Success"
		return (1)

if __name__ == '__main__':
	g = Buttons(1)
	g.startGame()