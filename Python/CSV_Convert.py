import sys
from os.path import basename
import os
import csv
import pandas as pd
import xarray as xr

def file_mgmt(filesToProcess):
	"""Initial function, used to seperate list of files from single file input."""
	if len(filesToProcess)>1: # if list of 2 or more files
        masterDF = pd.DataFrame()
        for input in filesToProcess:
            with open(input, 'r') as input_file:
                tempDF = csv_to_df(input_file)
            masterDF = pd.concat([masterDF,tempDF])
	else: # if just single file
		masterDF = csv_to_df(filesToProcess[0])

def get_basename(input):
    """Returns the name of the file without the file extension"""
    return os.path.splitext(basename(input))[0]

def get_testsite(base):
    """Returns the name of the testing location"""
    return base.split('_',1)[0]

def csv_to_df(input_file):
    """Returns a pandas DataFrame from a .csv file"""
    testSite = getTestSite(input_file)
    df1 = pd.read_csv(input_file,
            sep = ",",
            parse_dates = {'Date': [0,1,2,3,4]},
            date_parser = lambda x: pd.to_datetime(x, format="%Y %m %d %H %M"),
            index_col = ['Date'])
    df1.loc[:,'TestSite'] = testSite
    return df1

def replace_nan(df1):
    """Checks for values and returns a DataFrame with "NaN" values in their place"""
    df1.replace(to_replace="-999.00",value="NaN", inplace=True)
    df1.replace(r'\s+',"NaN", inplace=True, regex=True)
    return df1

def df_to_nc(df1,out_name):
    """Writes a NetCDF4 file from a DataFrame input"""
    xds = xr.Dataset.from_dataframe(df1)
    xds.to_netcdf(out_name + '.nc')

if __name__ == '__main__':
    fileConvert(sys.argv[1:])
