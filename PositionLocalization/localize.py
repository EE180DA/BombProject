from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import time


class Localize:

	def midpoint(ptA, ptB):
		return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

	def __init__ (self):
		pass

	def find(self, time_left):
		start_time = time.time()
		cap = cv2.VideoCapture(2)
		detectCount = 0

		green_lower_range = np.array([0, 40, 30], dtype=np.uint8)
		green_upper_range = np.array([223, 117, 155], dtype=np.uint8)

		red_lower_range = np.array([25, 155, 75], dtype=np.uint8)
		red_upper_range = np.array([160, 255, 124], dtype=np.uint8)

		while(time.time()-start_time < time_left):
			if not cap.isOpened():
				cap.open()
			ret, frame = cap.read()
			if ret:
				r_distance = 100
				g_distance = 100
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
					#((r_x, r_y), r_radius) = cv2.minEnclosingCircle(biggest_red)
					green_radius = max(w,h)/2
					M = cv2.moments(biggest_green)
					cX = int(M["m10"] / M["m00"])
					cY = int(M["m01"] / M["m00"])
					g_distance = 85.461*np.power(green_radius, -1.031)
					#cv2.circle(frame, (cX, cY), green_radius/4, (0, 255, 0), -1)
					print " Green Area: " + str(green_area) + "  Green Radius: " + str(green_radius) + "  Distance: " + str(g_distance)
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
						#(r_x, r_y), r_radius = cv2.minEnclosingCircle(biggest_red)
						red_area = int(cv2.contourArea(biggest_red))
						M = cv2.moments(biggest_red)
						x,y,w,h = cv2.boundingRect(biggest_red)
						red_radius = max(w, h)/2
						r_distance = 85.461*np.power(red_radius, -1.031)
						cX = int(M["m10"] / M["m00"])
						cY = int(M["m01"] / M["m00"])
						cv2.circle(frame, (cX, cY), red_radius/4, (0, 0, 255), -1)
						#cv2.circle(frame, (int(r_x), int(r_y)), int(r_radius), (0, 0, 255), -1)
						print " Red Area: " + str(red_area) + "  Red Radius: " + str(red_radius)  + "  Distance: " + str(r_distance)
				# cv2.imshow('edged',edged)
				# cv2.imshow('gray',gray)
				
				cv2.imshow('Objects Detected',frame)
				cv2.imshow('green', green_edged)
				cv2.imshow('red', red_edged)
				if r_distance < 0.7:
					return "red"
				elif g_distance < 0.7:
					return "green"
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break

		cap.release()
		cv2.destroyAllWindows()
		return "boom"


if __name__ == '__main__':
	d = Localize()
	detected = d.find(10)
	print "Detected: " + detected