import socket
import time
import threading
import thread
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
		self.lcd.writeTop("")
		self.lcd.writeBot("")
		self.morse_thread = threading.Thread(target = self.morse, args = (code,))
		self.morse_thread.daemon = True
		self.morsing = False

	def morse(self, code):
		while(morsing):
			for c in code:
				if c == ".":
					self.lcd.setcolor("g")
					time.sleep(0.3)
					self.lcd.setcolor("o")
				if c == "-":
					self.lcd.setcolor("g")
					time.sleep(1)
					self.lcd.setcolor("o")
				if c == " ":
					time.sleep(1)
			time.sleep(2)


	def startClient(self):
		# connect the client
		while True:
			received = self.client.recv(4096)
			print received
			if received == "":
				time.sleep(1)
				continue
			elif received[0] == "t":
				self.top = received[1:]
				self.lcd.writeTop(self.top)
			elif received[0] == "b":
				self.bottom = received[1:]
				self.lcd.writeBot(self.bottom)
			elif received[0] == "m":
				self.top = "Read Morse"
				self.bottom = "Much?"
				self.morsing = True
			elif received[0] == "#"
				self.morsing = False


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
