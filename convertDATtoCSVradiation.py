# Import SYS for passing input files, os.path's baseline for parsing file names, os for
import sys
from os.path import basename
import os
import csv

def fileConvert(filesToProcess):
	for input in filesToProcess:
		Direct, Diffuse, Diffuse2, D_Global, D_IR, U_Global, U_IR, Zenith, check= False, False, False, False, False, False, False, False, False
		base = os.path.splitext(basename(input))[0]
		baseFolder = base.split('_',1)[0] + "/csv/"
		print "Processing %s" % base
		out_name = ("../baselineRad/" + baseFolder + base + ".csv")
		with open(input, 'r') as input_file:
			with open(out_name, 'w') as output_file:
				for count, line in enumerate(input_file):
					if count < 4:
						words = line.split()
						for word in words:
							if word == "DIRECT":
								Direct = True
							if word == "DIFFUSE":
								Diffuse = True
							if word == "DIFFUSE2":
								Diffuse2 = True
							if word == "D_GLOBAL":
								D_Global = True
							if word == "D_IR":
								D_IR = True
							if word == "U_GLOBAL":
								U_Global = True
							if word == "U_IR":
								U_IR = True
							if word == "Zenith":
								Zenith = True
					else:
						if check!=True:
							writeHeaders(output_file, Direct, Diffuse, Diffuse2, D_Global, D_IR, U_Global, U_IR, Zenith)
							check=True
						outLine = ",".join(line.split())
						output_file.write(outLine + '\n')

def writeHeaders(output_file, Direct, Diffuse, Diffuse2, D_Global, D_IR, U_Global, U_IR, Zenith):
	output_file.write("Year,Month,Day,Hour,Minute,")
	if Direct:
		output_file.write("DIRECT,")
	if Diffuse:
		output_file.write("DIFFUSE,")
	if Diffuse2:
		output_file.write("DIFFUSE2,")
	if D_Global:
		output_file.write("D_GLOBAL,")
	if D_IR:
		output_file.write("D_IR,")
	if U_Global:
		output_file.write("U_GLOBAL,")
	if U_IR:
		output_file.write("U_IR,")
	if Zenith:
		output_file.write("Zenith\n")

if __name__ == '__main__':
	fileConvert(sys.argv[1:])
