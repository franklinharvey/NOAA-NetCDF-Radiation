import sys
from os.path import basename
import os
import csv
import datParse

def fileConvert(filesToProcess):
	for input in filesToProcess:
		instanceList = datParse.getInstanceList(input)
		instanceList = datParse.sortInstanceList(instanceList)
		instanceList = datParse.filterInstanceList(instanceList)
		headers = datParse.getCSVHeaders(instanceList)

		base = os.path.splitext(basename(input))[0]
		baseFolder = base.split('_',1)[0] + "/csv/"

		print "Processing %s" % base
		#out_name = ("../baselineRad/" + baseFolder + base + ".csv")
		out_name = "TEST.csv"

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
	fileConvert(sys.argv[1:])
