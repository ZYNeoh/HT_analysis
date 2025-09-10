import numpy as np
import matplotlib.pyplot as plt
import math

"""
"""

#Library
def wang_properties () :
    temp = [70, 80, 90, 100, 110, 120, 130, 140, 150]
    density = [978.2, 970.9, 966.2, 961.5, 952.5, 943.4, 934.7, 925.9, 917.5]
    cp = [4190, 4200, 4200, 4220, 4230, 4250, 4270, 4290, 4310] #Jkg-1K-1
    return temp, density, cp


#Formula
def thermal_resistance (DN, thickness,K) :
    return np.log((DN+thickness)/DN)/2/np.pi/K

def temp_cal (Ti, Ts, L, Cp, m_dot, R) :
    return (Ti - Ts)*(np.exp(-L/Cp/m_dot/R)) + Ts

def temp_change (Ti, Ts, L, Cp, m_dot, R) :
    return (Ti - Ts)*(1-np.exp(-L/Cp/m_dot/R))

#Validation model
def validation_model_sample (): 
    # Calculation Section

    x_axis_data = []
    y_axis_data = []

    x_axis_label = "x-axis Label"
    y_axis_label = "y-axis Label"

    legend_1 = ["Legend 1"]
    legend_2 = ["Lengend 2"]

    title = "Graph Title"

    x_axis_ref = []
    y_axis_ref = []

    extra_legend = "" # External data that want to show in legend
    return x_axis_data, y_axis_data, x_axis_ref, y_axis_ref, x_axis_label, y_axis_label, legend_1, legend_2, title, extra_legend

def valid_wang_fig_2a () :
    max_DN = 2
    DN = 0.4
    no_points = 1000
    thickness = 0.05
    conductivity = 0.1
    
    delta = (max_DN - DN)/no_points
    DN_plots = []
    R_plots = []
    for i in range (no_points+1) :
        resistance = thermal_resistance(DN,thickness,conductivity)
        DN_plots.append(DN)
        R_plots.append(resistance)
        DN = DN + delta
    
    DN_plot= [DN_plots]
    R_plot = [R_plots]
    
    DN_label = "Pipeline diameter DN (m)"
    R_label = "Thermal resistance R (KmW-1)"

    legend_Model = ["model"]
    legend_Paper = ["Wang(2022)"]

    title = "Validation of Fig 2A"

    DN_paper = [[0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0]]
    R_paper = [[0.18,0.1224,0.0936,0.0744,0.0636,0.0552,0.0480,0.0432,0.0384]]
    return DN_plot, R_plot,DN_paper,R_paper, DN_label,R_label , legend_Model, legend_Paper,title,0

def valid_wang_fig_2b(): 
    max_thickness = 0.26
    DN = 1
    no_points = 1000
    thickness = 0.02
    conductivity = 0.1
    
    delta = (max_thickness - thickness)/no_points
    thickness_plots = []
    R_plots = []
    for i in range (no_points+1) :
        resistance = np.log((DN+thickness)/DN)/2/np.pi/conductivity
        thickness_plots.append(thickness)
        R_plots.append(resistance)
        thickness = thickness + delta
    
    R_plot = [R_plots]
    thickness_plot = [thickness_plots]
    
    thickness_label = "Insulation thickness (m)"
    R_label = "Thermal resistance R (KmW-1)"

    legend_Model = ["model"]
    legend_Paper = ["Wang(2022)"]

    title = "Validation of Fig 2B"

    DN_paper = [[0.02, 0.05, 0.08, 0.11, 0.14, 0.17, 0.2, 0.23, 0.26]]
    R_paper = [[0.029, 0.0785, 0.1225, 0.1555, 0.205, 0.2435, 0.282, 0.3205, 0.359]]
    return thickness_plot, R_plot,DN_paper,R_paper, thickness_label,R_label , legend_Model, legend_Paper,title,0

def valid_wang_fig_2c(): 
    max_conductivity = 0.18
    DN = 1
    no_points = 1000
    thickness = 0.05
    conductivity = 0.02
    
    delta = (max_conductivity - conductivity)/no_points
    conductivity_plots = []
    R_plots = []
    for i in range (no_points+1) :
        resistance = np.log((DN+thickness)/DN)/2/np.pi/conductivity
        conductivity_plots.append(conductivity)
        R_plots.append(resistance)
        conductivity = conductivity + delta
    
    conductivity_plot= [conductivity_plots]
    R_plot= [R_plots]
    
    conductivity_label = "Thermal Conductivity (m)"
    R_label = "Thermal resistance R (KmW-1)"

    legend_Model = ["model"]
    legend_Paper = ["Wang(2022)"]

    title = "Validation of Fig 2C"

    DN_paper = [[0.02, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18]]
    R_paper = [[0.3790, 0.1869, 0.1248, 0.0965, 0.0739, 0.0626, 0.0541, 0.0457, 0.0400]]
    return conductivity_plot, R_plot,DN_paper,R_paper, conductivity_label,R_label , legend_Model, legend_Paper,title,0

def valid_wang_fig_3a () :
    DN = [0.4, 1, 2] #m
    T_i = 100 #Celsius
    v = 2.5 #ms-1
    T_s = 0 #Celsius
    insulation_thickness = 0.05 #m
    K_ins = 0.10 #Wm-1K-1
    
    temp_set, density_set, cp_set = wang_properties()
    density = np.interp(T_i,temp_set,density_set)
    cp = np.interp(T_i,temp_set,cp_set)

    iteration = 100
    max_length = 50000 #m
    delta = max_length/iteration

    T_plot = []
    L_plot = []

    for j in range (len(DN)) :
        T_plot_1 = []
        L_plot_1 = []
        length = 0
        for i in range (iteration +1 ) :
            R = thermal_resistance(DN[j],insulation_thickness,K_ins)
            m_dot = density*np.pi*(DN[j]/2)*(DN[j]/2)*v
            length = delta* i
            T_L = temp_change (T_i, T_s, length, cp, m_dot, R)

            L_plot_1.append(length)
            T_plot_1.append(T_L)
        T_plot.append(T_plot_1)
        L_plot.append(L_plot_1)

    Pipe_length_label = "Pipeline Length (m)"
    Temp_drop_label = "Temperature Drop (°C)"

    legend_Model = ["DN=0.4m (Verified Model)", "DN=1.0m (Verified Model)","DN=2.0m (Verified Model)"]
    legend_Paper = ["DN=0.4m Wang(2022)", "DN=1.0m Wang(2022)", "DN=2.0m Wang(2022)"]

    title = "Validation of Fig 3a"

    L_paper = [[10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000]]
    T_paper = [[4.42, 6.46, 8.50, 10.54, 12.51, 14.28, 16.32, 18.19, 19.92], 
               [1.70, 2.38, 3.23, 4.08, 4.93, 5.78, 6.46, 7.14, 8.09], 
               [0.85, 1.19, 1.53, 2.04, 2.38, 2.72, 3.13, 3.57, 4.08]]
    return L_plot, T_plot, L_paper,T_paper, Pipe_length_label, Temp_drop_label, legend_Model, legend_Paper, title, 0

def valid_wang_fig_3b () :
    DN = 1 #m
    T_i = [70, 100, 150] #Celsius
    v = 2.5 #ms-1
    T_s = 0 #Celsius
    insulation_thickness = 0.05 #m
    K_ins = 0.10 #Wm-1K-1
    
    iteration = 100
    max_length = 50000 #m
    delta = max_length/iteration

    T_plot = []
    L_plot = []

    for j in range (len(T_i)) :
        temp_set, density_set, cp_set = wang_properties()
        density = np.interp(T_i[j],temp_set,density_set)
        cp = np.interp(T_i[j],temp_set,cp_set)

        T_plot_1 = []
        L_plot_1 = []
        length = 0
        for i in range (iteration +1 ) :
            R = thermal_resistance(DN,insulation_thickness,K_ins)
            m_dot = density*np.pi*(DN/2)*(DN/2)*v
            length = delta* i
            T_L = temp_change (T_i[j], T_s, length, cp, m_dot,R)

            L_plot_1.append(length)
            T_plot_1.append(T_L)
        T_plot.append(T_plot_1)
        L_plot.append(L_plot_1)
    #print(T_plot)

    Pipe_length_label = "Pipeline Length (m)"
    Temp_drop_label = "Temperature Drop (°C)"

    legend_Model = ["Ti=70°C (Verified Model)", "Ti=100°C (Verified Model)","Ti=150°C (Verified Model)"]
    legend_Paper = ["Ti=70°C Wang(2022)", "Ti=100°C Wang(2022)", "Ti=150°C Wang(2022)"]

    title = "Validation of Fig 3b"

    L_paper = [[10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000]]
    T_paper = [[1.10, 1.65, 2.20, 2.75, 3.30, 3.85, 4.40, 4.95, 5.50], 
               [1.65, 2.48, 3.30, 4.13, 4.95, 5.72, 6.46, 7.26, 7.98], 
               [2.61, 3.85, 5.17, 6.46, 7.70, 8.94, 10.18, 11.39, 12.60]]
    return L_plot, T_plot, L_paper,T_paper, Pipe_length_label, Temp_drop_label, legend_Model, legend_Paper, title, 0

def valid_wang_fig_3c () :
    DN = 1 #m
    T_i = 100 #Celsius
    v = [1.0, 2.5, 5.0] #ms-1
    T_s = 0 #Celsius
    insulation_thickness = 0.05 #m
    K_ins = 0.10 #Wm-1K-1
    
    iteration = 100
    max_length = 50000 #m
    delta = max_length/iteration

    T_plot = []
    L_plot = []

    for j in range (len(v)) :
        temp_set, density_set, cp_set = wang_properties()
        density = np.interp(T_i,temp_set,density_set)
        cp = np.interp(T_i,temp_set,cp_set)

        T_plot_1 = []
        L_plot_1 = []
        length = 0
        for i in range (iteration +1 ) :
            R = thermal_resistance(DN,insulation_thickness,K_ins)
            m_dot = density*np.pi*(DN/2)*(DN/2)*v[j]
            length = delta* i
            T_L = temp_change (T_i, T_s, length, cp, m_dot,R)

            L_plot_1.append(length)
            T_plot_1.append(T_L)
        T_plot.append(T_plot_1)
        L_plot.append(L_plot_1)
    #print(T_plot)

    Pipe_length_label = "Pipeline Length (m)"
    Temp_drop_label = "Temperature Drop (°C)"

    legend_Model = ["v=1.0ms-1 (Verified Model)", "v=2.5ms-1 (Verified Model)","v=5.0ms-1 (Verified Model)"]
    legend_Paper = ["v=1.0ms-1 Wang(2022)", "v=2.5ms-1 Wang(2022)", "v=5.0ms-1 Wang(2022)"]

    title = "Validation of Fig 3c"

    L_paper = [[10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000]]
    T_paper = [[4.09, 6.21, 8.03, 10.00, 11.86, 13.80, 15.51, 17.41, 18.98], 
               [1.53, 2.48, 3.29, 4.02, 4.82, 5.77, 6.57, 7.30, 8.03], 
               [0.80, 1.28, 1.68, 2.04, 2.41, 2.92, 3.29, 3.65, 4.20]]
    return L_plot, T_plot, L_paper,T_paper, Pipe_length_label, Temp_drop_label, legend_Model, legend_Paper, title, 0

def valid_wang_fig_3d () :
    DN = 1 #m
    T_i = 100 #Celsius
    v = 2.5 #ms-1
    T_s = [-40, 0, 40] #Celsius
    insulation_thickness = 0.05 #m
    K_ins = 0.10 #Wm-1K-1
    
    iteration = 100
    max_length = 50000 #m
    delta = max_length/iteration

    T_plot = []
    L_plot = []

    for j in range (len(T_s)) :
        temp_set, density_set, cp_set = wang_properties()
        density = np.interp(T_i,temp_set,density_set)
        cp = np.interp(T_i,temp_set,cp_set)

        T_plot_1 = []
        L_plot_1 = []
        length = 0
        for i in range (iteration +1 ) :
            R = thermal_resistance(DN,insulation_thickness,K_ins)
            m_dot = density*np.pi*(DN/2)*(DN/2)*v
            length = delta* i
            T_L = temp_change (T_i, T_s[j], length, cp, m_dot,R)

            L_plot_1.append(length)
            T_plot_1.append(T_L)
        T_plot.append(T_plot_1)
        L_plot.append(L_plot_1)
    #print(T_plot)

    Pipe_length_label = "Pipeline Length (m)"
    Temp_drop_label = "Temperature Drop (°C)"

    legend_Model = ["Ts=-40°C (Verified Model)", "Ts=0°C (Verified Model)","Ts=40°C (Verified Model)"]
    legend_Paper = ["Ts=-40°C Wang(2022)", "Ts=0°C Wang(2022)", "Ts=40°C Wang(2022)"]

    title = "Validation of Fig 3d"

    L_paper = [[10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000], 
                [10000,15000,20000,25000,30000,35000,40000,45000,50000]]
    T_paper = [[2.35, 3.43, 4.66, 5.83, 6.86, 8.04, 9.11, 10.24, 11.27], 
               [1.72, 2.50, 3.23, 4.12, 4.90, 5.68, 6.57, 7.35, 8.09], 
               [0.98, 1.47, 1.96, 2.45, 2.94, 3.43, 3.92, 4.41, 4.90]]
    return L_plot, T_plot, L_paper,T_paper, Pipe_length_label, Temp_drop_label, legend_Model, legend_Paper, title, 0

def valid_wang_fig_4a (): 
    K_ins = 0.1
    thickness_ins = 0.050
    length = 50000 #m

    T_i = 100
    var_para = 1 #m
    T_s = 0
    v = 2.5

    var_para_min = 0.4
    var_para_max = 2

    iteration = 1000
    delta = (var_para_max-var_para_min)/iteration

    x_plot = []
    rel_h_plot = []
    for i in range (iteration +1) :
        var_para = var_para_min + delta*i
        temp_set, density_set, cp_set = wang_properties()
        density = np.interp(T_i,temp_set,density_set)
        cp = np.interp(T_i,temp_set,cp_set)

        m_dot = density*np.pi*(var_para/2)*(var_para/2)*v

        R = thermal_resistance(var_para, thickness_ins, K_ins)
        delta_T = temp_change(T_i, T_s, length, cp, m_dot, R)
        rel_h = delta_T/(T_i-50)*100

        rel_h_plot.append(rel_h)
        x_plot.append (var_para)
    #print(rel_h_plot)

    x_axis_data = [x_plot]
    y_axis_data = [rel_h_plot]

    x_axis_label = "Pipe Diameter (m)"
    y_axis_label = "Relative Heat Loss (%)"

    legend_1 = ["Model"]
    legend_2 = ["Wang (2022)"]

    title = "Validation of Wang (2022) Fig 4a"

    x_data = []
    for i in range (9) :
        x_data.append(var_para_min + i*((var_para_max-var_para_min)/8))
    
    y_data = [39.70, 26.82, 20.09, 16.27, 13.62, 11.72, 10.76, 9.07, 8.3]
    
    x_axis_ref = [x_data]
    y_axis_ref = [y_data]

    extra_legend = "" # External data that want to show in legend
    return x_axis_data, y_axis_data, x_axis_ref, y_axis_ref, x_axis_label, y_axis_label, legend_1, legend_2, title, extra_legend

def valid_wang_fig_4b (): 
    K_ins = 0.1
    thickness_ins = 0.050
    length = 50000 #m

    var_para = 100
    DN = 1 #m
    T_s = 0
    v = 2.5

    var_para_min = 70
    var_para_max = 150

    iteration = 1000
    delta = (var_para_max-var_para_min)/iteration

    x_plot = []
    rel_h_plot = []
    for i in range (iteration +1) :
        var_para = var_para_min + delta*i
        temp_set, density_set, cp_set = wang_properties()
        density = np.interp(var_para,temp_set,density_set)
        cp = np.interp(var_para,temp_set,cp_set)

        m_dot = density*np.pi*(DN/2)*(DN/2)*v

        R = thermal_resistance(DN, thickness_ins, K_ins)
        delta_T = temp_change(var_para, T_s, length, cp, m_dot, R)
        rel_h = delta_T/(var_para-50)*100

        rel_h_plot.append(rel_h)
        x_plot.append (var_para)
    #print(rel_h_plot)

    x_axis_data = [x_plot]
    y_axis_data = [rel_h_plot]

    x_axis_label = "Initial Temperature (°C)"
    y_axis_label = "Relative Heat Loss (%)"

    legend_1 = ["Model"]
    legend_2 = ["Wang (2022)"]

    title = "Validation of Wang (2022) Fig 4b"

    x_data = []
    for i in range (9) :
        x_data.append(var_para_min + i*((var_para_max-var_para_min)/8))
    
    y_data = [27.80, 21.17, 18.06, 16.17, 14.90, 14.03, 13.47, 12.96, 12.68]
    
    x_axis_ref = [x_data]
    y_axis_ref = [y_data]

    extra_legend = "" # External data that want to show in legend
    return x_axis_data, y_axis_data, x_axis_ref, y_axis_ref, x_axis_label, y_axis_label, legend_1, legend_2, title, extra_legend

def valid_wang_fig_4c (): 
    K_ins = 0.1
    thickness_ins = 0.050
    length = 50000 #m

    T_i = 100
    DN = 1 #m
    T_s = 0
    var_para = 2.5

    var_para_min = 1
    var_para_max = 5

    iteration = 1000
    delta = (var_para_max-var_para_min)/iteration

    x_plot = []
    rel_h_plot = []
    for i in range (iteration +1) :
        var_para = var_para_min + delta*i
        temp_set, density_set, cp_set = wang_properties()
        density = np.interp(T_i,temp_set,density_set)
        cp = np.interp(T_i,temp_set,cp_set)

        m_dot = density*np.pi*(DN/2)*(DN/2)*var_para

        R = thermal_resistance(DN, thickness_ins, K_ins)
        delta_T = temp_change(T_i, T_s, length, cp, m_dot, R)
        rel_h = delta_T/(T_i-50)*100

        rel_h_plot.append(rel_h)
        x_plot.append (var_para)
    #print(rel_h_plot)

    x_axis_data = [x_plot]
    y_axis_data = [rel_h_plot]

    x_axis_label = "Flow Velocity (ms-1)"
    y_axis_label = "Relative Heat Loss (%)"

    legend_1 = ["Model"]
    legend_2 = ["Wang (2022)"]

    title = "Validation of Wang (2022) Fig 4c"

    x_data = []
    for i in range (9) :
        x_data.append(var_para_min + i*((var_para_max-var_para_min)/8))
    
    y_data = [37.80, 25.92, 19.88, 16.02, 13.45, 11.57, 10.33, 9.09, 8.35]
    
    x_axis_ref = [x_data]
    y_axis_ref = [y_data]

    extra_legend = "" # External data that want to show in legend
    return x_axis_data, y_axis_data, x_axis_ref, y_axis_ref, x_axis_label, y_axis_label, legend_1, legend_2, title, extra_legend

def valid_wang_fig_4d (): 
    K_ins = 0.1
    thickness_ins = 0.050
    length = 50000 #m

    T_i = 100
    DN = 1 #m
    var_para = 0
    v = 2.5

    var_para_min = -40
    var_para_max = 40

    iteration = 1000
    delta = (var_para_max-var_para_min)/iteration

    x_plot = []
    rel_h_plot = []
    for i in range (iteration +1) :
        var_para = var_para_min + delta*i
        temp_set, density_set, cp_set = wang_properties()
        density = np.interp(T_i,temp_set,density_set)
        cp = np.interp(T_i,temp_set,cp_set)

        m_dot = density*np.pi*(DN/2)*(DN/2)*v

        R = thermal_resistance(DN, thickness_ins, K_ins)
        delta_T = temp_change(T_i, var_para, length, cp, m_dot, R)
        rel_h = delta_T/(T_i-50)*100

        rel_h_plot.append(rel_h)
        x_plot.append (var_para)
    #print(rel_h_plot)

    x_axis_data = [x_plot]
    y_axis_data = [rel_h_plot]

    x_axis_label = "Surrounding Temperature, Ts (°C)"
    y_axis_label = "Relative Heat Loss (%)"

    legend_1 = ["Model"]
    legend_2 = ["Wang (2022)"]

    title = "Validation of Wang (2022) Fig 4d"

    x_data = []
    for i in range (9) :
        x_data.append(var_para_min + i*((var_para_max-var_para_min)/8))
    
    y_data = [22.70, 20.96, 19.36, 17.73, 16.10, 14.49, 12.91, 11.26, 9.68]
    
    x_axis_ref = [x_data]
    y_axis_ref = [y_data]

    extra_legend = "" # External data that want to show in legend
    return x_axis_data, y_axis_data, x_axis_ref, y_axis_ref, x_axis_label, y_axis_label, legend_1, legend_2, title, extra_legend

def valid_Lu () :
    m_dot = 0.089
    T_1 = 167
    T_3 = 28
    Tamb = 25
    cp_fluid = 2370
    K_ins = 0.035
    Cp_ins = 128
    Di = 0.0445*2
    Do = 0.0953*2
    L = 1.24

    iteration = 1000

    R_ins = np.log(Do/Di) / 2 / np.pi / K_ins
    q_dot = (T_1 - T_3) / (R_ins)
    
    R_plots = []
    T_plots = []
    diameter_range = (Do-Di)
    increment = diameter_range / iteration
    for i in range (iteration+1) : 
        D_var = Di + increment*i 
        T_ans = T_1 + (T_3 - T_1 ) / np.log(Do/Di) * np.log(D_var/Di)
        R_plots.append(D_var/2)
        T_plots.append(T_ans)

    R_plot = [R_plots]
    T_plot = [T_plots]

    T_69 = np.interp(0.069,R_plots,T_plots)
    print(T_69)
    
    R_label = "Pipe Radius (m)"
    T_label = "Temperature (°C)"

    legend_model = ["Model"]
    legend_paper = ["Lu (2024)"]

    title = "Radial Temperature Distribution in Insulator"

    external_word_legend = "Heat Transfer = " + str(round(q_dot,2)) + " W"

    R_paper = [[0.0445,0.069,0.0953]]
    T_paper = [[167, 87.3, 28]]
    return R_plot,T_plot,R_paper,T_paper,R_label,T_label,legend_model,legend_paper,title,external_word_legend

def valid_zhang () : #Failed
    length = 2.5 #m
    DN  = 0.05 #m
    T_i = 40
    T_amb = 20
    cp = 4182
    density = 992.2
    m_dot = 82.5/3600
    K = 0.6178
    h = -16.233
    
    length_plot = []
    Temp_plot = []

    iteration = 1000
    delta = length/iteration
    for i in range (iteration) : 
        len = delta * i 
        R = 1/h/(np.pi*DN*length)
        T_L = temp_cal(T_i, T_amb, len, cp, m_dot, R)

        length_plot.append(len)
        Temp_plot.append(T_L)
    
    x_axis_data = [length_plot]
    y_axis_data = [Temp_plot]

    x_axis_label = "length (m)"
    y_axis_label = "Temperature (°C)"

    legend_1 = ["Model"]
    legend_2 = ["Zhang (2020)"]

    title = "Validation Zhang (2020) for Axial Temperature Distribution"

    x_axis_ref = [[]]
    y_axis_ref = [[]]

    extra_legend = "" # External data that want to show in legend
    return x_axis_data, y_axis_data, x_axis_ref, y_axis_ref, x_axis_label, y_axis_label, legend_1, legend_2, title, extra_legend


if __name__ == '__main__' :
    x_plot,y_plot,x2_plot,y2_plot,label_x,label_y, legend_1,legend_2,title,external_data = valid_wang_fig_3a ()
    #print(y_plot)
    for i in range (len(x_plot)): 
        plt.plot(x_plot[i],y_plot[i],label=legend_1[i] )
        plt.plot(x2_plot[i],y2_plot[i], 'x', label = legend_2[i])
    if len(str(external_data)) > 5 :
        plt.plot([],[],' ',label = external_data)
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()