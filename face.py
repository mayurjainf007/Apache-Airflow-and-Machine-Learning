import numpy as np
import cv2
import os
import time

def mainf():
	fac_cascade = cv2.CascadeClassifier('xmls/haarcascade_frontalface_default.xml')
	eye_cascade = cv2.CascadeClassifier('xmls/haarcascade_eye.xml')
	cap = cv2.VideoCapture(0)
	while 1:
		ret, img = cap.read()
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = fac_cascade.detectMultiScale(gray)
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			roi_gray = gray[y:y+h, x:x+w]
			roi_color = img[y:y+h, x:x+w]
			eyes = eye_cascade.detectMultiScale(roi_gray)
			for (ex,ey,ew,eh) in eyes:
				cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
		cv2.imshow('img',img)
		if cv2.waitKey(1):
			time.sleep(1)
			s,im = cap.read()
			cv2.imwrite('user.jpg',im)
			break
	cap.release()
	cv2.destroyAllWindows()
mainf()
