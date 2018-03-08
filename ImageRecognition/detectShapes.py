from shapeDetector import ShapeDetector
from colorDetector import ColorDetector
from Display.screen import Display
import imutils
import cv2
import numpy as np 
import random


class DetectShapes:

	def __init__ (self):
		self.shapes = ["triangle", "rectangle", "pentagon", "hexagon"]
		self.shapes_morse = {"triangle" : "- .-. ..", "rectangle" : ".-. . -.-.", "pentagon" : ".--. . -. ", "hexagon" : ".... . -..-"}
		self.colors = ["red", "blue", "green", "black", "brown", "purple", "orange"]
		self.colors_morse =  {"red" : ".-. . -..", "blue" : "-... .-.. ..-", "green" : "--. .-. .", "black" : "-... .-.. .-", "brown" : "-... .-. ---", "purple" : ".--. ..- .-.", "orange" : "--- .-. .-"}
                self.target_col = self.choose_target_color()
                self.target_sha = self.choose_target_shape()
                self.lcd = Display()

        def get_target_shape(self):
                return self.target_sha

        def get_target_color(self):
                return self.target_col

	def choose_target_shape(self):
		index = random.randint(0,3)
                print self.shapes[index]
		return self.shapes[index]

	def choose_target_color(self):
		index = random.randint(0,6)
                print self.colors[index]
		return self.colors[index]

	def get_shape_morse(self, shape):
		return self.shapes_morse[shape]

	def get_color_morse(self, color):
		return self.colors_morse[color]

	def start_minigame(self):
		cap = cv2.VideoCapture(0)
		detectCount = 0
		while(True):
			if not cap.isOpened():
				cap.open()
			ret, frame = cap.read()
			fullyDetected = False
			if ret:
				resized = imutils.resize(frame, width=300)
				ycb = cv2.cvtColor(resized, cv2.COLOR_BGR2YCR_CB)
				ratio = frame.shape[0] / float(resized.shape[0])
				gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
				blurred = cv2.GaussianBlur(gray, (5, 5), 0)
				thresh = cv2.threshold(blurred, 120, 255, cv2.THRESH_BINARY)[1]
				thresh = cv2.bitwise_not(thresh)
				# kernel = np.ones((5,5),np.uint8)
				# dilation = cv2.dilate(thresh,kernel,iterations = 1)
				cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
				cnts = cnts[0] if imutils.is_cv2() else cnts[1]
				sd = ShapeDetector()
				cd = ColorDetector()
				detected = False
				for c in cnts:
					# compute the center of the contour, then detect the name of the
					# shape using only the contour
					M = cv2.moments(c)
					cX = 0
					cY = 0
					if (M["m00"] != 0):
						cX = int((M["m10"] / M["m00"]))
						cY = int((M["m01"] / M["m00"]))

					shape = sd.detect(c)
			 		# color = cd.detect(frame[cX, cY])
			 		color = "unknown"
			 		if cX < resized.shape[0]-10 and cX > 10 and cY < resized.shape[1]-10 and cY > 10:
			 			pixel = ycb[cY-10:cY+10, cX-10:cX+10]
			 			color = cd.detect(pixel)
					# multiply the contour (x, y)-coordinates by the resize ratio,
					# then draw the contours and the name of the shape on the image
					c = c.astype("float")
					# c *= ratio
					c = c.astype("int")
					cv2.drawContours(resized, [c], -1, (0, 255, 0), 2)
					cv2.putText(resized, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
			 		cv2.putText(resized, color, (cX, cY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
					# show the output image
                                        print color + " " + shape
					if shape == self.target_sha and color == self.target_col:
						detected = True
						# print "detected"
				if detected:
					detectCount += 1
                                        self.lcd.set_color("g")
				else:
					detectCount = 0
                                        self.lcd.set_color("o")
				#print detectCount
				if detectCount > 9:
					fullyDetected = True
				

				#cv2.imshow('frame', resized)
				if fullyDetected:
					break
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
		cap.release()
		cv2.destroyAllWindows()
		if fullyDetected:
			return 1
		else:
			return 0

if __name__ == '__main__':
	d = DetectShapes()
	color = d.get_target_color()
        print "color is: %s" % color
	print d.get_color_morse(color)
	shape = d.get_target_shape()
	print shape
	print d.get_shape_morse(shape)
        d.start_minigame()
