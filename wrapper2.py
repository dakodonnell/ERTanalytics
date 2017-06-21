import numpy as np
from findStations2 import findStations
from findElectrodes2 import findElectrodes
from geoFactor2 import geoFactor
from fwdEngine2 import fwdEngine
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


xm,zn = findStations(array_type,a,num_electrodes,x0)

electrodes = findElectrodes(array_type,a,xm,zn)

#electrodes = np.vstack((src1,rec1,rec2,src2))

geo_factor = geoFactor(array_type,a,num_electrodes)

# Calculate Resistivity
if earth_model == "homogeneous":
    res_mesh = 1
    
rho_a = fwdEngine(res_mesh,geo_factor,dc,electrodes)
rho_a = np.around(rho_a,decimals=10)

stations = np.core.records.fromarrays([xm,zn],names="xm,zn")

pseudosection = pseudosection(x,z,rho_a)