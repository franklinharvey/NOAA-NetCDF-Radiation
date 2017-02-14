import sys
from os.path import basename
import os
import netCDF4 as nc

def file_mgmt(filesToProcess):
    for input in filesToProcess:
        print input
        foo=nc.Dataset(input,'r+')
        foo.Conventions='CF-1.6'
        foo.title = 'NOAA/ESRL/GMD/GRAD Radiation Archive - %s' % (get_testsite(input))
        foo.source = 'https://github.com/franklinharvey/NOAA-NetCDF-Radiation'
        foo.comment="Converted from .dat file in the radiation group's FTP server"

def get_filename(input):
	"""Returns the name of the file without the file extension"""
	return os.path.splitext(basename(input))[0]

def get_testsite(input):
	"""Returns the name of the testing location"""
	base = get_filename(input)
	return base.split('_',1)[0]

if __name__ == '__main__':
	df = file_mgmt(sys.argv[1:])
