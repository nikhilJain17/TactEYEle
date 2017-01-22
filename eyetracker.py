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


eyeX = 0
eyeY = 0

newEyeX = 0
newEyeY = 0

calibrated_X = 0
calibrated_Y = 0

while True:
	# update the mouse position

	curX = mouse.position[0]
	curY = mouse.position[1]
	# print 'MOUSE AT: ' + str(curX) + ', ' + str(curY)

	ret, input_image = capture.read()


	# search only within the face for der eyes
	face_cascade = cv2.CascadeClassifier('haarcascade_face.xml')
	eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
	face_found = face_cascade.detectMultiScale(input_image, 1.3, 5)

	# print 'testetetset ' + str((face_found[0])[0])
	input_image = cv2.cvtColor(input_image,cv2.COLOR_RGB2GRAY)


	pupilFrame = input_image
	pupilO = pupilFrame
	windowClose = numpynav.ones((5,5), numpynav.uint8)
	windowOpen = numpynav.ones((2,2), numpynav.uint8)
	windowErode = numpynav.ones((2,2), numpynav.uint8)
 
	for (x, y, w, h) in face_found:

		x = (face_found[0])[0]
		y = (face_found[0])[1]
		w = (face_found[0])[2]
		h = (face_found[0])[3]

		# make the contrast wild af
		pupilFrame = cv2.equalizeHist(input_image[y+(h/4):(y+h), x:(x+w)])
		pupilO = pupilFrame

		# threshold the goods like a door
		# needed for morphology
		_, pupilFrame = cv2.threshold(pupilFrame, 55, 255, cv2.THRESH_BINARY)

		# apply some MORPHOLOGIES
		# get rid of noise both inside and outside of the img
		pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_CLOSE, windowClose) # get rid of most crap inside the img (foreground)
		pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_ERODE, windowErode) # thin those boundaries boi
		pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_OPEN, windowOpen) # get rid of crap outside the img (background)

		# find all the fwacking blobs, some of them are the pewpils
		blobs = cv2.inRange(pupilFrame, 250, 255) # get all the blobs that are dark af (remember we binary thresholded them to be dark)

		# find all the contours (basically shapes) in the img, and approximate the points between the middle to save data
		countours, hierarchy = cv2.findContours(blobs, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

		# print countours

		# advanced blob analysis techniques
		# only finds the right pupil
		# but do we really need anything else
		# then again, do we really need anything?
 
		# delete the biggest blob
		if len(countours) >= 2:
			# find the biggest blob
			maxArea = 0
			maIndex = 0
			distanceX = [] # delete the left-most blob 
			curIndex = 0
			for count in countours:
				area = cv2.contourArea(count)
				center = cv2.moments(count)

				# AHHHHHHHHHHHHH
				if center['m00'] != 0:
					cx,cy = int(center['m10']/center['m00']), int(center['m01']/center['m00'])

				distanceX.append(cx)
				if area > maxArea:
					maxArea = area
					maIndex = curIndex

				curIndex += 1

			del countours[maIndex]
			del distanceX[maIndex]


		# delete the leftmost blobhinav
		if len(countours) >= 2:
			edgeOfReality = distanceX.index(min(distanceX))
			del countours[edgeOfReality]
			del distanceX[edgeOfReality]

		# get lwargest blawb
		if len(countours) >= 1:
			maxArea = 0
			for count in countours:
				area = cv2.contourArea(count)
				if area > maxArea:
					maxArea = area
					largeblawb = count

		if len(largeblawb) > 0:
			center = cv2.moments(largeblawb)
			
			# calibrate the foirst time
			if (calibrated_X == 0):
				calibrated_X = newEyeX
			
			if (calibrated_Y == 0):
				calibrated_Y = newEyeY

			# they now have the old values
			eyeX = newEyeX
			eyeY = newEyeY

			# update the new values
			newEyeX,newEyeY = int(center['m10']/center['m00']), int(center['m01']/center['m00'])
			# cv2.circle(pupilO, (cx, cy), 5, 255, -1)
			print str(newEyeX) + ', ' + str(newEyeY)


		eyes = eye_cascade.detectMultiScale(pupilFrame)
		for (x, y, w, h) in eyes:
			cv2.rectangle(pupilFrame, (x + ex, y + ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
		# print str(eyeX) + ', ' + str(eyeY) + '_____' + str(newEyeX) + ', ' + str(newEyeY)
 		
		# move the mouse but not the rat
		# compare the old and new x,y values to determine the direction
		# set a threshold so random jitters won't change it
		# left = 0
		# up = 0
		# THRESHOLD = 1
		# NEG_THRESH = -1

		# output = ''
		# if (newEyeX - calibrated_X > THRESHOLD):
		# 	left = 20
		# 	output += 'left'
		# elif (newEyeX - calibrated_X < NEG_THRESH):
		# 	left = -20
		# 	output += 'right'

		# if (newEyeY - calibrated_Y > THRESHOLD):
		# 	up = 20
		# 	output += '___up'
		# elif (newEyeY - calibrated_Y < NEG_THRESH):
		# 	up = -20
		# 	output += '___down'

		# print output
		# mouse.move(left, up)
		# print 'MOUSE---------' + str(mouse.position)

 	cv2.namedWindow('DO NOT READ', cv2.WINDOW_NORMAL)
 	# cv2.resizeWindow('DO NOT READ', 300, 300)
 	cv2.imshow('DO NOT READ', pupilFrame)
 	

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		cv2.destroyAllWindows()

