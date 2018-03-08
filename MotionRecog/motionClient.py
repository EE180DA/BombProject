import socket
import time
from Response import Response
from random import shuffle

class Client:
	def __init__(self):
		# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# client.connect((target, port))
		self.client.connect(('192.168.42.1', 4999))
		self.gesQuestions = ['0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1111']
		shuffle(self.gesQuestions)

	def startClient(self):
		# connect the client
		received = self.client.recv(4096)
		# Codewords
		if received == "G1":
			return(1)
		elif received == "G2":
			return(2)
		elif received == "G3":
			return(3)
		else: 
			return(8)
		print received
	def sendMessage(self, message):
		self.client.send(message)
		while True:
			received = self.client.recv(4096)
			time.sleep(0.1)
			if received == "ACK":
				print('Acknowledged')
				break
			else:
				print('Message not sent')
				self.client.send(message)
		print "Sent:", message


	def endClient(self):
		self.client.close()

if __name__ == '__main__':
	r = Response()
	while True:
		try:
			g = Client() 
			d = g.startClient()
			break
		except KeyboardInterrupt:
			exit()
		except:
			print('Didnt connect')
			time.sleep(1)
	i=0
	c=g.gesQuestions[i]
	g.sendMessage(c) 
	while d>0: 	
		if c == '0001':
			# For Q1, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '0010':
			# For Q2, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)

		if c == '0011':
			# For Q3, Shake is the correct answer
			response=r.get()
			if response == 2:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)

		if c == '0100':
			# For Q4, Shake is the correct answer
			response=r.get()
			if response == 2:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '0101':
			# For Q5, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '0110':
			# For Q6, Shake is the correct answer
			response=r.get()
			if response == 2:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '0111':
			# For Q7, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1000':
			# For Q8, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1001':
			# For Q9, Shake is the correct answer
			response=r.get()
			if response == 2:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1010':
			# For Q10, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1011':
			# For Q11, Shake is the correct answer
			response=r.get()
			if response == 2:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1100':
			# For code Q12, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1101':
			# For code Q13, Shake is the correct answer
			response=r.get()
			if response == 2:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1110':
			# For Q14, Nod is the correct answer
			response=r.get()
			if response == 1:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if c == '1111':
			# For Q15, Shake is the correct answer
			response=r.get()
			if response == 2:
				d-=1
				if d<=0: 
					break
				g.sendMessage('Right')
				time.sleep(1)
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage(c)
			elif response == 3:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Pass')
				time.sleep(1)
				g.sendMessage(c)
			elif response == 4:
				g.sendMessage('Hint')
				time.sleep(1)
			else:
				if i<15:
					i+=1
				else: 
					i=0
				c=g.gesQuestions[i]
				g.sendMessage('Wrong')
				time.sleep(1)
				g.sendMessage(c)
		if d == 8:
			print('Client Error')
			result = 0
			break
	g.sendMessage('Success')
	g.endClient()