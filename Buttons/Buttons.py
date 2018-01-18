import mraa
import time

class Buttons:
	def __init__(self):
		d2 = mraa.Gpio(2)
		d3 = mraa.Gpio(4)
		d4 = mraa.Gpio(7)
		d5 = mraa.Gpio(8)
		d6 = mraa.Gpio(12)
		#d2.dir(mraa.DIR_IN)
		#d3.dir(mraa.DIR_IN)
		#d4.dir(mraa.DIR_IN)
		#d5.dir(mraa.DIR_IN)
		#d6.dir(mraa.DIR_IN)

	def getValues(self):
		self.d2 = mraa.Gpio(2)
		self.d3 = mraa.Gpio(4)
		self.d4 = mraa.Gpio(7)
		self.d5 = mraa.Gpio(8)
		self.d6 = mraa.Gpio(12)
		print "D2: ", self.d2.read()
		print "D3: ", self.d3.read()
		print "D4: ", self.d4.read()
		print "D5: ", self.d5.read()
		print "D6: ", self.d6.read()

	def startGame(self):
		while True:
			self.getValues()
			#FIRST button press
			if self.d2.read() == 1:
				while True:
					self.getValues()
					#SECOND button press
					if self.d3.read() == 1:
						while True:
							self.getValues()
							#THIRD button press
							if self.d4.read() == 1:
								while True:
									self.getValues()
									#FOURTH button press
									if self.d5.read() == 1:
										while True:
											self.getValues()
											#FIFTH button press
											if self.d6.read() == 1:
												print "SUCCESS!"
												return(1)
											elif self.d2.read() == 1 or self.d3.read() == 1 or self.d4.read() == 1 or self.d5.read() == 1:
												print "FALIURE!"
												return(0)
									elif self.d2.read() == 1 or self.d3.read() == 1 or self.d4.read() == 1 or self.d6.read() == 1:
										print "FAILURE!"
										return(0)
							elif self.d2.read() == 1 or self.d3.read() == 1 or self.d5.read() == 1 or self.d6.read() == 1:
								print "FAILURE!"
								return(0)
					elif self.d2.read() == 1 or self.d6.read() == 1 or self.d4.read() == 1 or self.d5.read() == 1:
						print "FAILURE!"
						return(0)
			elif self.d6.read() == 1 or self.d3.read() == 1 or self.d4.read() == 1 or self.d5.read() == 1:
				print "FAILURE!"
				return(0)

if __name__ == '__main__':
	g = Buttons()
	while True:
		g.getValues()
		time.sleep(0.4)