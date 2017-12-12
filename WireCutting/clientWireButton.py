import socket
import time
from WireCutting import WireCutting

class Client:
	def __init__(self):
		# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# client.connect((target, port))
		self.client.connect(('192.168.42.1', 3999))

	def startClient(self):
		# connect the client
		received = self.client.recv(4096)
		# Codewords for each wire
		if received == "ReRe":
			return(0)
		elif received == "BrGr":
			return(1)
		elif received == "BlBl":
			return(2)
		elif received == "BrBl":
			return(3)
		elif received == "ReWh":
			return(4)
		else:
			return(5)

	def endClient(self, output):
		if output == 0:
			self.client.send('Fail')
		elif output == 1:
			self.client.send('Success')
		self.client.close()

if __name__ == '__main__':
	r = WireCutting()
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

	while True: 	
		if c == 0:
			response=r.startGame(c)
			if response == 1:
				result = 1
				g.endClient(result)
				break
			else:
				result = 0
		elif c == 1:
			response=r.startGame(c)
			if response == 1:
				result = 1
				g.endClient(result)
				break
			else:
				result = 0
		elif c == 2:
			response=r.startGame(c)
			if response == 1:
				result = 1
				g.endClient(result)
				break
			else:
				result = 0
		elif c == 3:
			response=r.startGame(c)
			if response == 1:
				result = 1
				g.endClient(result)
				break
			else:
				result = 0
		elif c == 4:
			response=r.startGame(c)
			if response == 1:
				result = 1
				g.endClient(result)
				break
			else:
				result = 0
		elif c == 5:
			print('Client Error')
			result = 0
		g.endClient(result)