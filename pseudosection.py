import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def pseudosection(x,z,rho_a):

    # Create a meshgrid
    xv,zv = np.meshgrid(np.linspace(0,19,500),np.linspace(0,19,500))
   
   # Interpolate rho_v values over meshgrid
    rho_av = griddata((x,z),rho_a,(xv,zv))
    
    pseudosection = plt.contourf(xv,zv*-1,rho_av)
   
    return plt.show(pseudosection)
    
