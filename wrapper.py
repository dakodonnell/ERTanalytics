import numpy as np
from findStations import findStations
from map2Coords import map2Coords
from geoFactor import geoFactor
from fwdEngine import fwdEngine
from pseudosection import pseudosection

### SURVEY PARAMETERS ###
num_electrodes = 20 #Number of electrodes in a spread
array_type = "wenner" #Type of electrode array
a = 1 #"A" spacing between quadrapole, in meters
dc = 1.0 #DC current, in amperes
x0 = 0 #Initial location of electrode spread
sweeps = 1
overlap = 0


### HALF SPACE PARAMETERS ###
earth_model = "homogeneous"


### BURIED SPHERE PARAMETERS ###
sphere_res = "N/A" #ohm-meters
sphere_z = "N/A" #meters
sphere_x = "N/A" #meters
sphere_R = "N/A" #meters


### HETEROGENEOUS LAYER PARAMETERS ###
num_layers = 0
if int(num_layers) > 0:
    layer_res = np.empty(int(num_layers))
    layer_z = np.empty(int(num_layers))
else:
    layer_res = "N/A"
    layer_z = "N/A"

# C1,P1,P2,C2
electrodes = findStations(array_type,a,num_electrodes,x0)

midpoint, z_eff = map2Coords(array_type,a,num_electrodes,electrodes)

geo_factor = geoFactor(array_type,a,num_electrodes)
 
# Calculate Resistivity
if earth_model == "homogeneous":
    res_mesh = 1
    
rho_a = fwdEngine(res_mesh,geo_factor,dc,electrodes)

# Organize Data
struc=np.core.records.fromarrays([rho_a.flatten(),midpoint.flatten(),z_eff.flatten()],names='rho_a,x,z')

x = struc.x
z = struc.z
rho_a = struc.rho_a

# Remove nan values from data
for i in range(len(x)):
    if np.isnan(x[i]) == True:
        z[i] = np.nan

x = x[np.isfinite(x)]
z = z[np.isfinite(z)]
rho_a = rho_a[np.isfinite(rho_a)]
rho_a = np.around(rho_a,decimals=10)


pseudosection = pseudosection(x,z,rho_a)




    



 