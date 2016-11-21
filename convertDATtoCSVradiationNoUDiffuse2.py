# Import SYS for passing input files, os.path's baseline for parsing file names, os for
import sys
from os.path import basename
import os
import csv

def fileConvert(filesToProcess):
	headers = 'Year Month Day Hour Minute Direct Diffuse2 D_Global D_IR Zenith'
	for input in filesToProcess:
		base = os.path.splitext(basename(input))[0]
		print "Processing %s" % base
		out_name = (base + ".csv")

		with open(input, 'r') as input_file:
			with open(out_name, 'w') as output_file:
				output_file.write('"%s"\n'%'","'.join(headers.split()))
				for count, line in enumerate(input_file):
					if count<4: continue
					outLine = ",".join(line.split())
					output_file.write(outLine + '\n')

if __name__ == '__main__':
	fileConvert(sys.argv[1:])
