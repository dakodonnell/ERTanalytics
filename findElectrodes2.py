from __future__ import division
import numpy as np


def findElectrodes(array_type,a,xm,zn):


    if array_type == "wenner":
        src1 = xm-1.5*a*zn
        rec1 = xm-0.5*a*zn
        rec2 = xm+0.5*a*zn
        src2 = xm+1.5*a*zn
        
    elif array_type == "dipoledipole":
        src2 = xm-a*(1+zn/2)
        src1 = xm-a*zn/2
        rec1 = xm+a*zn/2
        rec2 = xm+a*(1+zn/2)
        
    electrodes = np.vstack((src1,rec1,rec2,src2)).T
        
    return electrodes