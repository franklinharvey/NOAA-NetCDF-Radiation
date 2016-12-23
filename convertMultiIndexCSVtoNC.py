import pandas as pd
import xarray as xr
import sys
from os.path import basename
import os

def openFile(filesToProcess):
    for input in filesToProcess:
        df1=pd.DataFrame()
        base = os.path.splitext(basename(input))[0]
        out_name = ("../baselineRad/largeNC/" + base + ".nc")
        df1 = createDataFrame(input)
        xds=xr.Dataset.from_dataframe(df1)
        xds.to_netcdf(out_name)

def createDataFrame(input_file):
    df1 = pd.read_csv(input_file,
            sep = ",",
            nrows = 5000,
            index_col = ['TestSite','Date'])
    return df1

if __name__ == '__main__':
    openFile(sys.argv[1:])
    print "done"
