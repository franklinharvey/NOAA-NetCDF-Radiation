import pandas as pd
import xarray as xr
import sys
from os.path import basename
import os

def openFile(filesToProcess):
    counter = 0
    for input in filesToProcess:
        base = os.path.splitext(basename(input))[0]
        if counter == 0:
            baseFolder = base.split('_',1)[0] + "/nc/"
        df1=pd.DataFrame()
        out_name = ("../baselineRad/" + baseFolder + base + ".nc")
        df1 = pd.read_csv(input,
            sep=",",
            parse_dates = {"Date":[0,1,2,3,4]},
            date_parser=lambda x:pd.to_datetime(x,format="%Y %m %d %H %M"),
            index_col=['Date'])
        df1.loc[:,"TestSite"]="ALT"

        df1 = DataFrameReplaceValues(df1)
        xds=xr.Dataset.from_dataframe(df1)
        xds.to_netcdf(out_name)
        print base
        del df1
        xds.close()
        counter+=1


def DataFrameReplaceValues(df1):
    df1.replace(to_replace="-999.00",value="NaN", inplace=True)
    df1.replace(r'\s+',"NaN", inplace=True, regex=True)
    return df1

if __name__ == '__main__':
    openFile(sys.argv[1:])
    print "done"
