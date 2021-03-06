import cv2
import numpy as np
from matplotlib import pyplot as plt

class ColorDetector:
	def __init__(self):
		pass
 
	def detect(self, ycb):
		red_lower_range = np.array([40, 182, 95], dtype=np.uint8)
		red_upper_range = np.array([113, 225, 136], dtype=np.uint8)

		blue_lower_range = np.array([0, 54, 143], dtype=np.uint8)
		blue_upper_range = np.array([90, 116, 198], dtype=np.uint8)

		green_lower_range = np.array([30, 50, 106], dtype=np.uint8)
		green_upper_range = np.array([134, 121, 127], dtype=np.uint8)

		black_lower_range = np.array([0, 109, 121], dtype=np.uint8)
		black_upper_range = np.array([63, 126, 142], dtype=np.uint8)

		brown_lower_range = np.array([17, 129, 76], dtype=np.uint8)
		brown_upper_range = np.array([91, 178, 124], dtype=np.uint8)

		purple_lower_range = np.array([0, 129, 151], dtype=np.uint8)
		purple_upper_range = np.array([106, 149, 201], dtype=np.uint8)

		orange_lower_range = np.array([54, 149, 40], dtype=np.uint8)
		orange_upper_range = np.array([116, 224, 94], dtype=np.uint8)

		redmask = cv2.inRange(ycb, red_lower_range, red_upper_range)
 		bluemask = cv2.inRange(ycb, blue_lower_range, blue_upper_range)
 		greenmask = cv2.inRange(ycb, green_lower_range, green_upper_range)
 		blackmask = cv2.inRange(ycb, black_lower_range, black_upper_range)
		purplemask = cv2.inRange(ycb, purple_lower_range, purple_upper_range)
		brownmask = cv2.inRange(ycb, brown_lower_range, brown_upper_range)
		orangemask = cv2.inRange(ycb, orange_lower_range, orange_upper_range)

		values = [0, 0, 0, 0, 0, 0, 0]

		color = "unknown"
		for i in range (0, blackmask.shape[0]):
			for j in range (0, blackmask.shape[1]):
				values[0]+=blackmask[i,j]
		#print("Number of black pixels: %d" % (values[0]/255))
		for i in range (0, redmask.shape[0]):
			for j in range (0, redmask.shape[1]):
				values[1]+=redmask[i,j]
		#print("Number of red pixels: %d" % (values[1]/255))
		for i in range (0, bluemask.shape[0]):
			for j in range (0, bluemask.shape[1]):
				values[2]+=bluemask[i,j]
		#print("Number of blue pixels: %d" % (values[2]/255))
		for i in range (0, greenmask.shape[0]):
			for j in range (0, greenmask.shape[1]):
				values[3]+=greenmask[i,j]
		#print("Number of green pixels: %d" % (values[3]/255))
		for i in range (0, purplemask.shape[0]):
			for j in range (0, purplemask.shape[1]):
				values[4]+=purplemask[i,j]
		#print("Number of purple pixels: %d" % (values[4]/255))
		for i in range (0, brownmask.shape[0]):
			for j in range (0, brownmask.shape[1]):
				values[5]+=brownmask[i,j]
		#print("Number of brown pixels: %d" % (values[5]/255))
		for i in range (0, orangemask.shape[0]):
			for j in range (0, orangemask.shape[1]):
				values[6]+=orangemask[i,j]
		#print("Number of black pixels: %d" % (values[6]/255))
		#print("Total number of pixels:" + str(blackmask.shape[0]*blackmask.shape[1]))
		m = values.index(max(values))
		if max(values) > 0:
			if m == 0:
				color = "black"
			if m == 1:
				color = "red"
			if m == 2:
				color = "blue"
			if m == 3:
				color = "green"
			if m == 4:
				color = "purple" 
			if m == 5:
				color = "brown" 
			if m == 6:
				color = "orange"  
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
		#print color
		return color

 

 



if __name__ == '__main__':
	img = cv2.imread('RedPixel.jpg')
	ycb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
	cd = ColorDetector()
	cd.detect(ycb)
