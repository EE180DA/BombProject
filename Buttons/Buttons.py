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

	def getValues(self):
		self.d0 = mraa.Gpio(0)
		self.d1 = mraa.Gpio(1)
		self.d2 = mraa.Gpio(2)
		self.d3 = mraa.Gpio(3)
		self.d4 = mraa.Gpio(4)
		self.d5 = mraa.Gpio(5)
		self.d6 = mraa.Gpio(6)
		self.d7 = mraa.Gpio(7)

	def startGame(self):
		buttonOrder = [0, 1, 2, 3, 4, 5, 6, 7]
		for i in range (0,8):
			flag = 0
			while flag == 0:
				if mraa.Gpio(buttonOrder[i]).read() == 1:
					print "Next"
					time.sleep(0.5)
					flag = 1
				elif mraa.Gpio(buttonOrder[(i+9)%8]).read() == 1 or mraa.Gpio(buttonOrder[(i+10)%8]).read() == 1 or mraa.Gpio(buttonOrder[(i+11)%8]).read() == 1 \
					or mraa.Gpio(buttonOrder[(i+12)%8]).read() == 1 or mraa.Gpio(buttonOrder[(i+13)%8]).read() == 1 or mraa.Gpio(buttonOrder[(i+14)%8]).read() == 1 \
					or mraa.Gpio(buttonOrder[(i+15)%8]).read() == 1:
					print "Boom!"
					time.sleep(0.5)
					flag = 1
					return (0)
		print "Success"
		return (1)

if __name__ == '__main__':
	g = Buttons()
	g. startGame()