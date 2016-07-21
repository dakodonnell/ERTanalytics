import numpy as np
import euclidean

def fwdEngine(res_mesh,geo_factor,dc,electrodes):
    
    src1,rec1,rec2,src2 = electrodes.transpose((2,0,1))
    
    # Calculate the euclidean distance between electrode pairs
    r1 = euclidean.dist(src1,rec1)
    r2 = euclidean.dist(src2,rec1)
    r3 = euclidean.dist(src1,rec2)
    r4 = euclidean.dist(src2,rec2)
        
        
    if res_mesh == 1:
        
        deltaV = dc*res_mesh/(2*np.pi)*((1/r1-1/r2)-(1/r3-1/r4))
        
        resistance = deltaV/dc
        
        rho_a = resistance*geo_factor
   
    return (rho_a)
        