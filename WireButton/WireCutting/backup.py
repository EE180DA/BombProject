import mraa
import random
import time

class WireCutting:
	def __init__(self, diff):
		#random.seed()
		#self.RANDGEN = random.randint(0,4)
		self.wiresDifficulty = diff
		self.wiresNum = 0
		self.wiresCorrect = [0, 0, 0, 0, 0]
		self.wiresCode = ""
		self.selectWiresDifficulty(self.wiresDifficulty)

		#flags for cut wire
		self.a0 = mraa.Aio(0)
		self.a1 = mraa.Aio(1)
		self.a2 = mraa.Aio(2)
		self.a3 = mraa.Aio(3)
		self.a4 = mraa.Aio(4)
		self.wiresFlags = [0, 0, 0, 0, 0]
		self.wiresa0 = 0
		self.wiresa1 = 0
		self.wiresa2 = 0
		self.wiresa3 = 0
		self.wiresa4 = 0

	def selectWiresDifficulty(self, diff):
		if diff == 0: #Easy
			self.wiresNum = 1
			self.wiresCorrect = [3, 0, 0, 0, 0]
		elif diff == 1: #Medium
			self.wiresNum = 3
			self.wiresCode = "e78gp"
			self.wiresCorrect = [4, 1, 3, 0, 0]
		elif diff == 2: #Hard
			self.wiresNum = 5
			self.wiresCode = "b3j9a"
			self.wiresCorrect = [2, 4, 0, 1, 3]

	def wiresReconnect(self):
		self.sendMessage("Incorrect Answer, Stage Reset")
		self.sendMessage("Reconnect Wires")
		print "Wrong"
		self.wiresa0 = 0
		self.wiresa1 = 0
		self.wiresa2 = 0
		self.wiresa3 = 0
		self.wiresa4 = 0
		self.wiresFlags = [0, 0, 0, 0, 0]
		j = 0
		while True:
			if self.a0.read() < 120 and self.a1.read() < 120 and self.a2.read() < 120 and self.a3.read() < 120 and self.a4.read() < 120:
				j = j + 1
				time.sleep(0.5)
				if j == 5:
					return(1)
			else:
				j = 0

	def startWiresGame(self):
		i = 0
		while i < self.wiresNum:
			if self.a0.read() > 120 and self.wiresa0 == 0:
				self.wiresFlags[i] = 0
				if self.wiresCorrect[i] != self.wiresFlags[i]:
					self.wiresReconnect()
					i = 0
				else:
					i = i + 1
					self.wiresa0 = 1
			if self.a1.read() > 120 and self.wiresa1 == 0:
				self.wiresFlags[i] = 1
				if self.wiresCorrect[i] != self.wiresFlags[i]:
					self.wiresReconnect()
					i = 0
				else:
					i = i + 1
					self.wiresa1 = 1
			if self.a2.read() > 120 and self.wiresa2 == 0:
				self.wiresFlags[i] = 2
				if self.wiresCorrect[i] != self.wiresFlags[i]:
					self.wiresReconnect()
					i = 0
				else:
					i = i + 1
					self.wiresa2 = 1
			if self.a3.read() > 120 and self.wiresa3 == 0:
				self.wiresFlags[i] = 3
				if self.wiresCorrect[i] != self.wiresFlags[i]:
					self.wiresReconnect()
					i = 0
				else:
					i = i + 1
					self.wiresa3 = 1
			if self.a4.read() > 120 and self.wiresa4 == 0:
				self.wiresFlags[i] = 4
				if self.wiresCorrect[i] != self.wiresFlags[i]:
					self.wiresReconnect()
					i = 0
				else:
					i = i + 1
					self.wiresa4 = 1
			print self.wiresFlags
			print i
			time.sleep(0.5)

if __name__ == '__main__':
	g = WireCutting(1)
	g.startWiresGame()
	# while True:
	#  	print "A0: ", mraa.Aio(0).read()
	#  	print "A1: ", mraa.Aio(1).read()
	#  	print "A2: ", mraa.Aio(2).read()
	#  	print "A3: ", mraa.Aio(3).read()
	#  	print "A4: ", mraa.Aio(4).read()
	#  	print " "
	#  	time.sleep(0.5)