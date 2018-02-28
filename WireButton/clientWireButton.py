import socket
import time
import mraa
from random import randint

class Client:
	def __init__(self):
		# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# client.connect((target, port))
		self.client.connect(('192.168.42.1', 3999))

		#Button Inits
		#random.seed()
		self.buttonCorrectSequence = [0, 0, 0, 0, 0, 0, 0, 0]
		self.buttonCheckSequence = [0, 1, 2, 3, 4, 5, 6, 7]
		self.buttonScreenDisplay = [0, 0, 0, 0, 0, 0, 0, 0]
		self.StageSequence = 0
		self.button_diff = 0

		#Wire Inits
		self.wiresDifficulty = 0
		self.wiresNum = 0
		self.wiresCorrect = [0, 0, 0, 0, 0]
		self.wiresCode = ""
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

	def startClient(self):
		# connect the client
		while True:
			received = self.client.recv(4096)
			print received
                        if received == "":
                            time.sleep(1)
                            continue
			# Codewords for minigames
			if received == "B1":
				self.button_diff = 0
				return(0)
			elif received == "B2":
				self.button_diff = 1
				return(1)
			elif received == "B3":
				self.button_diff = 2
				return(2)
			elif received == "W1":
				self.wiresDifficulty = 0
				return(3)
			elif received == "W2":
				self.wiresDifficulty = 1
				return(4)
			elif received == "W3":
				self.wiresDifficulty = 2
				return(5)
		
	def sendMessage(self, message):
		self.client.send(message)
		while True:
			received = self.client.recv(4096)
			time.sleep(0.3)
			if received == "ACK":
				print "Acknowledged"
				break
			else:
				print('Message not sent')
				self.client.send(message)
		print "Sent:", message

	def endClient(self):
		self.client.close()

	def setbuttonCorrectSequence(self, diff, stage_seq):
		if diff == 0: #Easy
			self.buttonCorrectSequence = [1, 5, 3, 0, 4, 6, 7, 2]
		elif diff == 1: #Medium
			if stage_seq == 1: #Stage Display numbers 3, 1, 4
				self.buttonCorrectSequence = [1, 2, 0, 7, 8, 8, 8, 8]
				self.buttonScreenDisplay = [3, 1, 4, 4, 8, 8, 8, 8]
			elif stage_seq == 2: #Stage Display numbers 2, 4, 1
				self.buttonCorrectSequence = [6, 4, 5, 4, 8, 8, 8, 8]
				self.buttonScreenDisplay = [2, 4, 1, 1, 8, 8, 8, 8]
			elif stage_seq == 3: #Stage Display numbers 1, 4, 3
				self.buttonCorrectSequence = [3, 4, 3, 1, 8, 8, 8, 8]
				self.buttonScreenDisplay = [1, 4, 3, 3, 8, 8, 8, 8]
			elif stage_seq == 4: #Stage Display numbers 4, 3, 2
				self.buttonCorrectSequence = [0, 1, 3, 5, 8, 8, 8, 8]
				self.buttonScreenDisplay = [4, 3, 2, 2, 8, 8, 8, 8]
		elif diff == 2: #Hard
			if stage_seq == 1: #Stage Display numbers 3, 1, 4, 2, 2 CHECKED
				self.buttonCorrectSequence = [1, 2, 0, 7, 3, 6, 0, 6]
				self.buttonScreenDisplay = [3, 1, 4, 4, 2, 2, 2, 2]
			elif stage_seq == 2: #Stage Display numbers 2, 4, 1, 3, 3 CHECKED
				self.buttonCorrectSequence = [6, 4, 5, 4, 6, 1, 6, 6]
				self.buttonScreenDisplay = [2, 4, 1, 1, 3, 3, 3, 3]
			elif stage_seq == 3: #Stage Display numbers 1, 4, 3, 2, 4 CHECKED
				self.buttonCorrectSequence = [3, 4, 3, 1, 5, 6, 1, 5]
				self.buttonScreenDisplay = [1, 4, 3, 3, 2, 2, 4, 4]
			elif stage_seq == 4: #Stage Display numbers 4, 3, 2, 1, 4 CHECKED
				self.buttonCorrectSequence = [0, 1, 3, 5, 1, 4, 5, 1]
				self.buttonScreenDisplay = [4, 3, 2, 2, 1, 1, 4, 4]
				
	def startButtonGame(self):
		random.seed()
		self.StageSequence = randint(1,4)
		self.setbuttonCorrectSequence(self.button_diff, self.StageSequence)
		i = 0
		self.sendMessage(" "+str(self.buttonScreenDisplay[i]))
		while i < 8:
			print "Correct button:", self.buttonCorrectSequence[i]+1
			print "Screen display number:", self.buttonScreenDisplay[i]
			
			#Send screen2 display to server, dont send if end of game
			#if self.buttonScreenDisplay[i] != 8 and self.buttonScreenDisplay[i] != 0:
			#	self.sendMessage(str(self.buttonScreenDisplay[i]))

			x = self.buttonCorrectSequence[i]

			#if medium difficiulty, only 4 button presses are required
			if self.button_diff == 1 and i >= 4:
				break
			
			while True:
				#if correct button is pressed, move on to next iteration of i (next stage)
				if mraa.Gpio(self.buttonCorrectSequence[i]).read() == 1:
					print "Next Stage"
					i = i + 1
					if i == 8 or self.buttonScreenDisplay[i] == 8:
						break
					else:
						self.sendMessage("R"+str(self.buttonScreenDisplay[i]))
					time.sleep(0.5)
					break
				time.sleep(0.2)

				#if incorrect button is pressed, reset back to the first stage (subtract time if needed)
				if mraa.Gpio(self.buttonCheckSequence[(x+9)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+10)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+11)%8]).read() == 1 or \
					mraa.Gpio(self.buttonCheckSequence[(x+12)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+13)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+14)%8]).read() == 1 or \
					mraa.Gpio(self.buttonCheckSequence[(x+15)%8]).read() == 1:
					print "Incorrect Answer, Stage Reset"
					i = 0
					self.sendMessage("W"+str(self.buttonScreenDisplay[i]))
					time.sleep(0.5)
					break
		print "Success"
		return (1)

	def selectWiresDifficulty(self, diff):
		if diff == 0: #Easy
			self.wiresNum = 1
			self.wiresCorrect = [3, 0, 0, 0, 0]
		elif diff == 1: #Medium
			self.wiresNum = 3
			self.sendMessage("e78ip")
			self.wiresCorrect = [4, 1, 3, 0, 0]
		elif diff == 2: #Hard
			self.wiresNum = 5
			self.sendMessage("b3j9a")
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
					self.sendMessage("Resume Game")
					if self.wiresDifficulty == 1:
						self.sendMessage("e78ip")
					elif self.wiresDifficulty == 2:
						self.sendMessage("b3j9a")
					return(1)
			else:
				j = 0

	def startWiresGame(self):
		self.selectWiresDifficulty(self.wiresDifficulty)
		i = 0
		while i < self.wiresNum:
			print "Disconnect: ", self.wiresCorrect[i]
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
			time.sleep(0.5)
		print "Success"
		return(1)

if __name__ == '__main__':
	while True:
		try:
			g = Client() 
			c = g.startClient()
			break
		except KeyboardInterrupt:
			exit()
		except:
			print('Didnt connect')
			time.sleep(1)

	#Select difficulty

	# Start the buttons game
	if c >= 0 and c < 3:
		print "Starting Buttons game Difficulty:" , c
		response=g.startButtonGame()
		if response == 1:
			g.sendMessage("Success")
		else:
			g.sendMessage("Failure")

	#Start the wires game
	c = g.startClient()
	if c >= 3 and c < 6:
		print "Starting Wires game Difficulty:" , c
		response=g.startWiresGame()
		if response == 1:
			g.sendMessage("Success")
		else:
			g.sendMessage("Failure")
	
	g.endClient()
