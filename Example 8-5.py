"""
Validation of Textbook Example 8-5
"""

import numpy as np

#Assumption
"""
Assumption
1) Steady Flow condition
2) Surface heat flux is uniform
3) Innersurface of the tube is smooth
"""

#Input
input_tin = 15 #Temperature enter the tube
input_tout = 65 #Temperature exit the tube

input_pipe_diameter = 0.03 #m
input_pipe_length = 5 #m

input_volume_flow_rate = 0.01/60 #m3s-1

#Processed Data

##Taking Data from Table refer with Bulk mean temperature
table_rho = 992.1 #kgm-3
table_k = 0.631 #Wm-1K-1
table_v = 0.658e-6 #m2s-1
table_cp = 4179 #Jkg-1K-1
table_Pr = 4.32

def bulk_temp (Temp_in, Temp_out): 
    return (Temp_in+Temp_out)/2

def cross_section_area (D) :
    return 0.25*np.pi*D*D

def surface_area (D, L): 
    return np.pi*D*L

def heat_transfer(rho,volume_flow_rate,cp,temp_in, temp_out) :
    mass_flow_rate = rho*volume_flow_rate
    heat_transfer_rate = mass_flow_rate*cp*(temp_out-temp_in)
    return heat_transfer_rate

def inner_surface_temperature (rho,volume_flow_rate,cp,temp_in, temp_out,D,L,v,pr,k) : 
    qdots = heat_transfer(rho,volume_flow_rate,cp,temp_in, temp_out)/surface_area(D,L)
    velocity_average = volume_flow_rate/cross_section_area(D)
    renolds_number = velocity_average*D/v

    if renolds_number> 10000 :
        L_h = 10*D
        if L_h < L : 
            nusselt_number = 0.023*np.power(renolds_number,0.8)*np.power(pr,0.4)
    
    h = k*nusselt_number/D

    Temperature_inner_surface = temp_out+qdots/h
    return Temperature_inner_surface

"""
Improvement in inner, find the other condition in if there
"""

print(inner_surface_temperature(table_rho,input_volume_flow_rate,table_cp,input_tin,input_tout,input_pipe_diameter,input_pipe_length,table_v,table_Pr,table_k))
