import json
from collections import Counter
from heapq import nlargest
from pathlib import Path

data_folder = Path()
def read():
	con = []
	json_data=open(data_folder / 'geo.txt').read()
	data = json.loads(json_data)
	for i in range(len(data)):
		con.append(data[i]['country'])
	with open(data_folder / 'country.txt', 'w+') as filehandle:  
	    json.dump(con, filehandle)

def top_10():
	file=open(data_folder / 'country.txt', 'r')
	wordcount={}
	for word in file.read().split(','):
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1
	top10 = nlargest(10, wordcount, key=wordcount.get)
	print(top10)

#read()
#top_10()
