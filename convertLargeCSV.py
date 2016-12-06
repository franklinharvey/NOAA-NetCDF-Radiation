from os.path import basename
import os
import netCDF4 as nc
import time
import sys
import csv
import pandas as pd
import numpy as np

def openFile(filesToProcess):
    df1 = pd.DataFrame()
    counter = 0
    for input in filesToProcess:
        print "1st check"
        base = os.path.splitext(basename(input))[0]
        print "Working on %s" % base
        with open(input, 'r') as input_file:
            #row_count = sum(1 for row in input_file)
            if counter == 0:
                print "2check"
                df1 = createDataFrame(input_file, counter)
            else:
                print "3check"
                df2 = createDataFrame(input_file, counter)
                df1 = pd.concat([df1,df2])
                print "4check"
        counter += 1
        input_file.close()
        print "5check"
    df1.to_csv('large.csv')

def createDataFrame(input_file, counter):
    checkTime = time.clock()
    print "Start DataFrame -- #%d" % counter
    df1 = pd.read_csv(input_file,
            sep = ",",
            #nrows = 5000,
            index_col = ['Date'])
    print "End DataFrame -- #%d" % counter
    print "Ran for " + str(time.clock() - checkTime) + " Seconds"
    return df1

if __name__ == '__main__':
    openFile(sys.argv[1:])
