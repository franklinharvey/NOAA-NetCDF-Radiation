"""
This module should accept .dat files and return .csv files.
"""

import sys
from os.path import basename
import os
import csv
import dat_parse

def file_mgmt(filesToProcess):
	"""Initial function, used to seperate list of files from single file input."""
	if len(filesToProcess)>1: # if list of 2 or more files
		for input in filesToProcess:
			dat_to_csv(input)
	else: # if just single file
		dat_to_csv(filesToProcess[0])

def get_headers(input):
	"""Parses headers in .dat file and returns them comma seperated."""
	instanceList = dat_parse.get_instancelist(input)
	instanceList = dat_parse.sort_instancelist(instanceList)
	instanceList = dat_parse.filter_instancelist(instanceList)
	return dat_parse.get_csvheaders(instanceList)

def dat_to_csv(input):
	"""Converts .dat to .csv file"""
	base = os.path.splitext(basename(input))[0]
	baseFolder = base.split('_',1)[0] + "/csv/"
	headers = get_headers(input)

	print "Processing %s" % base
	out_name = ("../../baselineRad/" + baseFolder + base + ".csv")

	with open(input, 'r') as input_file:
		with open(out_name, 'w') as output_file:
			output_file.write(headers + "\n")
			for count, line in enumerate(input_file):
				if count < 4:
					pass
				else:
					if line.split()[0]=='\x1a':
						pass
					else:
						outLine = ",".join(line.split())
						output_file.write(outLine + '\n')

if __name__ == '__main__':
	file_mgmt(sys.argv[1:])
