import numpy as np

def geoFactor(array_type,a,num_electrodes):


    if array_type == "wenner":
        # Max number of data levels in a wenner array         
        n_max = (num_electrodes-1)//3   
        
        # Initialize an array of same shape as the resistance array        
        geofact = np.ones((n_max,num_electrodes-3))
        
        # Calculate the geometric factor for each n-lvl        
        for n in range(1,n_max+1):      
            geofact[n-1] *= 2*np.pi*a*n
        
    elif array_type == "dipoledipole":
        # Max number of data levels in a dipole-dipole array         
        n_max = num_electrodes-3
        
        # Initialize an array of same shape as the resistance array
        geofact = np.ones((n_max,num_electrodes-3))
        
        # Calculate the geometric factor for each n-lvl       
        for n in range(1,n_max+1):
            geofact[n-1] *= np.pi*n*(n+1)*(n+2)*a

    return geofact