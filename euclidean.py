import numpy as np

# Converts arrays of xyz-coordinates to spherical coordinates
def cart2sph(xv,yv,zv):
    rho = np.sqrt(xv**2+yv**2+zv**2)
    phi = np.arctan2(yv,xv)
    theta = np.arctan2(zv,np.sqrt(xv**2+yv**2))
    return rho,phi,theta
	
# Converts arrays of spherical coordinates to xyz-coordinates
def sph2cart(rho,phi,theta):
    xv = rho*np.sin(theta)*np.cos(phi)
    yv = rho*np.sin(theta)*np.sin(phi)
    zv = rho*np.cos(theta)
    return xv,yv,zv

# Euclidean distance between two 1D arrays, used for lists of x-coordinates
def dist(r1,r2):
    return np.sqrt((r1-r2)**2)

# Euclidean distance between two 2D arrays, used for lists of xyz-coordinates
def arrayDist(r1,r2):
    return np.sqrt(np.sum((r1-r2)**2,axis=1))
	
