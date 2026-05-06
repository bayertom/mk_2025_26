from numpy import *
from pyproj import *
from matplotlib.pyplot import *

def project(proj_name, R_z, lat, lon, lat0):
    # Create new projection given by proj_name
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
#proj_name = "bonne"
#proj_name = "eck5"
#proj_name = "wintri"
#proj_name = "aitoff"

R = 6380000
lat0 = 10

#Define projection grid
lat_min = -80
lat_max = 80
lon_min = -180
lon_max = 180
nlat = 10
nlon = 10

#Create intervals
lat = linspace(lat_min, lat_max, nlat)
lon = linspace(lon_min, lon_max, nlon)

#Create  meshgrid
latg, long = meshgrid(lat, lon)

#Project meshgrid
X, Y, a, b = project(proj_name, R, latg, long, lat0)

#Airy local
h2_a = 0.5*((a-1)**2+(b-1)**2)

#Complex local
h2_c = 0.5*(abs(a-1)+abs(b-1)) + a/b - 1

#Airy global
H2_a = mean(h2_a)

#Complex global
H2_c = mean(h2_c)

#Airy weighted global
w = cos(latg * pi /180)
H2_aw = sum(w*h2_a)/sum(w)

#Complex weighted global
H2_cw = sum(w*h2_c)/sum(w) 

print(H2_aw, H2_cw)

#Draw continents
continents = loadtxt("v:/Bayer/mk_2025_26/u4/continents_points/eur.txt")

#Extract coordinates
latc = continents[:, 0]
lonc = continents[:, 1]

#Project points
Xc, Yc, ac, bc = project(proj_name, R, latc, lonc, lat0)

#Draw points
plot(Xc, Yc)
show()

print(Xc)