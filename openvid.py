from __future__ import division
from pathlib import Path
import cv2
import os
import getpass

def chre(filex, add=0):
	original_file = filex
	z = True
	while(z):
		if (add != 0):
			split = filex.split(".")
			part1 = split[0] + "_" + str(add)
			original_file = str(".".join([part1, split[1]]))
		if os.path.isfile(original_file):
			z = False
			break
		else:
			add += 1
			chre(original_file, add)
	return original_file

def mainov():
	filex = 'output.avi'
	filex = chre(filex)
	cap = cv2.VideoCapture(filex)
	ret, frame = cap.read()
	cap.set(cv2.CAP_PROP_FPS, 20)
	size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

	while(1):
		ret, frame = cap.read()
		cv2.namedWindow('frame', cv2.WND_PROP_FULLSCREEN)
		cv2.setWindowProperty("frame",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
		cv2.imshow('frame',frame)
		k = cv2.waitKey(30) & 0xff
		if k == 27:
			cap.release()
			cv2.destroyAllWindows()
def mainim():
	name = list(os.popen('find / -iname "*.jpg"').read().split("\n"))
	for i in name:
		img = cv2.imread(i)
		screen_res = 1280, 720
		scale_width = screen_res[0] / img.shape[1]
		scale_height = screen_res[1] / img.shape[0]
		scale = min(scale_width, scale_height)
		window_width = int(img.shape[1] * scale)
		window_height = int(img.shape[0] * scale)

		cv2.namedWindow('xxx', cv2.WINDOW_NORMAL)
		cv2.resizeWindow('xxx', window_width, window_height)

		cv2.imshow('xxx', img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
mainov()
mainim()