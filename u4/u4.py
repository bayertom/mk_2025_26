from numpy import *
from pyproj import *

def project(proj_name, R_z, lat, lon, lat0):
    # Create new projection
    my_proj =  Proj(proj=proj_name, R=R_z, lat_1 = lat0)

    # Project point calculation
    [X,Y] = my_proj(lon, lat)

    #Distortions
    dist = my_proj.get_factors(lon, lat)
    a = dist.tissot_semimajor
    b = dist.tissot_semiminor

    return X, Y, a, b 

#Define projection
proj_name = "sinu"
R = 6380000
lat0 = 10

#Define grid
lat_min = -80
lat_max = 80
lon_min = -180
lon_max = 180
nlat = 10
nlon = 10


#Create intervals
lat = linspace(lat_min, lat_min, nlat)
lon = linspace(lon_min, lon_min, nlon)

#Create  meshgrid
latg, long = meshgrid(lat, lon)

#Project meshgrid
X, Y, a, b = project(proj_name, R, latg, long, lat0)

print(X)
