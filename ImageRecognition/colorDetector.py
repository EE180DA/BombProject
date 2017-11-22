import cv2
import numpy as np
from matplotlib import pyplot as plt

class ColorDetector:
	def __init__(self):
		pass
 
	def detect(self, hsv):
		cv2.imshow('frame',hsv)
		red1_lower_range = np.array([159, 100, 100], dtype=np.uint8)
		red1_upper_range = np.array([199, 255, 255], dtype=np.uint8)

		red2_lower_range = np.array([0, 100, 100], dtype=np.uint8)
		red2_upper_range = np.array([20, 255, 255], dtype=np.uint8)


		blue_lower_range = np.array([98, 100, 100], dtype=np.uint8)
		blue_upper_range = np.array([138, 255, 255], dtype=np.uint8)

		green_lower_range = np.array([43, 100, 100], dtype=np.uint8)
		green_upper_range = np.array([83, 255, 255], dtype=np.uint8)

		black_lower_range = np.array([0, 0, 0], dtype=np.uint8)
		black_upper_range = np.array([180, 255, 30], dtype=np.uint8)

		red1mask = cv2.inRange(hsv, red1_lower_range, red1_upper_range)
		red2mask = cv2.inRange(hsv, red2_lower_range, red2_upper_range)
 		bluemask = cv2.inRange(hsv, blue_lower_range, blue_upper_range)
 		greenmask = cv2.inRange(hsv, green_lower_range, green_upper_range)
 		blackmask = cv2.inRange(hsv, black_lower_range, black_upper_range)
		
		values = [0, 0, 0, 0, 0]

		color = "unknown"
		for i in range (0, blackmask.shape[0]):
			for j in range (0, blackmask.shape[1]):
				values[0]+=blackmask[i,j]
		print("Number of black pixels: %d" % (values[0]))
		for i in range (0, red1mask.shape[0]):
			for j in range (0, red1mask.shape[1]):
				values[1]+=red1mask[i,j]
		print("Number of red1 pixels: %d" % (values[1]))
		for i in range (0, red2mask.shape[0]):
			for j in range (0, red2mask.shape[1]):
				values[2]+=red2mask[i,j]
		print("Number of red2 pixels: %d" % (values[2]))
		for i in range (0, bluemask.shape[0]):
			for j in range (0, bluemask.shape[1]):
				values[3]+=bluemask[i,j]
		print("Number of blue pixels: %d" % (values[3]))
		for i in range (0, greenmask.shape[0]):
			for j in range (0, greenmask.shape[1]):
				values[4]+=greenmask[i,j]
		print("Number of green pixels: %d" % (values[4]))
		m = values.index(max(values))
		if max(values) != 0:
			if m == 0:
				color = "black"
			if m == 1 or m==2:
				color = "red"
			if m == 3:
				color = "blue"
			if m == 4:
				color = "green" 

		# if blackmask[0,0] == 255:
		# 	print("It's black!")
		# 	color = "black"
		# if red1mask[0,0] == 255:
		# 	print("It's red!")
		# 	color = "red"
		# if red2mask[0,0] == 255:
		# 	print("It's red!")
		# 	color = "red"
		# if bluemask[0,0] == 255:
		# 	print("It's blue!")
		# 	color = "blue"
		# if greenmask[0,0] == 255:
		# 	print("It's green!")
		# 	color = "green"
		return color

 

 



if __name__ == '__main__':
	img = cv2.imread('GreenPixel.jpg')
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	cd = ColorDetector()
	cd.detect(hsv)
