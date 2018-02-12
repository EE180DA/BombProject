import socket
import time
from WireCutting.WireCutting import WireCutting
from Buttons.Buttons import Buttons
class Client:
	def __init__(self):
		# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# client.connect((target, port))
		self.client.connect(('192.168.42.1', 3999))

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
				return(0)
			elif received == "B2":
				return(1)
			elif received == "B3":
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
		b = Buttons(c)
		print "Starting Buttons game Difficulty:" , c
		response=1#b.startGame()
		if response == 1:
			g.sendMessage("Success")
		else:
			g.sendMessage("Failure")

	c = g.startClient()
	if c >= 3 and c < 6:
		w = WireCutting()
		print "Starting Wires game Difficulty:" , c
		response=1#w.startGame(c)
		if response == 1:
			g.sendMessage("Success")
		else:
			g.sendMessage("Failure")
	elif c >= 6:
		print("Client Error")
		result = 0
	g.endClient()
