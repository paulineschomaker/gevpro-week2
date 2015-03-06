#!/usr/bin/env python
#Pauline Schomaker, S2731517
import sys
import xml.etree.ElementTree as ET
import shutil

def main(argv):
	"""Deze functie haalt alle foute data uit het bestand en schrijft de goede data naar een nieuw bestand."""
	
	#Bestanden, tree en root#
	spontalFile = argv[1]
	outputFile = argv[2]
	shutil.copyfile(spontalFile, outputFile)
	tree = ET.parse(outputFile)
	root = tree.getroot()
	
	#BOTTOM_HZ, TOP_HZ, F0_START en F0_END assignen aan variabelen
	for POINT in root.findall('POINT'):
		bottomValue = float(POINT.find('BOTTOM_HZ').text)
		topValue = float(POINT.find('TOP_HZ').text)
		startValue = float(POINT.find('F0_START').text)
		endValue = float(POINT.find('F0_END').text)
		
	#Als F0_START EN F0_END zich niet binnen BOTTOM_HZ en TOP_HZ bevinden, wordt de foute data verwijderd.	
		if (startValue < bottomValue):
			root.remove(POINT)
		elif (startValue > topValue):
			root.remove(POINT)
		elif (endValue > topValue):
			root.remove(POINT)
		elif (endValue < bottomValue):
			root.remove(POINT)
	tree.write(outputFile)
		
if __name__ == "__main__":
	main(sys.argv)
