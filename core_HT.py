"""
This File is for Running the core code for Heat Transfer Analysis
"""

import numpy as np 
import matplotlib.pyplot as plt
import time
from playsound import playsound

import material
import run

def cal_As (diameter, length) :
    return np.pi * diameter * length 

def cal_cross_area (diameter):
    return np.pi * (diameter/2)*(diameter/2)

def cal_nu_turb (re,pr) :
    f = (0.79 * np.log(re) - 1.64) **(-2)
    return (f / 8) * (re - 1000) * pr / (1 + 12.7 * np.power(f/8,0.5) * ((np.power(pr,2/3)) - 1))

def cal_re (velo_kgs, diameter, kinematic_viscosity) :
    return velo_kgs * diameter / kinematic_viscosity

def cal_m_dot (density, area, velocity) :
    return density* area* velocity

def cal_velo_fluid (density, area, m_dot) :
    return m_dot/density/area

def sectional_analysis (
        p_L = 30,
        no_section = 1000, 
        layer_diameter_set = [0.015, 0.025, 0.05],
        type_selection_fluid = 0,
        type_selection_pipe = 0,
        type_selection_insulator = [0],

        T_i = 350,
        T_amb = 30,

        velo_fluid = 0.05,
        selection = 1,
        model = [False, False] # [Transient Model, Natural Conection Model] 
):
    start_time = time.time()
    """
    #S01
    Check for tally of number of layers
    """
    if len(layer_diameter_set) != len(type_selection_insulator) +2 :
        print("Lack of Layer Information")
        return 0, 0
    
    """
    #S02
    Data Preparation for insulation layer (Constant through Pipe)
    """
    ins_layer = len(type_selection_insulator) 
    layer_k_set = [0]
    for i in range (ins_layer) : 
        layer_k_set.append(material.data_set_insulator_mat_k[type_selection_insulator[i]])

    """
    #S03
    Data Export Preparation
    """
    export_data_x, export_data_y, export_data_z = run.HT_data_export_preparation(selection, T_i)

    """
    #S04
    Constatnt Variable across pipe (pre-Calculation)
    """
    g = 9.81
    relaxation_factor = 0.01
    
    if model [0] == False : 
        no_section = 1

    delta_pipe_length = p_L/ no_section
    As = cal_As(layer_diameter_set[0], delta_pipe_length)

    # Assumed Constant Mass Flow rate across pipe, therefore the mass flow rate calculated based on the initial condition whereby the velocity of the fluid is same as given
    fluid_prop   = material.fluid_material (type_selection_fluid-1, T_i)
    fluid_density = fluid_prop [0]

    m_dot = cal_m_dot (fluid_density,cal_cross_area(layer_diameter_set[0]),velo_fluid)

    init_T_i = T_i
    for i in range (no_section):
        """
        #Si_01
        Export Data Length 
        """
        x_data = (i)*delta_pipe_length + delta_pipe_length/2
        x_data_2 = (i+1)*delta_pipe_length

        """
        #Si_02
        Data Preparation (Variating)
        """
        fluid_density, fluid_cp, fluid_k, fluid_viscos, fluid_pr = material.fluid_material (type_selection_fluid-1, T_i)
        layer_k_set [0] = material.pipe_mat_prop (type_selection_pipe-1, T_i)

        """
        #Si_03
        Calculation (Internal Convection)
        """
        velo_fluid_new = cal_velo_fluid(fluid_density, cal_cross_area(layer_diameter_set[0]), m_dot)
        re = cal_re(velo_fluid_new, layer_diameter_set[0], fluid_viscos)
        nu = cal_nu_turb(re, fluid_pr)
        fluid_h = fluid_k * nu / layer_diameter_set[0]

        """
        #Si_04
        R_set Preparation (integrate with the internal convection resistance)
        """
        r_set = np.zeros(len(type_selection_insulator)+2)

        """
        #Si_05
        Thermal Resistance Calculation
        """
        for i in range (len(layer_k_set)): 
            r_set[i] = np.log(layer_diameter_set[i+1] / layer_diameter_set[i]) / 2 / np.pi / delta_pipe_length / layer_k_set[i] 

        """
        #Si_06
        Calculation (Natural Convection)
        """
        amb_h = 0
        amb_h_g = 20
        iteration = 0
        amb_h_off = 20
        while abs(amb_h_g - amb_h) > 0.1 :
            
            if model[1] == False : 
                amb_h_g = amb_h_off
            else :
                amb_h_g = amb_h_g + relaxation_factor * (amb_h - amb_h_g)

            """
            #Sin_01
            Auto Adjustment of Relaxation Factor
            """
            if str(amb_h_g).lower() == "nan": 
                relaxation_factor = relaxation_factor/10
                iteration = 0
                amb_h_g = 20
                amb_h = 0
            if iteration > 1000 :
                relaxation_factor = relaxation_factor * 10
                iteration = 0
                amb_h_g = 20
                amb_h = 0

            """
            #Sin_02
            Main Calculation (Natural Convection)
            """
            AsO = cal_As(layer_diameter_set[-1],delta_pipe_length)
            r_set[-1] = 1 / amb_h_g / AsO
            r_t = sum(r_set)

            q_s = fluid_h * (T_amb - T_i) / (1 + As * r_t * fluid_h)
            Q_dot = q_s * As

            T_so = T_amb - Q_dot * ( 1 / amb_h_g / AsO)

            T_f = ( T_so + T_amb ) / 2
            beta = 1 / (T_f + 273)
            amb_k, amb_pr, amb_dyn_vis  = material.amb_prop(0,T_f)
            Gr_D = g * beta * (T_so - T_amb) * layer_diameter_set[-1] * layer_diameter_set[-1] * layer_diameter_set[-1] / amb_dyn_vis / amb_dyn_vis
            RaD = Gr_D * amb_pr

            Nu_o = np.power((0.6 + 0.387 * np.power(RaD,1/6) / np.power(1+ np.power(0.559 / amb_pr, 9/16),8/27)),2)
            amb_h = Nu_o * amb_k / layer_diameter_set[-1]

            if model[1] == False :
                amb_h = amb_h_off

            iteration = iteration + 1

        """
        #Si_07
        Calculation Temperature Exit
        """
        Te = T_i + Q_dot / m_dot / fluid_cp

        """
        #Si_08
        Export Data
        """
        export_data_x, export_data_y, export_data_z = run.HT_data_export (
            export_data_x, export_data_y, export_data_z, selection, x_data_2, x_data,
            fluid_h, As, r_set, Q_dot, Te, init_T_i, T_i, velo_fluid_new, 
            m_dot,fluid_cp
            )
        
        T_i = Te

    end_time = time.time()
    print(f"Time Consume : {round(end_time-start_time,2)} seconds")
    return export_data_x, export_data_y, export_data_z

def radial_analysis(r_set, Ti, q_dot) :
    T_plot = [Ti]
    for i in range (len(r_set)): 
        Ti = q_dot * r_set[i] +Ti
        T_plot.append(Ti)
    return T_plot

def plot_radial (Do, Di, T_inner, T_outter) :
    R_plot = []
    T_plot = []
    diameter_range = Do - Di
    iteration = 100
    increment = diameter_range / iteration

    for i in range (iteration+1) :
        D_var = Di + increment * i 
        T_ans = T_inner + (T_outter - T_inner) / np.log(Do/Di) * np.log(D_var/Di)
        R_plot.append(D_var/2)
        T_plot.append(T_ans)
    return R_plot, T_plot

if __name__ == "__main__" : 
    print("Running")

    print("Complete Run")