import mraa
from VoiceRecog.speech import SpeechRecognition
import time

class TheButton:
	def __init__(self, diff):
		self.pin = mraa.Gpio(8)
		self.difficulty = diff
		self.button_time = 5

	def start(self):
                print "started checking"
		timeout_start = time.time()
                #5 seconds to press the red button to initiate bonus sequence
                while time.time() < timeout_start + self.button_time:
	    	    if self.pin.read() == 1:
                        print "button pressed"
		    	g = SpeechRecognition()
		        result = g.start_bonus()
		        return result
                print "time over"
	        return(0)
		#result = 0:no bonus, 1:add score, 2:add time

if __name__ == '__main__':
	b = theButton(0)
	result = b.start()
	print result
