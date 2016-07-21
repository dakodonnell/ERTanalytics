import numpy as np

def map2Coords(array_type,a,num_electrodes,electrodes):
    
    # Max number of data levels in an electrode array
    if array_type == "wenner":
        n_max = (num_electrodes - 1) // 3 
    elif array_type == "dipoledipole":
        n_max = num_electrodes - 3
    
    # Calculate the midpoint and effective depth of each electrode set
    midpoint = np.empty((n_max,num_electrodes-3))
    z_eff = np.empty((n_max,num_electrodes-3))
    for n in range(n_max):
        for i in range(num_electrodes-3):
            midpoint[n,i] = np.sum(electrodes[n,i])/4
            z_eff[n,i]= 1.5*a*(n+1)
            
    return midpoint,z_eff