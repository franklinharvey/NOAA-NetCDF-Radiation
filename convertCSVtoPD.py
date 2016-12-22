# -*- coding: utf-8 -*-
from time import clock
import netCDF4 as nc
import sys
from os.path import basename
import os
import csv
import pandas as pd

def openFile(filesToProcess):
    counter = 0
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    length = len(filesToProcess)
    for input in filesToProcess:
        base = os.path.splitext(basename(input))[0]
        if counter<1:
            output_name = base.split('_',1)[0]
            sys.stdout.write("There are %d files to precess in %r\n" % (len(filesToProcess), output_name))
        with open(input, 'r') as input_file:
            counter+=1
            sys.stdout.write("Processing %s -- Request # %d / %d" % (base, counter, len(filesToProcess)))
            sys.stdout.write('\n')
            if counter < 2:
                df1 = createDataFrame(input_file, output_name)
            else:
                df2 = createDataFrame(input_file, output_name)
                df1 = pd.concat([df1,df2])
        input_file.close()
    df1 = DataFrameReplaceValues(df1)
    df1.to_csv("../baselineRad/large csv/" + output_name + '.csv')
    del df1
    del df2

def createDataFrame(input_file, output_name):
    checkTime = time.clock()
    df1 = pd.read_csv(input_file,
            sep = ",",
            parse_dates = {'Date': [0,1,2,3,4]},
            date_parser = lambda x: pd.to_datetime(x, format="%Y %m %d %H %M"),
            index_col = ['Date'])
    df1.loc[:,'TestSite'] = output_name
    return df1

def DataFrameReplaceValues(df1):
    df1.replace(to_replace="-999.00",value="NaN", inplace=True)
    df1.replace(r'\s+',"NaN", inplace=True, regex=True)
    return df1

if __name__ == '__main__':
    runTime = time.clock()
    openFile(sys.argv[1:])
    runTime =  time.clock() - runTime
    m, s = divmod(runTime, 60)
    h, m = divmod(m, 60)
    print "Runtime -- %d:%02d:%02d" % (h,m,s)
