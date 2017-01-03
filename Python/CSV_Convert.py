import time
import sys
from os.path import basename
import os
import csv
import pandas as pd
import xarray as xr

def fileMGMT(filesToProcess):
	"""Initial function, used to seperate list of files from single file input."""
	if len(filesToProcess)>1: # if list of 2 or more files
		for input in filesToProcess:
			fileConvert(input)
	else: # if just single file
		fileConvert(filesToProcess[0])

def fileConvert(input):
    base = os.path.splitext(basename(input))[0]
    masterDF = pd.DataFrame()
    with open(input, 'r') as input_file:
        tempDF = createDataFrame(input_file, testSite)
    masterDF = pd.concat([masterDF,tempDF])
    return masterDF

def getBaseName(input):
    """Returns the name of the file without the file extension"""
    return os.path.splitext(basename(input))[0]

def getTestSite(base):
    """Returns the name of the testing location"""
    return base.split('_',1)[0]

def openFile(filesToProcess):
    counter = 0
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    length = len(filesToProcess)
    for input in filesToProcess:
        base = os.path.splitext(basename(input))[0]
        if counter<1:
            testSite = base.split('_',1)[0]
            sys.stdout.write("There are %d files to precess in %r\n" % (len(filesToProcess), output_name))
        with open(input, 'r') as input_file:
            counter+=1
            sys.stdout.write("Processing %s -- Request # %d / %d" % (base, counter, len(filesToProcess)))
            sys.stdout.write('\n')
            if counter < 2:
                df1 = createDataFrame(input_file, testSite)
            else:
                df2 = createDataFrame(input_file, testSite)
                df1 = pd.concat([df1,df2])
        input_file.close()
    df1 = DataFrameReplaceValues(df1)
    df1.to_csv("../../baselineRad/large csv/" + testSite + '.csv')
    writeNetCDF(df1,base)
    del df1
    del df2

def createDataFrame(input_file, testSite):
    checkTime = time.clock()
    df1 = pd.read_csv(input_file,
            sep = ",",
            parse_dates = {'Date': [0,1,2,3,4]},
            date_parser = lambda x: pd.to_datetime(x, format="%Y %m %d %H %M"),
            index_col = ['Date'])
    df1.loc[:,'TestSite'] = testSite
    return df1

def DataFrameReplaceValues(df1):
    """Checks for values and returns a DataFrame with "NaN" values in their place"""
    df1.replace(to_replace="-999.00",value="NaN", inplace=True)
    df1.replace(r'\s+',"NaN", inplace=True, regex=True)
    return df1

def writeNetCDF(df1,out_name):
    """Writes a NetCDF4 file using the CSV input"""
    xds = xr.Dataset.from_dataframe(df1)
    xds.to_netcdf(out_name + '.nc')

if __name__ == '__main__':
    runTime = time.clock()
    fileMGMT(sys.argv[1:])
    runTime =  time.clock() - runTime
    m, s = divmod(runTime, 60)
    h, m = divmod(m, 60)
    print "Runtime -- %d:%02d:%02d" % (h,m,s)
