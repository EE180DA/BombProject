import socket
import time
from Response import Response

class Client:
	def __init__(self):
		# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# client.connect((target, port))
		self.client.connect(('192.168.42.1', 4999))

	def startClient(self):
		# connect the client
		received = self.client.recv(4096)
		# Codewords
		if received == "001":
			return(1)
		elif received == "010":
			return(2)
		elif received == "011":
			return(3)
		elif received == "100":
			return(4)
		elif received == "101":
			return(5)
		elif received == "110":
			return(6)
		elif received == "111":
			return(7)
		else: 
			return(8)
	def sendMessage(self, message):
		self.client.send(message)
		print "Sent:", message


	def endClient(self):
		self.client.close()

if __name__ == '__main__':
	r = Response()
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
		if c == 1:
			# For code 001, Nod is the correct answer
			response=r.get()
			if response == 1:
				result = 1
				g.sendMessage('Success')
				break
			elif response == 3:
				result = 2
				c=2
				g.sendMessage('Pass')
			elif response == 4:
				result = 3
				g.sendMessage('Hint')
			else:
				result = 0
				c=2
				g.sendMessage('Fail')
		if c == 2:
			# For code 010, Nod is the correct answer
			response=r.get()
			if response == 1:
				result = 1
				g.sendMessage('Success')
				break
			elif response == 3:
				result = 2
				c=3
				g.sendMessage('Pass')
			elif response == 4:
				result = 3
				g.sendMessage('Hint')
			else:
				result = 0
				c=3
				g.sendMessage('Fail')

		if c == 3:
			# For code 011, Shake is the correct answer
			response=r.get()
			if response == 2:
				result = 1
				g.sendMessage('Success')
				break
			elif response == 3:
				result = 2
				c=4
				g.sendMessage('Pass')
			elif response == 4:
				result = 3
				g.sendMessage('Hint')
			else:
				result = 0
				c=4
				g.sendMessage('Fail')

		if c == 4:
			# For code 100, Shake is the correct answer
			response=r.get()
			if response == 2:
				result = 1
				g.sendMessage('Success')
				break
			elif response == 3:
				result = 2
				c=5
				g.sendMessage('Pass')
			elif response == 4:
				result = 3
				g.sendMessage('Hint')
			else:
				result = 0
				c=5
				g.sendMessage('Fail')
		if c == 5:
			# For code 101, Nod is the correct answer
			response=r.get()
			if response == 1:
				result = 1
				g.sendMessage('Success')
				break
			elif response == 3:
				result = 2
				c=6
				g.sendMessage('Pass')
			elif response == 4:
				result = 3
				g.sendMessage('Hint')
			else:
				result = 0
				c=6
				g.sendMessage('Fail')
		if c == 6:
			# For code 110, Shake is the correct answer
			response=r.get()
			if response == 2:
				result = 1
				g.sendMessage('Success')
				break
			elif response == 3:
				result = 2
				c=7
				g.sendMessage('Pass')
			elif response == 4:
				result = 3
				g.sendMessage('Hint')
			else:
				result = 0
				c=7
				g.sendMessage('Fail')
		if c == 7:
			# For code 111, Nod is the correct answer
			response=r.get()
			if response == 1:
				result = 1
				g.sendMessage('Success')
				break
			elif response == 3:
				result = 2
				c=1
				g.sendMessage('Pass')
			elif response == 4:
				result = 3
				g.sendMessage('Hint')
			else:
				result = 0
				c=1
				g.sendMessage('Fail')
		if c == 8:
			print('Client Error')
			result = 0
			break
	g.endClient()