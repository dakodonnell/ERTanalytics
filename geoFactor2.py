import numpy as np

def geoFactor(array_type,a,num_electrodes):

    # Initialize an array of same shape as the resistance array        
    geofact = np.empty((0,1))

    if array_type == "wenner":
        # Max number of data levels in a wenner array         
        n_max = (num_electrodes-1)//3   
        
        # Calculate the geometric factor for each n-lvl        
        for n in range(1,n_max+1):      
            i_max = num_electrodes-n*3
            for i in range(i_max):
                geofact = np.append(geofact,2*np.pi*a*n)
        
    elif array_type == "dipoledipole":
        # Max number of data levels in a dipole-dipole array         
        n_max = num_electrodes-3
        
        # Calculate the geometric factor for each n-lvl       
        for n in range(1,n_max+1):
            i_max = num_electrodes-(n+2)
            for i in range(i_max):            
                geofact = np.append(geofact, np.pi*n*(n+1)*(n+2)*a)

    return geofact
