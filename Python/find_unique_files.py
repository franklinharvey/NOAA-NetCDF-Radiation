import sys
import csv
import csv_convert

def file_mgmt(filesToProcess):
    headerList = []
    fileList = []
    for input in filesToProcess:
        fileName = csv_convert.get_filename(input)
        with open(input) as input_file:
            reader = csv.reader(input_file)

            rownum = 0
            noMatch = True
            for row in reader:
                if rownum == 0:
                    for entry in headerList:
                        if entry == row:
                            noMatch = False
                    if noMatch:
                        headerList.append(row)
                        fileList.append(fileName)
                    rownum+=1
                else:
                    break

    with open("filetype.csv",'w') as output_file:
        output_file.write("Example File,Headers\n")
        for count,file in enumerate(fileList):
            output_file.write("%s,%s\n" % (file,headerList[count]))
if __name__ == '__main__':
	df = file_mgmt(sys.argv[1:])
