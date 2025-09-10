"""
Text Book Example 8-6 Validation
"""


import numpy as np

"""
Assumptions 
1) Steady Operating Conditions
2) Radiation effects are negligible
3) Convection effects on the outerpipe surface are negligible
4) One dimentionsal heat conduction through pipe wall and insulation
5) The thermal conductivities of pipewall and insulation are constant
6) Thermal resistance at the interface is negligible
7) Surface temperature are uniform
8) Inner surface of the tube are smooth
"""


#input 
input_pipe_length = 10 # m
input_pipe_inner_diameter = 0.05#m
input_pipe_outter_diameter = 0.06#m

input_mass_flow_rate = 0.05 #kgs-1

input_temperature_enter = 350 #Celsius
input_temperature_exit = 290 #Celsius

input_insulator_thickness = 0.0225 #m

#Pre-Input
input_Kpipe = 15#Wm-1K-1
input_Kinsulator = 0.95 #Wm-1K-1

##Froom Table A9 input as bulk temperature
input_fluid_properties_cp = 7900 #Jkg-1K-1
input_fluid_properties_k = 0.0836 #Wm-1K-1
input_fluid_properties_dynamic_viscosity = 2.084e-5 #kgm-1s-1
input_fluid_properties_Pr = 1.97


def bulk_temp (Temp_in, Temp_out): 
    return (Temp_in+Temp_out)/2

def cross_section_area (D) :
    return 0.25*np.pi*D*D

def surface_area (D, L): 
    return np.pi*D*L

def heat_transfer_coefficient (Di,L,mass_flow_rate,dynamic_viscosity,pr,k_fluid ) : 
    renolds_number = 4*mass_flow_rate/np.pi/Di/dynamic_viscosity

    if renolds_number > 10000 :
        L_h = 10*Di

        if L > L_h : 
            f = (0.790*np.log(renolds_number)-1.64)**(-2)
            nusselt = (f*pr*(renolds_number-1000)/8)/(1+12.7*np.power(f/8,0.5)*(np.power(pr,2/3)-1))
    
    h = k_fluid *nusselt/Di
    return h

def inner_pipe_surface_temperature (tenter, texit, h, As, mass_flow_rate, cp ) :
    return ((texit - tenter*np.power(np.e,h*-1*As/mass_flow_rate/cp))/(1-np.power(np.e,h*-1*As/mass_flow_rate/cp)))

#print(heat_transfer_coefficient(input_pipe_inner_diameter, input_pipe_length,input_mass_flow_rate,input_fluid_properties_dynamic_viscosity,input_fluid_properties_Pr,input_fluid_properties_k))
#print(surface_area(input_pipe_inner_diameter,input_pipe_length))
#print(inner_pipe_surface_temperature(input_temperature_enter,input_temperature_exit,heat_transfer_coefficient(input_pipe_inner_diameter, input_pipe_length,input_mass_flow_rate,input_fluid_properties_dynamic_viscosity,input_fluid_properties_Pr,input_fluid_properties_k),surface_area(input_pipe_inner_diameter,input_pipe_length),input_mass_flow_rate,input_fluid_properties_cp))

def thermal_resistance(D1,D2,k,l) :
    return np.log(D1/D2)/2/np.pi/k/l

def outter_pipe_surface_temperature (tenter, texit, h, As, mass_flow_rate, cp, Di,Do,insulation_thickness,kpipe,kinsulator,L) :
    Dinsulator = Do + 2*insulation_thickness
    Rpipe = thermal_resistance(Do,Di,kpipe,L)
    Rinsulator = thermal_resistance(Dinsulator,Do,kinsulator,L)
    Rtotal = Rpipe + Rinsulator 

    Tsi = inner_pipe_surface_temperature (tenter, texit, h, As, mass_flow_rate, cp ) 

    outter_surface_temperature = Tsi - Rtotal*mass_flow_rate*cp*(tenter-texit)
    return outter_surface_temperature

print (outter_pipe_surface_temperature(input_temperature_enter,input_temperature_exit,heat_transfer_coefficient(input_pipe_inner_diameter, input_pipe_length,input_mass_flow_rate,input_fluid_properties_dynamic_viscosity,input_fluid_properties_Pr,input_fluid_properties_k),surface_area(input_pipe_inner_diameter,input_pipe_length),input_mass_flow_rate,input_fluid_properties_cp,input_pipe_inner_diameter,input_pipe_outter_diameter,input_insulator_thickness,input_Kpipe,input_Kinsulator,input_pipe_length))
