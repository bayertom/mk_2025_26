from math import *

def WGSToJTSK (phi_WGS, la_WGS):
    #WGS84 parameters
    a_WGS = 6378137.00
    b_WGS = 6356752.3142
    
    e2_WGS = (a_WGS*a_WGS - b_WGS*b_WGS)/(a_WGS*a_WGS)
    W_WGS = sqrt(1-e2_WGS*(sin(phi_WGS))**2)
    N_WGS = a_WGS/W_WGS
    
    #XYZ coordinates, WGS 84
    X_WGS = N_WGS * (cos(phi_WGS) * cos(la_WGS))
    Y_WGS = N_WGS * (cos(phi_WGS) * sin(la_WGS))
    Z_WGS = N_WGS * (1 - e2_WGS) * sin(phi_WGS)
    
    #Helmert transformation, parameters
    om_x = 4.9984 / 3600 * pi /180 
    om_y = 1.5867 /3600 * pi / 180
    om_z = 5.2611 /3600 * pi / 180
    m = 1 - 3.5623e-06
    dlt_x = -570.8285
    dlt_y = -85.6769
    dlt_z = -462.8420
    
    #Helmert transformation, Bessel ellipsoid
    X_Bes = m * (X_WGS + Y_WGS * om_z - om_y * Z_WGS) + dlt_x
    Y_Bes = m * (-om_z * X_WGS + Y_WGS + om_x * Z_WGS) + dlt_y
    Z_Bes = m * (om_y * X_WGS - om_x * Y_WGS + Z_WGS) + dlt_z
    
    #Bessel parameters
    a_Bes = 6377397.155
    b_Bes = 6356078.963
    e2_Bes = (a_Bes*a_Bes - b_Bes*b_Bes)/(a_Bes*a_Bes)
   
    #Phi, lam, Bessel
    la_Bes = atan2(Y_Bes,X_Bes)
    tan_phi_Bes = Z_Bes / ((1 - e2_Bes) * sqrt(X_Bes**2 + Y_Bes**2))
    phi_Bes = atan(tan_phi_Bes)

#Input coordinates
phi_WGS = 50 * pi/180
la_WGS = 15 * pi/180

WGSToJTSK (phi_WGS, la_WGS)
