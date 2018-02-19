import mraa

class theButton:
	def __init__(self, diff):
		self.pin = mraa.Gpio(8)
		self.difficulty = diff

	def start(self, diff):
		while True:
			if self.pin.read() == 1:
				print "Button pressed"

if __name__ == '__main__':
	b = theButton()
	b.start()