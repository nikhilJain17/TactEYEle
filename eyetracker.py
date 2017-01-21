import cv2
import numpy as numpynav
import time
from pynput.mouse import Button, Controller
# gray scale
# use eye haar cascade to center in on the eye
# canny to find edges
# hough circle detection to find der pupil


print "starting"

mouse = Controller()

capture = cv2.VideoCapture(0)
# read, show = capture.read()
# cv2.imshow('', show)
time.sleep(0.5)


while True:
	# update the mouse position

	curX = mouse.position[0]
	curY = mouse.position[1]
	print 'MOUSE AT: ' + str(curX) + ', ' + str(curY)

	_, input_image = capture.read()

	# search only within the face for der eyes
	face_cascade = cv2.CascadeClassifier('haarcascade_face.xml')
	face_found = face_cascade.detectMultiScale(input_image, 1.3, 5)

	# print 'testetetset ' + str((face_found[0])[0])

	for (x, y, w, h) in face_found:

		x = (face_found[0])[0]
		y = (face_found[0])[1]
		w = (face_found[0])[2]
		h = (face_found[0])[3]

		input_image = input_image[y:y+h, x:x+w]
		input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

		# detect der eye
		eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
		eyes_found = eye_cascade.detectMultiScale(input_image)


		# at this point we have the eyes
 
		# only draw two forking circles
		# @TODO SHOULD I GET RID OF THIS
		counter = 0
		for (ex, ey, ew, er) in eyes_found:
			
			# draw a circle
			counter += 1
			if (counter > 2):
				break

			else:
				cv2.circle(input_image, (ex + ew/2 , ey + ew/2), ew/2, (0, 
255, 255), 5)
				# # draw a cross on the center of the eye
				# x1 = ex + ew/2
				# x2 = ex + ew/2 + 5
				# cv2.line(roi_gray, (x1, ey + ew/2), (x2, ey + ew/2), (0, 0, 0), 5)	
				print str(ex + ew/2) + ', ' + str(ey + ew/2) 	

				# determine which direction the mouse should move
				left = 20
				up = 20

				if ex > curX:
					left *= -1
				if ey > curY:
					up *= -1

				mouse.move(left, up)



		_,input_image = cv2.threshold(input_image,225,255,cv2.THRESH_TOZERO_INV)


		# apply canny cheese
		# roi_gray = cv2.Canny(roi_eye, 95, 100)

		# # hough detection
		# circles_found = cv2.HoughCircles(input_image, cv2.cv.CV_HOUGH_GRADIENT,11, 49)

		# print str(len(circles_found))
		# if circles_found is not None:
		# 	for (x, y, r) in circles_found:
		# 		cv2.circle(output, (x, y), r, (0, 255, 0), 5)

		cv2.imshow("don't read", input_image)

		k = cv2.waitKey(30) & 0xff
		if k == 27:
			cv2.destroyAllWindows()

