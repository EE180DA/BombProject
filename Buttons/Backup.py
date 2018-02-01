import mraa
import time

class Buttons:
	def __init__(self):
		d0 = mraa.Gpio(0)
		d1 = mraa.Gpio(1)
		d2 = mraa.Gpio(2)
		d3 = mraa.Gpio(3)
		d4 = mraa.Gpio(4)
		d5 = mraa.Gpio(5)
		d6 = mraa.Gpio(6)
		d7 = mraa.Gpio(7)

		#d2.dir(mraa.DIR_IN)
		#d3.dir(mraa.DIR_IN)
		#d4.dir(mraa.DIR_IN)
		#d5.dir(mraa.DIR_IN)
		#d6.dir(mraa.DIR_IN)
		PlayerSequence = [0, 0, 0, 0, 0, 0, 0]
		CorrectSequence = [0, 1, 2, 3, 4, 5, 6, 7]
		Buttons = [0, 0, 0, 0, 0, 0, 0]

	def getValues(self):
		self.d0 = mraa.Gpio(0)
		self.d1 = mraa.Gpio(1)
		self.d2 = mraa.Gpio(2)
		self.d3 = mraa.Gpio(3)
		self.d4 = mraa.Gpio(4)
		self.d5 = mraa.Gpio(5)
		self.d6 = mraa.Gpio(6)
		self.d7 = mraa.Gpio(7)
		self.Buttons = [self.d0.read(), self.d1.read(), self.d2.read(), self.d3.read(), 
						self.d4.read(), self.d5.read(), self.d6.read(), self.d7.read()]


	def startGame(self):
		while True:
			for i in range(0,7):
				getValues();
				if sum(Buttons) == 1:
					for j in range (0,7):
						if Buttons(j) == 1:
							PlayerSequence(i) = j
							break
					continue



				

if __name__ == '__main__':
	g = Buttons()
	while True:
		g.getValues()
		time.sleep(0.4)
