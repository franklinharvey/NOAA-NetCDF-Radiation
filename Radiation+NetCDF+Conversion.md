
# Converting Radiation's ".dat" files to a NetCDF file

The files found in radiations FTP server (found at ftp://ftp.cmdl.noaa.gov in /g-rad/baseline/) are organized by test sites like ALT (Alert Observatory in Alert, Nunavut, Canada; a BSRN site) and BRW (Barrow Observatory in Barrow, Alaska, United States; a baseline GMD observatory). There are six total baseline observatories and four BSRN sites. Each testing location is a directory holding a zip files, one per month. Each zip file, when unzipped, contains a single ".dat" file:

                    ALT_RAD                                                
                                                   ALT_RAD2                
                     DIRECT        D_GLOBAL        U_GLOBAL          Zenith
    Year Mn Dy Hr Mi        DIFFUSE2            D_IR            U_IR        
    2004  9  1  0  1    1.04   79.40   78.67  303.58   61.06  310.95  85.142
    2004  9  1  0  2    0.71   74.36   73.91  303.80   57.82  310.92  85.171
    2004  9  1  0  3    0.67   71.80   71.64  304.25   56.84  310.98  85.199
    2004  9  1  0  4    0.75   74.35   74.83  304.21   59.68  310.89  85.227

This is the first eight lines of the first file in the ALT directory ("alt_2004_09.dat"). The first issue is evident right away: the headers are not all on one line. In fact, some headers use two lines. This format is fairly legible to humans, but any program would have a hard time reading this. I decided the first thing to do would be to convert these files to CSV's (as most data libraries would certainly have readers for CSV's). There is an irregular amount of whitespace between columns, but I knew python wouldn't have had an issue with this.

My second issue is exemplified with these excerpts from the BAO directory:

                   BAO0_RAD                                                
                                                   BAO8_RAD                
                     DIRECT        D_GLOBAL        U_GLOBAL          Zenith
    Year Mn Dy Hr Mi         DIFFUSE            D_IR            U_IR        
    1992  1  1  0  3 -999.00 -999.00 -999.00 -999.00 -999.00 -999.00  93.734
    1992  1  1  0  6 -999.00 -999.00 -999.00 -999.00 -999.00 -999.00  94.245
    1992  1  1  0  9 -999.00 -999.00 -999.00 -999.00 -999.00 -999.00  94.758
    1992  1  1  0 12 -999.00 -999.00 -999.00 -999.00 -999.00 -999.00  95.273

                    BAO_RAD                                

                     DIRECT        D_GLOBAL          Zenith
    Year Mn Dy Hr Mi        DIFFUSE2            D_IR        
    2016  5  1  0  1    0.32  105.18  105.66  302.53  69.491
    2016  5  1  0  2    0.37   97.06   96.79  306.56  69.681
    2016  5  1  0  3    0.24   91.87   92.35  307.61  69.872
    2016  5  1  0  4    0.00   93.20   94.02  306.54  70.062

The files shown are "bao_1992_01.dat" (shown first) and "bao_2016_05.dat" (shown second). The headers change. Specifically, "DIFFUSE" changes to "DIFFUSE2". Additionally "BAO8_RAD U_GLOBAL" and "U_IR" are removed. The headers swap at the beginning of 2016.

## Converting ".dat" to ".csv"

I will take these steps: import file, parse headers, set flags for each possible header, write present headers, write data delimited by commas. Here we go:


```python
import csv #to write to a csv
from os.path import basename
import os #to get filename
```


```python
input = "../baselineRad/bao/dat/bao_1992_01.dat" #this is formatted for my directory layout, and normally would use a queue for all files in a directory
Direct, Diffuse, Diffuse2, D_Global, D_IR, U_Global, U_Global2, U_IR, Zenith, check= False, False, False, False, False, False, False, False, False, False
#set flags for all headers and a checking variable to false, these will be set to true as they are found


base = os.path.splitext(basename(input))[0] #get name of input file "bao_1992_01" in this case
baseFolder = base.split('_',1)[0] + "/csv/" #returns "bao/csv/"
out_name = ("../baselineRad/" + baseFolder + base + ".csv") #sets output to "../baselineRad/bao/csv/bao_1992_01.csv"
```


```python
def writeHeaders(output_file, Direct, Diffuse, Diffuse2, D_Global, D_IR, U_Global, U_Global2, U_IR, Zenith):
    output_file.write("Year,Month,Day,Hour,Minute,")
    if Direct:
        output_file.write("DIRECT,")
    if Diffuse:
        output_file.write("DIFFUSE,")
    if Diffuse2:
        output_file.write("DIFFUSE2,")
    if D_Global:
        output_file.write("D_GLOBAL,")
    if D_IR:
        output_file.write("D_IR,")
    if U_Global:
        output_file.write("U_GLOBAL,")
    if U_Global2:
        output_file.write("U_GLOBAL,")
    if U_IR:
        output_file.write("U_IR,")
    if Zenith:
        output_file.write("Zenith\n")

### This is the function I use to actually write the headers into the CSV ###
```


```python
with open(input, 'r') as input_file:
    with open(out_name, 'w') as output_file:
        for count, line in enumerate(input_file):
            if count < 4:
                words = line.split()
                for word in words:
                    if word == "DIRECT":
                        Direct = True
                    if word == "DIFFUSE":
                        Diffuse = True
                    if word == "DIFFUSE2":
                        Diffuse2 = True
                    if word == "D_GLOBAL":
                        D_Global = True
                    if word == "D_IR":
                        D_IR = True
                    if word == "U_GLOBAL":
                        U_Global = True
                    if word =="U_GLOBAL2":
                        U_Global2 = True
                    if word == "U_IR":
                        U_IR = True
                    if word == "Zenith":
                        Zenith = True
            else:
                if check!=True:
                    writeHeaders(output_file, Direct, Diffuse, Diffuse2, D_Global, D_IR, U_Global, U_Global2, U_IR, Zenith)
                    check=True
                outLine = ",".join(line.split())
                output_file.write(outLine + '\n')

input_file.close()
output_file.close()
```

I'll try to summarize the above snippet:

I open the .dat file and I create a .csv file to write to. I iterate through each line and check to see if I'm on a line before line 4 (python line reads are zero-based) because I know all the headers are in lines 0-3. The operation "line.split()" returns everything delimited by any whitespace, so this gets each word from the header. I then check for every header and set its flag to "true." If I've gone through the header lines I then check to see if I've already written my headers (this is what the check variable looks for). If I haven't, I write them (essentially only headers that have been found will be written). Then I split the remaining data by whitespace, delimit it by commas, and write it out.

With not much more work, you can use this script to iterate through all DAT files and write out accordingly. However, a CSV file is not our goal, NetCDF is.

## Converting CSV to NetCDF

A quick google search reveals that there are endless ways to do this, but I've decided to use xarray and pandas. My workflow was to make a dataframe from each CSV and then use that dataframe to export out to a NetCDF file. I chose this method because of how flexible a dataframe is. For instance, a dataframe could contain all the data from a testing location (even with the changing headers) or even all the radiation data in total. Here is what I did:


```python
import pandas as pd
import xarray as xr
from os.path import basename
import os
```


```python
input = "alt_2004_09.csv"
df1=pd.DataFrame()
out_name = "test.nc"
df1 = pd.read_csv(input,
    sep=",",
    parse_dates = {"Date":[0,1,2,3,4]},
    date_parser=lambda x:pd.to_datetime(x,format="%Y %m %d %H %M"),
    index_col=['Date'])
df1.loc[:,"TestSite"]="ALT"
xds=xr.Dataset.from_dataframe(df1)
xds.to_netcdf(out_name)
```

Essentially the file is separated by commas, the date is parsed (and used as an index), and the testing location is added into a column. This should return a .nc file.
