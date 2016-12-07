# -*- coding: utf-8 -*-
import time
from time import sleep
import netCDF4 as nc
import sys
from os.path import basename
import os
import csv
import numpy as np
import pandas as pd

def openFile(filesToProcess):
    counter = 0
    df1 = pd.DataFrame()
    length = len(filesToProcess)
    printProgress(counter, length, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
    for input in filesToProcess:
        sleep(0.1)
        printProgress(counter, length, prefix = 'Progress:', suffix = 'Complete', barLength = 50)
        base = os.path.splitext(basename(input))[0]
        if counter<1:
            output_name = base.split('_',1)[0]
            #print "There are %d files to precess in %r" % (len(filesToProcess), output_name)
        with open(input, 'r') as input_file:
            counter+=1
            #print "Processing %s -- Request # %d / %d" % (base, counter, len(filesToProcess))
            if counter < 2:
                df1 = createDataFrame(input_file, counter)
                df1.loc[:,'testsite'] = output_name
            else:
                df2 = createDataFrame(input_file, counter)
                df1 = pd.concat([df1,df2])
        input_file.close()
    df1.replace(to_replace="-999.00",value="NaN", inplace=True)
    df1.to_csv("../baselineRad/large csv/" + output_name + '.csv')

def createDataFrame(input_file, counter):
    checkTime = time.clock()
    #print "Start DataFrame -- #%d" % counter
    df1 = pd.read_csv(input_file,
            sep = ",",
            parse_dates = {'Date': [0,1,2,3,4]},
            date_parser = lambda x: pd.to_datetime(x, format="%Y %m %d %H %M"),
            index_col = ['Date'])
    #print "End DataFrame -- #%d" % counter
    #print "Ran for " + str(time.clock() - checkTime) + " Seconds"
    return df1

def printProgress (iteration, total, prefix = '', suffix = '', decimals = 1, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(barLength * iteration / float(total)))
    bar = '█' * filled_length + '-' * (barLength - filled_length)
    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()

if __name__ == '__main__':
    runTime = time.clock()
    openFile(sys.argv[1:])
    runTime =  time.clock() - runTime
    m, s = divmod(runTime, 60)
    h, m = divmod(m, 60)
    print "Runtime -- %d:%02d:%02d" % (h,m,s)
