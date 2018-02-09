import mraa
import time

while True:
	print "b0", mraa.Gpio(0).read()
	# print "b1", mraa.Gpio(1).read()
	# print "b2", mraa.Gpio(2).read()
	# print "b3", mraa.Gpio(3).read()
	# print "b4", mraa.Gpio(4).read()
	# print "b5", mraa.Gpio(5).read()
	# print "b6", mraa.Gpio(6).read()
	# print "b7", mraa.Gpio(7).read()
	time.sleep(0.1)