from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2


class localize:

	def midpoint(ptA, ptB):
		return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

	def __init__ (self):
		pass

	def find_distance(self):
		cap = cv2.VideoCapture(1)
		detectCount = 0

		green_lower_range = np.array([0, 68, 30], dtype=np.uint8)
		green_upper_range = np.array([143, 123, 146], dtype=np.uint8)

		red_lower_range = np.array([45, 167, 75], dtype=np.uint8)
		red_upper_range = np.array([150, 255, 124], dtype=np.uint8)

		while(True):
			if not cap.isOpened():
				cap.open()
			ret, frame = cap.read()
			if ret:
				ycb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
				greenmask = cv2.inRange(ycb, green_lower_range, green_upper_range)
				gray = cv2.GaussianBlur(greenmask, (5, 5), 0)
				edged = cv2.Canny(gray, 70, 90)
				edged = cv2.dilate(edged, None, iterations=1)
				edged = cv2.erode(edged, None, iterations=1)


				#finding contours
				cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
				cnts = cnts[0] if imutils.is_cv2() else cnts[1]	
				colors = ((0, 0, 255), (240, 0, 159), (0, 165, 255), (255, 255, 0),
					(255, 0, 255))
				refObj = None
				biggest_green = np.zeros([1,1])
				biggest_red = np.zeros([1,1])
				for c in cnts:
					# if the contour is not sufficiently large, ignore it
					area = cv2.contourArea(c)
					if area < 100:
						continue
				 	
					approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
					area = cv2.contourArea(c)
					if ((len(approx) > 8) & (len(approx) < 23) & (area > 60) ):
						if not biggest_green.all():
							biggest_green = c
						elif area > cv2.contourArea(biggest_green):
							biggest_green = c
				if biggest_green.all():
					area = cv2.contourArea(biggest_green)
					radius = int((np.sqrt(area/3.14))/4)
					M = cv2.moments(biggest_green)
					cX = int(M["m10"] / M["m00"])
					cY = int(M["m01"] / M["m00"])
					cv2.circle(frame, (cX, cY), radius, (0, 255, 0), -1)

				redmask = cv2.inRange(ycb, red_lower_range, red_upper_range)
				gray = cv2.GaussianBlur(redmask, (5, 5), 0)
				edged = cv2.Canny(gray, 70, 90)
				edged = cv2.dilate(edged, None, iterations=1)
				edged = cv2.erode(edged, None, iterations=1)


				cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
				cnts = cnts[0] if imutils.is_cv2() else cnts[1]	

				for c in cnts:
					# if the contour is not sufficiently large, ignore it
					area = cv2.contourArea(c)
					if area < 100:
						continue
				 	
					approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
					area = cv2.contourArea(c)
					if ((len(approx) > 8) & (len(approx) < 23) & (area > 60) ):
						if not biggest_red.all():
							biggest_red = c
						elif area > cv2.contourArea(biggest_red):
							biggest_red = c
				if biggest_red.all():
						M = cv2.moments(biggest_red)
						cX = int(M["m10"] / M["m00"])
						cY = int(M["m01"] / M["m00"])
						cv2.circle(frame, (cX, cY), 20, (0, 0, 255), -1)
				# cv2.imshow('edged',edged)
				# cv2.imshow('gray',gray)
				cv2.imshow('Objects Detected',frame)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
		cap.release()
		cv2.destroyAllWindows()


if __name__ == '__main__':
	d = localize()
	d.find_distance()