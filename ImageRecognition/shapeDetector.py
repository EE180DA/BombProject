# import the necessary packages
import cv2
 
class ShapeDetector:
	def __init__(self):
		pass
 
	def detect(self, c):
		# initialize the shape name and approximate the contour

		shape = "unidentified"
		i = 0
		curLen = -1
		n = 0
		while (i<15):
			peri = cv2.arcLength(c, True)
			approx = cv2.approxPolyDP(c, 0.035 * peri, True)
			if len(approx) == 3:
				if curLen == 3:
					n = n+1
				else:
					n = n-1
					if n < 0:
						curLen = 3
			elif len(approx) == 4:
				if curLen == 4:
					n = n+1
				else:
					n = n-1
					if n < 0:
						curLen = 4
			elif len(approx) == 5:
				if curLen == 5:
					n = n+1
				else:
					n = n-1
					if n < 0:
						curLen = 5
			elif len(approx) == 6:
				if curLen == 6:
					n = n+1
				else:
					n = n-1
					if n < 0:
						curLen = 6
			elif len(approx) == 7:
				if curLen == 7:
					n = n+1
				else:
					n = n-1
					if n < 0:
						curLen = 7
			else:
				if curLen == 0:
					n = n+1
				else:
					n = n-1
					if n < 0:
						curLen = 0
			i = i+1
		if curLen == 3:
			shape = "triangle"
 
		# if the shape has 4 vertices, it is either a square or
		# a rectangle
		elif curLen == 4:
			# compute the bounding box of the contour and use the
			# bounding box to compute the aspect ratio
			(x, y, w, h) = cv2.boundingRect(approx)
			ar = w / float(h)
 
			# a square will have an aspect ratio that is approximately
			# equal to one, otherwise, the shape is a rectangle
			shape = "square" if ar >= 0.80 and ar <= 1.2 else "rectangle"
 
		# if the shape is a pentagon, it will have 5 vertices
		elif curLen == 5:
			shape = "pentagon"
		elif curLen == 6:
			shape = "hexagon"
		elif curLen == 7:
			shape = "heptagon"
 
		# otherwise, we assume the shape is a circle
		else:
			shape = "circle"
 
		# return the name of the shape
		return shape