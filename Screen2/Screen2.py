import socket
import time
from .Display.screen import Display

class Client:
	def __init__(self):
		# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# client.connect((target, port))
		self.client.connect(('192.168.42.1', 5999))
		self.top = ""
		self.bottom = ""
		self.lcd = Display()
        self.writeTop("")
        self.writeBot("")

	def startClient(self):
		# connect the client
		while True:
			received = self.client.recv(4096)
			print received
                if received == "":
                    time.sleep(1)
                    continue
                if received[0] == "t":
                	self.top = received[1:]
                	self.lcd.writeTop(self.top)
                if received[0] == "b":
                	self.bottom = received[1:]
                	self.lcd.writeBot(self.bottom)


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


	g.endClient()
