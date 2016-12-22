import scipy
import numpy
import netCDF4
import csv
from numpy import arange, dtype

def str_to_float(str):
    try:
        number = float(str)
    except ValueError:
        number = -999.00
    return number

v1 = []
v2 = []
v3 = []
v4 = []
v5 = []
v6 = []
v7 = []
v8 = []

f = open('../baselineRad/alt/csv/alt_2004_09.csv').readlines()

for line in f[1:]:
    fields = line.split(',')
    v1.append(fields[0]) #date
    v2.append(str_to_float(fields[1]))#direct
    v3.append(str_to_float(fields[2]))#diffuse
    v4.append(str_to_float(fields[3]))#dglobal
    v5.append(str_to_float(fields[4]))#d_ir
    v6.append(str_to_float(fields[5]))#UGLOBAL
    v7.append(str_to_float(fields[6]))#U_IR
    v8.append(str_to_float(fields[7]))#ZENITH

ncout = netCDF4.Dataset('out.nc', 'w')

directOut = arange(v2, dtype='float32')
#diffuseOut = arange(v3, dtype='float32')
#zenithOut = arange(v4, dtype='float32')

direct = ncout.createVariable('direct',dtype('float32').char)
#diffuse = ncout.createVariable('diffuse',dtype('float32').char)
#zenith = ncout.createVariable('zenith',dtype('float32').char)

direct.units = 'irradiance'
#diffuse.units = 'irradiance'
#zenith.units = 'degrees'

direct[:] = directOut
#diffuse[:] = diffuseOut
#zenith[:] = zenithOut

ncout.close()
f.close()
