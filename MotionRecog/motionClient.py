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
		# Codeword 1234
		if received == "1234":
			return(1)
		# Codeword 5678
		elif received == "5678":
			return(2)
		else: 
			return(5)

	def endClient(self, output):
		if output == 0:
			self.client.send('Fail')
		elif output == 1:
			self.client.send('Success')
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
			# For code 1234, Nod is the correct answer
			response=r.get()
			if response == 1:
				result = 1
				g.endClient(result)
				break
			else
				result = 0
		elif c == 2:
			response=r.get()
			# For code 5678, Shake is the correct answer
			if response == 2:
				result = 1
				g.endClient(result)
				break
			else
				result = 0
		elif c == 5:
			print('Client Error')
			result = 0
		g.endClient(result)