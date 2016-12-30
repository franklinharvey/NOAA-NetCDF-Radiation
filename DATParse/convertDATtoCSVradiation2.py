import sys
from os.path import basename
import os
import csv

def fileConvert(filesToProcess):
	for input in filesToProcess:
		headers = []
		Direct, Diffuse, Diffuse2, D_Global, D_IR, U_Global, U_Global2, U_IR, Zenith, check= False, False, False, False, False, False, False, False, False, False
		base = os.path.splitext(basename(input))[0]
		baseFolder = base.split('_',1)[0] + "/csv/"
		print "Processing %s" % base
		#out_name = ("../baselineRad/" + baseFolder + base + ".csv")
		out_name = "TEST.csv"
		with open(input, 'r') as input_file:
			with open(out_name, 'w') as output_file:
				for count, line in enumerate(input_file):
					if count < 4:
						words = line.split()
						for word in words:
							if word == "DIRECT":
								headers.append(word)
							if word == "DIFFUSE":
								headers.append(word)
							if word == "DIFFUSE2":
								headers.append(word)
							if word == "D_GLOBAL":
								headers.append(word)
							if word == "D_IR":
								headers.append(word)
							if word == "U_GLOBAL":
								headers.append(word)
							if word =="U_GLOBAL2":
								headers.append(word)
							if word == "U_IR":
								headers.append(word)
							if word == "Zenith":
								headers.append(word)
					else:
						if check!=True:
							writeHeaders(headers,output_file)
							check=True
						outLine = ",".join(line.split())
						output_file.write(outLine + '\n')

def writeHeaders(headers,output_file):
	headers.sort()
	output_file.write("Year,Month,Day,Hour,Minute,")
	for word in headers:
		output_file.write(word)
		if word != "Zenith":
			output_file.write(",")
	output_file.write("\n")

if __name__ == '__main__':
	fileConvert(sys.argv[1:])
