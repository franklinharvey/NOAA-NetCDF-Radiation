import sys
from os.path import basename
import os
import csv
import datParse

def getHeaders(input):
	"""Parses headers in .dat file and returns them comma seperated."""
	instanceList = datParse.getInstanceList(input)
	instanceList = datParse.sortInstanceList(instanceList)
	instanceList = datParse.filterInstanceList(instanceList)
	return datParse.getCSVHeaders(instanceList)

def fileMGMT(filesToProcess):
	if len(filesToProcess)>1:
		for input in filesToProcess:
			fileConvert(input)
	else:
		fileConvert(filesToProcess[0])

def fileConvert(input):
	"""Converts .dat to .csv file"""
	base = os.path.splitext(basename(input))[0]
	baseFolder = base.split('_',1)[0] + "/csv/"
	headers = getHeaders(input)

	print "Processing %s" % base
	out_name = ("../baselineRad/" + baseFolder + base + ".csv")

	with open(input, 'r') as input_file:
		with open(out_name, 'w') as output_file:
			output_file.write(headers + "\n")
			for count, line in enumerate(input_file):
				if count < 4:
					pass
				else:
					outLine = ",".join(line.split())
					output_file.write(outLine + '\n')

if __name__ == '__main__':
	fileMGMT(sys.argv[1:])
