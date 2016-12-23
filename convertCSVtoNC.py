import pandas as pd
import xarray as xr
import sys
from os.path import basename
import os

def openFile(filesToProcess):
    counter = 0
    for input in filesToProcess:
        counter+=1
        df1=pd.DataFrame()
        base = os.path.splitext(basename(input))[0]
        if counter < 2:
            baseFolder = base.split('_',1)[0] + "/nc/"
        out_name = ("../baselineRad/" + baseFolder + base + ".nc")
        df1 = pd.read_csv(input,
            sep=",",
            parse_dates = {"Date":[0,1,2,3,4]},
            date_parser=lambda x:pd.to_datetime(x,format="%Y %m %d %H %M"),
            index_col=['Date'])
        df1.loc[:,"TestSite"]="ALT"
        xds=xr.Dataset.from_dataframe(df1)
        xds.to_netcdf(out_name)
        print out_name
        del df1
        xds.close()

if __name__ == '__main__':
    openFile(sys.argv[1:])
    print "done"
