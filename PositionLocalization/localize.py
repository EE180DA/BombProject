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
		cap = cv2.VideoCapture(0)
		detectCount = 0

		green_lower_range = np.array([0, 67, 30], dtype=np.uint8)
		green_upper_range = np.array([167, 118, 145], dtype=np.uint8)

		red_lower_range = np.array([45, 188, 75], dtype=np.uint8)
		red_upper_range = np.array([160, 255, 124], dtype=np.uint8)

		while(True):
			if not cap.isOpened():
				cap.open()
			ret, frame = cap.read()
			if ret:
				ycb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
				greenmask = cv2.inRange(ycb, green_lower_range, green_upper_range)
				gray = cv2.GaussianBlur(greenmask, (5, 5), 0)
				green_edged = cv2.Canny(gray, 70, 90)
				green_edged = cv2.dilate(green_edged, None, iterations=1)
				green_edged = cv2.erode(green_edged, None, iterations=1)
				# green_edged = cv2.erode(green_edged, None, iterations=1)
				# green_edged = cv2.dilate(green_edged, None, iterations=1)
				#finding contours
				cnts = cv2.findContours(green_edged.copy(), cv2.RETR_EXTERNAL,
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
					if area < 700:
						continue
				 	
					approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
					area = cv2.contourArea(c)
					if ((len(approx) > 8) & (len(approx) < 23) & (area > 60) ):
						if not biggest_green.all():
							biggest_green = c
						elif area > cv2.contourArea(biggest_green):
							biggest_green = c
				if biggest_green.all():
					green_area = cv2.contourArea(biggest_green)
					# green_radius = int(np.sqrt(green_area/3.14))
					x,y,w,h = cv2.boundingRect(biggest_green)
					green_radius = max(w,h)
					M = cv2.moments(biggest_green)
					cX = int(M["m10"] / M["m00"])
					cY = int(M["m01"] / M["m00"])
					cv2.circle(frame, (cX, cY), green_radius/4, (0, 255, 0), -1)
					print " Green Area: " + str(green_area) + "  Green Radius: " + str(green_radius)
				redmask = cv2.inRange(ycb, red_lower_range, red_upper_range)
				gray = cv2.GaussianBlur(redmask, (5, 5), 0)
				gray = cv2.erode(gray, None, iterations=1)
				gray = cv2.dilate(gray, None, iterations=1)
				red_edged = cv2.Canny(gray, 70, 90)
				red_edged = cv2.dilate(red_edged, None, iterations=1)
				red_edged = cv2.erode(red_edged, None, iterations=1)
				

				cnts = cv2.findContours(red_edged.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
				cnts = cnts[0] if imutils.is_cv2() else cnts[1]	

				for c in cnts:
					# if the contour is not sufficiently large, ignore it
					area = cv2.contourArea(c)
					if area < 700:
						continue
				 	
					approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
					area = cv2.contourArea(c)
					if ((len(approx) > 8) & (len(approx) < 23) & (area > 60) ):
						if not biggest_red.all():
							biggest_red = c
						elif area > cv2.contourArea(biggest_red):
							biggest_red = c
				if biggest_red.all():
						# red_radius = int(np.sqrt(cv2.contourArea(biggest_red)/3.14))
						red_area = int(cv2.contourArea(biggest_red))
						M = cv2.moments(biggest_red)
						x,y,w,h = cv2.boundingRect(biggest_red)
						red_radius = max(w, h)
						cX = int(M["m10"] / M["m00"])
						cY = int(M["m01"] / M["m00"])
						cv2.circle(frame, (cX, cY), red_radius/4, (0, 0, 255), -1)
						print " Red Area: " + str(red_area) + "  Red Radius: " + str(red_radius) 
				# cv2.imshow('edged',edged)
				# cv2.imshow('gray',gray)
				
				cv2.imshow('Objects Detected',frame)
				cv2.imshow('red', green_edged)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
		cap.release()
		cv2.destroyAllWindows()


if __name__ == '__main__':
	d = localize()
	d.find_distance()