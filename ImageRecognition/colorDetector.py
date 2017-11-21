import cv2
import numpy as np
from matplotlib import pyplot as plt

class ColorDetector:
	def __init__(self):
		pass
 
	def detect(self, hsv):

		red1_lower_range = np.array([159, 100, 100], dtype=np.uint8)
		red1_upper_range = np.array([199, 255, 255], dtype=np.uint8)

		red2_lower_range = np.array([0, 100, 100], dtype=np.uint8)
		red2_upper_range = np.array([20, 255, 255], dtype=np.uint8)


		blue_lower_range = np.array([98, 100, 100], dtype=np.uint8)
		blue_upper_range = np.array([138, 255, 255], dtype=np.uint8)

		green_lower_range = np.array([43, 100, 100], dtype=np.uint8)
		green_upper_range = np.array([83, 255, 255], dtype=np.uint8)

		black_lower_range = np.array([0, 100, 0], dtype=np.uint8)
		black_upper_range = np.array([255, 255, 20], dtype=np.uint8)

		red1mask = cv2.inRange(hsv, red1_lower_range, red1_upper_range)
		red2mask = cv2.inRange(hsv, red2_lower_range, red2_upper_range)
 		bluemask = cv2.inRange(hsv, blue_lower_range, blue_upper_range)
 		greenmask = cv2.inRange(hsv, green_lower_range, green_upper_range)
 		blackmask = cv2.inRange(hsv, black_lower_range, black_upper_range)
		
		color = "unknown"

		if blackmask[0,0] == 255:
			print("It's black!")
			color = "black"
		if red1mask[0,0] == 255:
			print("It's red!")
			color = "red"
		if red2mask[0,0] == 255:
			print("It's red!")
			color = "red"
		if bluemask[0,0] == 255:
			print("It's blue!")
			color = "blue"
		if greenmask[0,0] == 255:
			print("It's green!")
			color = "green"
		return color

 

 



if __name__ == '__main__':
	img = cv2.imread('Messi5.jpg')
	cd = ColorDetector()
	cd.detect(img)
