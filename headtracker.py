# BACKUP PLAN OF THE CENTURY

import cv2
import numpy as np
import uuid
import PIL
from PIL import Image
from pynput.mouse import Button, Controller


def main():
	# import the cascades 
	face_cascade = cv2.CascadeClassifier('haarcascade_face.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

	mouse = Controller()

	# load the webcam feed
	capture = cv2.VideoCapture(0)

	while True:
		ret, img = capture.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # array with found faces

		# draw lines, put your face there
		imgHeight = img.shape[0]
		imgWidth = img.shape[1]
		# print  
		cv2.line(img, (imgWidth/2, 0), (imgWidth/2, imgHeight), (40, 100, 123), 7)
		cv2.line(img, (0, imgHeight/3), (imgWidth, imgHeight/3), (40, 100, 123), 7)

		for (x, y, w, h) in faces:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

			roi = gray[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi)

			if len(eyes) == 1:
				mouse.click(Button.left, 1)

			# counter = 0
   			for (ex,ey,ew,eh) in eyes:

				# counter += 1
				# if (counter > 2):
				# 	break

				# two false cases for eyes
				notLower = (y + h/3) > (y + ey)
				# notMiddle = abs((x + ex) - (x + w/2)) > 30 
								
				if (notLower):# and notMiddle):
					cv2.rectangle(img, (x + ex, y + ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

			# print str(x) + ', ' + str(y)

			# face right = screen left
		
			difLeft = (x+w/2) - (imgWidth/2) 
			# print str(difLeft)  

			if (difLeft > 20):
				# left = (imgWidth/2 - 20) - x # left = 530 - x for variable movement
				print 'left'
			elif (difLeft < -20):
				# left = (imgWidth/2 + 20) - x
				print 'right'
			else:
				print 'neither'

			difUp = (y + h/2) - (imgHeight/2)
			if (difUp < -20):
				print 'up'

			elif (difUp > 20):
				print 'down'

			print str(difLeft) + ', ' + str(difUp)
			# if (abs(difLeft) > 13 and abs(difUp) > 6):
			# 	# within bounds
			# 	if (mouse.position[0] > 5 and mouse.position[0] < 1395):
			# 		mouse.move(-1 * difLeft, difUp)
			if (abs(difLeft) > 10):
				mouse.move(-0.7 * difLeft, 0)
				if mouse.position[0] < 10:
					mouse.move(15, 0)
				elif mouse.position[0] > 1390:
					mouse.move(-15, 0)
			if (abs(difUp) > 10):
				mouse.move(0, .5 * difUp)


		# cv2.resizeWindow('img', 1400, 800)
		cv2.imshow('img', img)

		# to break program with esc key
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			cv2.destroyAllWindows()


main()