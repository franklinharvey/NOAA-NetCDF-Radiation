from os.path import basename
import os
import netCDF4 as nc
import sys
import csv
import pandas as pd

def openFile(filesToProcess):
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    counter = 0
    for input in filesToProcess:
        base = os.path.splitext(basename(input))[0]
        print "Working on %s" % base
        with open(input, 'r') as input_file:
            #row_count = sum(1 for row in input_file)
            if counter == 0:
                df1 = createDataFrame(input_file)
            else:
                df2 = createDataFrame(input_file)
                df1 = pd.concat([df1,df2])
                del df2
        counter += 1
        input_file.close()
    print "Working on the output"
    df1.to_csv('../baselineRad/large.csv')
    del df1
    del df2

def createDataFrame(input_file):
    df1 = pd.read_csv(input_file,
            sep = ",",
            #nrows = 5000000,
            index_col = ['TestSite','Date'])
    return df1

if __name__ == '__main__':
    openFile(sys.argv[1:])
