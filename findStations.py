import numpy as np

def findStations(array_type,a,num_electrodes,x0):
    
    # Initialize an empty 3D array to hold electrode coordinates in n data lvls
    electrodes = np.empty((0,num_electrodes-3,4))
    
    # Define a "not a number" array
    nan_arr = np.array([[[np.nan,np.nan,np.nan,np.nan]]])
    
    # Create array of electrode coordinates for every n-lvl of data 
    
    if array_type == "wenner": 

        # Max number of data levels in a wenner array 
        n_max = (num_electrodes - 1) // 3    
    
        for n in range(1,n_max+1): # For each lvl of n
            i_max = num_electrodes - n*3 # Max num of i data points per n-lvl
            station = np.array([[[x0,x0+n*a,x0+2*n*a,x0+3*n*a]]]) #C1,P1,P2,C2
            n_data = np.empty((0,1,4)) # Initialize placeholder array for n-lvl
            n_data = np.vstack((n_data,station)) # Add coords to placeholder
        
            pad = n*3 - 3
        
            # Shift, copy initial n-lvl coords iterating over num data points in n
            for i in range(1,i_max):
                station = station + a
                n_data = np.hstack((n_data,station))
            
            # Add in placeholders to keep a consistent array shape
            for j in range(pad):
                n_data = np.hstack((n_data,nan_arr))
                
            electrodes = np.vstack((electrodes,n_data))
    

    elif array_type == "dipoledipole":
    
        # Max number of data levels in a dipole-dipole array
        n_max = num_electrodes - 3        
        
        for n in range(1,n_max+1): # For each lvl of n
            i_max = num_electrodes - 2 - n # Find max num of data points
            #station = np.array([[[x0,x0+a,x0+n+a,x0+n+2*a]]]) # n-lvl coords
            station = np.array([[[x0+a,x0+n+a,x0+n+2*a,x0]]]) #C2,C1,P1,P2
            n_data = np.empty((0,1,4)) # Initialize placeholder array for n-lvl  
            n_data = np.vstack((n_data,station)) # Add coords to placeholder
        
            pad = n - 1
        
            # Shift, copy initial n-lvl coords iterating over num data points in n
            for i in range(1,i_max):
                station = station + a
                n_data = np.hstack((n_data,station))
            
            # Add in placeholders to keep a consistent array shape
            for j in range(pad):
                n_data = np.hstack((n_data,nan_arr))
            
            electrodes = np.vstack((electrodes,n_data)) 
    

    return electrodes
    

        



    
