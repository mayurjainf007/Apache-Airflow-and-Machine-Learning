import os	
import subprocess
import time
import datetime

def end():
	#subprocess.call(['gnome-terminal'], env=os.environ)
	now = datetime.datetime.now()
	os.system("echo '0%' ")
	time.sleep(5)
	os.system("echo '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' ")
	time.sleep(1)
	os.system("echo '100%' ")
	os.system("echo '\nProcess Terminated' ")
	os.system("echo 'Thank You For Your Patience!!!' ")
	os.system("date")
	time.sleep(1)
end()
