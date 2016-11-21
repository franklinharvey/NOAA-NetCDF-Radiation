import netCDF4 as nc
import sys
import csv
import numpy as np

def openFile(filesToProcess):
    for input in filesToProcess:
        input_file = csv.reader(input)
        row_count = sum(1 for row in input_file)

def createDataFrame(input_file, counter):
    checkTime = time.clock()
    #print "Start DataFrame -- #%d" % counter
    df1 = pd.read_csv(input_file,
            na_values = '-999.00',
            sep = ",",
            index_col = ['Date'])
    #print "End DataFrame -- #%d" % counter
    #print "Ran for " + str(time.clock() - checkTime) + " Seconds"
    return df1

if __name__ == '__main__':
    openFile(sys.argv[1:])
