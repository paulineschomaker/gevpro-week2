#!/usr/bin/env python
#Pauline Schomaker, s2731517
import sys

class Country():
	
	def __init__(self, name):
		self.name = name
		
	def __str__(self):
		return "Hello from {0}".format(self.name)
		print("hallo")
		
def main(argv):
	country = Country(argv[1])
	print(country)
if __name__ == '__main__':
	main(sys.argv)
	
	
	
