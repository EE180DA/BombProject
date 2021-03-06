import mraa
import random
import time

class WireCutting:
	def __init__(self, diff):
		#random.seed()
		#self.RANDGEN = random.randint(0,4)
		self.difficulty = diff
		#flags for cut wire

	def getValues(self):
		self.a0 = mraa.Aio(0)
		self.a1 = mraa.Aio(1)
		self.a2 = mraa.Aio(2)
		self.a3 = mraa.Aio(3)
		self.a4 = mraa.Aio(4)


	def startGame(self):



		if RANDGEN == 0:
			print "Cut the RED + RED wire!"
			while True:
				if self.a0.read() < 160:
					print "SUCCESS"
					return(1)
				elif self.a1.read() < 160 or self.a2.read() < 160 or self.a3.read() < 160 or self.a4.read() < 160:
					print "FAILURE"
					return(0)
		elif RANDGEN == 1:
			print "Cut the BROWN + GREEN wire!"
			while True:
				self.getValues()
				if self.a1.read() < 160:
					print "SUCCESS"
					return(1)
				elif self.a0.read() < 160 or self.a2.read() < 160 or self.a3.read() < 160 or self.a4.read() < 160:
					print "FAILURE"
					return(0)
		elif RANDGEN == 2:
			print "Cut the BLACK + BLACK wire!"
			while True:
				self.getValues()
				if self.a2.read() < 160:
					print "SUCCESS"
					return(1)
				elif self.a1.read() < 160 or self.a0.read() < 160 or self.a3.read() < 160 or self.a4.read() < 160:
					print "FAILURE"
					return(0)
		elif RANDGEN == 3:
			print "Cut the BROWN + BLUE wire!"
			while True:
				self.getValues()
				if self.a3.read() < 160:
					print "SUCCESS"
					return(1)
				elif self.a1.read() < 160 or self.a2.read() < 160 or self.a0.read() < 160 or self.a4.read() < 160:
					print "FAILURE"
					return(0)
		elif RANDGEN == 4:
			print "Cut the RED + WHITE wire!"
			while True:
				self.getValues()
				if self.a4.read() < 160:
					print "SUCCESS"
					return(1)
				elif self.a1.read() < 160 or self.a2.read() < 160 or self.a3.read() < 160 or self.a0.read() < 160:
					print "FAILURE"
					return(0)

if __name__ == '__main__':
	g = WireCutting()
	#g.startGame(1)

	t = WireCutting()
	while True:
		t.getValues()
		print t.a0.read()
		print t.a1.read()
		print t.a2.read()
		print t.a3.read()
		print t.a4.read()