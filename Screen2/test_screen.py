import socket
import time
import threading
import thread
import sys
from Display.screen import Display

class Client:
	def __init__(self):
		# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
		#self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# client.connect((target, port))
		#self.client.connect(('192.168.42.1', 5999))
		self.top = ""
		self.bottom = ""
		self.lcd = Display()
		self.lcd.write_top("")
		self.lcd.write_bot("")
                self.code = ""
		self.morse_thread = threading.Thread(target = self.morse, args = ())
		self.morse_thread.daemon = True
		self.morsing = True

	def morse(self):
                self.lcd.set_color("o")
                time.sleep(1)
		while(self.morsing):
			for c in self.code:
				if c == ".":
					self.lcd.set_color("g")
					time.sleep(0.1)
					self.lcd.set_color("o")
                                        time.sleep(0.1)
				if c == "-":
					self.lcd.set_color("g")
					time.sleep(0.5)
					self.lcd.set_color("o")
                                        time.sleep(0.1)
				if c == " ":
					time.sleep(1)
                        time.sleep(1)
                        self.lcd.set_color("r")
			time.sleep(2)
                        self.lcd.set_color("o")
                        time.sleep(2)


	def startClient(self):
		# connect the client
		while True:
			#received = self.client.recv(4096)
                        received = raw_input("Input: ")
			#print received
			if received == "":
				time.sleep(1)
				continue
			elif received[0] == "t":
				self.top = received[1:]
				self.lcd.write_top(self.top)
			elif received[0] == "b":
				self.bottom = received[1:]
				self.lcd.write_bot(self.bottom)
			elif received[0] == "m":
				self.top = "Read Morse"
				self.bottom = "Much?"
                                self.code = received[1:]
                                self.morse_thread.start()
				self.morsing = True
                        elif received[0] == "#":
				self.morsing = False
                                self.morse_thread.join()



	def sendMessage(self, message):
		self.client.send(message)
		print "Sent:", message

	def endClient(self):
		self.client.close()

if __name__ == '__main__':
	g = Client()
        g.startClient()