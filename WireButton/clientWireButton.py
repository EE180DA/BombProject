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
		self.buttonCorrectSequence = [0, 0, 0, 0, 0, 0, 0, 0]
		self.buttonCheckSequence = [0, 1, 2, 3, 4, 5, 6, 7]
		self.buttonScreenDisplay = [0, 0, 0, 0, 0, 0, 0, 0]
		self.StageSequence = randint(1, 4)
		self.button_diff = 0
		

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
				return(3)
			elif received == "W2":
				return(4)
			elif received == "W3":
				return(5)
		

	def sendMessage(self, message):
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
				self.buttonScreenDisplay = [3, 1, 4, 4, 8, 8, 8, 8]
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
		self.setbuttonCorrectSequence(self.button_diff, 4)
		i = 0
		while i < 8:
			print "Correct button:", self.buttonCorrectSequence[i]+1
			print "Screen display number:", self.buttonScreenDisplay[i]
			#Send screen2 display to server
			self.sendMessage(str(self.buttonScreenDisplay[i]))
			x = self.buttonCorrectSequence[i]
			#if medium difficiulty, only 4 button presses are required
			if self.button_diff == 1:
				if i >= 4:
					break			
			while True:
				#if correct button is pressed, move on to next iteration of i (next stage)
				if mraa.Gpio(self.buttonCorrectSequence[i]).read() == 1:
					print "Next Stage"
					time.sleep(0.5)
					i = i + 1
					break
				time.sleep(0.2)
				#if incorrect button is pressed, reset back to the first stage (subtract time if needed)
				if mraa.Gpio(self.buttonCheckSequence[(x+9)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+10)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+11)%8]).read() == 1 or \
					mraa.Gpio(self.buttonCheckSequence[(x+12)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+13)%8]).read() == 1 or mraa.Gpio(self.buttonCheckSequence[(x+14)%8]).read() == 1 or \
					mraa.Gpio(self.buttonCheckSequence[(x+15)%8]).read() == 1:
					print "Incorrect Answer, Stage Reset"
					i = 0
					time.sleep(0.5)
					break
		print "Success"
		return (1)

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

	if c >= 0 and c < 3:
		print "Starting Buttons game Difficulty:" , c
		response=g.startButtonGame()
		if response == 1:
			g.sendMessage("Success")
		else:
			g.sendMessage("Failure")

	c = g.startClient()
	if c >= 3 and c < 6:
		print "Starting Wires game Difficulty:" , c
		response=1#w.startWireGame(c)
		if response == 1:
			g.sendMessage("Success")
		else:
			g.sendMessage("Failure")
	elif c >= 6:
		print("Client Error")
		result = 0
	g.endClient()
