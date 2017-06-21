import numpy as np
def findStations(array_type,a,num_electrodes,x0):

    zn = np.empty((0,1))
    xm = np.empty((0,1))

    if array_type == "wenner":
        n_max = (num_electrodes-1)//3

        for n in range(n_max):
            i_max = num_electrodes-(n+1)*3
            for i in range(i_max):
                x = x0+(1.5*(n+1)+i)*a
                xm = np.append(xm,x)
                z = 3/2*a*n                
                zn = np.append(zn,n+1)

    elif array_type == "dipoledipole":
        n_max = num_electrodes-3
        
        for n in range(n_max):
            i_max = num_electrodes-(n+3)
            for i in range(i_max):
                x = x0+a*(1.5+i+0.5*n)
                xm = np.append(xm,x)
                z = 3/2*a*n
                zn = np.append(zn,n+1)
	
    return xm,zn