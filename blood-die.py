#!/usr/bin/env python
#Pauline Schomaker, S2731517
from collections import namedtuple
import json
import sys

def main(argv):
	fname = json.load(open(argv[1]))
	taalData = namedtuple('Language','Taal, Blood, Die')
	resultlist = []
	for item in fname:
		Taal = item[0].strip()
		Blood = str(item[2]).split()
		Die = str(item[3]).split()
		for elem in Blood:
			if elem in Die:
				for elem in Die:
					if elem in Blood:
						resultlist.append(taalData(Taal,Blood, Die))
	print (resultlist)
	#print ("{:5} {:5} {:5}".format([taalData for item in resultlist]))
		
if __name__== "__main__":
	main(sys.argv)
