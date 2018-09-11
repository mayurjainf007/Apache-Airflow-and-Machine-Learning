import cv2
import os
from pathlib import Path

def chre(filex, add=0):
	original_file = filex
	z = True
	while(z):
		if (add != 0):
			split = filex.split(".")
			part1 = split[0] + "_" + str(add)
			original_file = str(".".join([part1, split[1]]))
		if os.path.isfile(original_file):
			add += 1
			chre(original_file, add)
		else:
			z = False
			break
	return original_file

def mainvi():
	os.chdir(file)
	filex = 'output.avi'
	cap = cv2.VideoCapture(0)
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	filey = chre(filex)
	out = cv2.VideoWriter(filey, fourcc, 20.0, (640,480))
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		out.write(frame)
		cv2.imshow('frame',gray)
		if cv2.waitKey(30) & 0xff == ord('q'):
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()

mainvi()
