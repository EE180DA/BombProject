from shapeDetector import ShapeDetector
from colorDetector import ColorDetector
import imutils
import cv2
import numpy as np 

cap = cv2.VideoCapture(0)

while(True):
	if not cap.isOpened():
		cap.open()
	ret, frame = cap.read()
	if ret:
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		resized = imutils.resize(frame, width=300)
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
	 		if cX < resized.shape[0]-20 and cX > 20 and cY < resized.shape[1]-20 and cY > 20:
	 			pixel = resized[cX-20:cX+20, cY-20:cY+20]
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

		cv2.imshow('frame', resized)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
cap.release()
cv2.destroyAllWindows()
