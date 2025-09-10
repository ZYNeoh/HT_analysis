#Library

#Roughness Values
#epsilon (material, condition) in string return epsilon_value as float

#fluid_property (fluid type) in string return (density (kgm-3), kinematics viscosity (m2s-1)) as float


#Roughness Values
def epsilon (material,condition) :
    material_set = ["steel", "iron", "brass", "plastic", "concrete", "rubber", "wood"]
    material_value = [0, 0, 0.002, 0.0015, 0, 0.01, 0.5]
    condition_set = ["sheet metal", "stainless", "commercial", "riveted","rusted", "cast", "wrought", "galvanized", "asphalted cast", "smoothed", "rough" ]
    condition_value = [0.05, 0.002, 0.046, 3.0, 2.0, 0.26, 0.046, 0.15, 0.12, 0.04, 2.0]
    
    material0 = str(material)
    condition0 = str(condition)
    material1 = material0.lower()
    condition1 = condition0.lower()
    
    decision = 0
    i = 0
    
    while decision == 0 :
        if material1 == material_set[i]:
            if i == 0 or i == 1 or i == 4 :
                decision_1 = 0
                j = 0
                while decision_1 == 0 :
                    if condition1 == condition_set[j] :
                        decision_1 = 1 
                        decision = 1
                        epsilon_value = condition_value[j]
                    else :
                        decision_1=0
                        j = j+1
                    
                    if j >= len(condition_set) :
                        decision_1 =1
                        decision = 1
                        print ("Condition not found, set epsilon value = 1")
                        epsilon_value = 1
            else :
                decision = 1
                epsilon_value = material_value[i]
        else : 
            decision = 0
            i = i+1
        
        if i >= len(material_set) : 
            decision = 1
            print("Material not found, set epsilon value = 1")
            epsilon_value = 1
    return epsilon_value


#Fluid Property
def fluid_property (fluid) :
    fluid_set = ["h2", "he", "h2o", "ar", "dry air", "co2", "co", "n2", "o2", "no", "n2o", "cl2", "ch4", "ammonia", "benzene", "carbon tetrachloride", "ethanol", "ethylene glycol", "freon 12", "gasoline", "glycerin", "kerosene", "mercury", "methanol", "sae 10w oil", "sae 10w30 oil", "sae 30w oil", "sae 50w oil", "water", "seawater (30)"]
    fluid_density_set = [0.0837749694251936, 0.166123114553608, 0.749082755809213, 1.66123114553608, 1.20260905014268, 1.82429677945373, 1.16184264166327, 1.16184264166327, 1.33509987770077, 1.23318385650224, 1.82429677945373, 2.94537301263759, 0.666530779, 608, 881, 1590, 789, 1117, 1327, 680, 1260, 804, 13550, 791, 870, 876, 791, 902, 998, 1025]
    fluid_viscosity_set = [9.05E-6, 1.97E-5, 1.02E-5, 2.24E-5, 1.8E-5, 1.48E-5, 1.82E-5, 1.76E-5, 2E-5, 1.90E-5, 1.45E-5, 1.03E-5, 1.34E-5, 2.2E-4, 6.51E-4, 9.67E-4, 1.20E-3, 2.14E-2, 2.62E-4, 2.92E-4, 1.49, 1.92E-3, 1.56E-3, 5.98E-4, 1.04E-1, 1.7E-1, 2.9E-1, 8.6E-1, 1E-3, 1.07E-3]
    
    fluid0 = str(fluid)
    fluid1 = fluid0.lower()
    condition = 0
    i = 0
    while condition == 0 :
        if fluid1 == fluid_set[i] :
            condition = 1 
            density = fluid_density_set[i]
            viscosity = fluid_viscosity_set[i]
        else :
            condition = 0 
            i = i+1 
            
        if i >= len(fluid_set) :
            condition = 1 
            print("Fluid type error, set density = 1000, and kinematic viscosity = 1E-6")
            density = 1000
            viscosity = 1E-3
    
    kinematic_viscosity = viscosity/density

    return density, kinematic_viscosity


#Minor Loses 

#Minor Loses of Usual Joint
def minor_loses_usual_join (Joint_Type, Connection_Type, Nominal_diameter) : #Need to use inch
    joint_type_set = ["Globe Valves (Fully Open)", "Gate (Fully Open)", "Swing Check (Fully Open)", "Angle (Fully Open)", "Elbows - 45 regular", "Elbows - 45 long radius", "Elbows - 90 regular", "Elbows - 90 long radius", "Elbows - 180 regular", "Elbows -180 long radius", "Tees - Line Flow", "Tees - Branch Flow"]
    value_set = [[14, 8.2, 6.9, 5.7, 13, 8.5, 6.0, 5.8, 5.5], [0.30, 0.24, 0.16, 0.11, 0.80, 0.35, 0.16, 0.07, 0.03], [5.1, 2.9, 2.1, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0], [9.0, 4.7, 2.0, 1.0, 4.5, 2.4, 2.0, 2.0, 2.0], [0.39, 0.32, 0.30, 0.29,0 ,0 ,0 ,0, 0], [0, 0, 0, 0, 0.21, 0.20, 0.19, 0.16, 0.14], [2.0, 1.5, 0.95, 0.64, 0.50, 0.39, 0.30, 0.26, 0.21],[1.0, 0.72, 0.41, 0.23, 0.40, 0.30, 0.19, 0.15, 0.10], [2.0, 1.5, 0.95, 0.64, 0.41, 0.35, 0.30, 0.25, 0.20], [0, 0, 0, 0, 0.40, 0.30, 0.21, 0.15, 0.10], [0.90, 0.90, 0.90, 0.90, 0.24, 0.19, 0.14, 0.10, 0.07], [2.4, 1.8, 1.4, 1.1, 1.0, 0.80, 0.64, 0.58, 0.41]]
    diameter_set = [0.5, 1.0, 2.0, 4.0, 1.0, 2.0, 4.0, 8.0, 20.0]
    type_set = ["screwed", "flanged"]
    joint_type_0 = str(Joint_Type).lower()
    connection_type_0 = str(Connection_Type).lower()
    diameter_0 = float(Nominal_diameter)/0.0254
    minor_loses = 0
    passing = 0

    for i in range(len(joint_type_set)) :
        if joint_type_set[i].lower() == joint_type_0 :
            passing = passing +1
            for j in range (len(type_set)) :
                if connection_type_0 == type_set [j].lower() : 
                    passing = passing + 1
                    current_i = j *4 
                    if current_i == 4 :
                        current_range = 5
                    else :
                        current_range = 4
                    for k in range (current_range):
                        if diameter_0 == diameter_set[k+current_i] :
                            passing = passing + 1
                            minor_loses_0 = value_set[i]
                            minor_loses = minor_loses_0 [k+current_i]
                            if minor_loses == 0 :
                                print("The particular Data does not exist")
                                print("Minor Loses assumed as 1")
                                minor_loses = 1
    
    if minor_loses == 0 :
        print ("Error, minor loses = 0")
        if passing == 0 :
            print ("Joint Type Error")
        elif passing == 1 :
            print("Connection Type Error")
        elif passing == 2 :
            print ("Nominal Diameter does not existed")

    return minor_loses

#Partially Open

def minor_loses_partial_open (type_0, status) :
    operation_status = str(status).lower()
    operation_type = str(type_0).lower()
    status_set = ["Quarter Close", "Half Close", "Three Quarter Close"]
    type_set = ["Gate", "Disk", "Globe"]
    value_set = [[20, 3.9, 1], [20, 3, 0.5], [15, 6, 4]]
    minor_loses = 0
    passing = 0

    for i in range(len(status_set)): 
        if operation_status == status_set[i].lower(): 
            passing = passing +1
            for j in range(len(type_set)): 
                if type_set[j].lower() == operation_type :
                    passing = passing +1
                    minor_loses_0 = value_set[j]
                    minor_loses = minor_loses_0[i]

    if minor_loses == 0 :
        print ("Error, minor loses = 0")

        if passing == 0 :
            print ("Status Error, only accept Quarter Close, Half Close, Three Quarter Close")
        elif passing == 1 :
            print("Type Error")

    return minor_loses


#Bending

def minor_loses_bending(theta, Radius, nominal_diameter): 
    theta_set = [45, 90, 180]
    x_value = float(Radius)/nominal_diameter
    value_set = [[0.15, 0.11, 0.107, 0.11, 0.205, 0.29], [0.24, 0.19, 0.2, 0.3, 0.485], [0.275, 0.23, 0.21, 0.26, 0.55,0.97]]
    x_value_set = [[1.1, 2, 2.5, 3, 10, 15], [1.13, 2.5, 4, 8.9, 15], [1.4, 1.9, 2.1, 3, 8, 15]]
    minor_loses = 0
    passing = 0

    for i in range (len(theta_set)): 
        if theta_set[i] == theta: 
            passing = passing +1
            current_x_value_set = x_value_set[i]
            current_value_set = value_set[i]

    if passing == 0 :
        print ("There is no data for the theta. Only 45, 90, 180 is accepted")
    else: 
        if x_value < current_x_value_set [0] :
            print("The pipe ratio is below than the minimum, hence no data. Set minor loses = 0")
        elif x_value> current_x_value_set[-1] : 
            print ("The pipe ratio is exceed the maximum, hence no data. Set minor loses = 0")
        else :
            for i in range (len(current_x_value_set)-1): 
                if x_value == current_x_value_set[i] :
                    minor_loses = current_value_set[i]
                elif x_value < current_x_value_set[i+1] and x_value > current_x_value_set[i] :
                    minor_loses = current_value_set[i+1] - ((current_x_value_set[i+1] - x_value) / (current_x_value_set[i+1] - current_x_value_set[i])*(current_value_set[i+1] - current_value_set[i]))


    return minor_loses

#Inlet
def minor_loses_inlet () :
    minor_loses = 0.5
    return minor_loses

# sudden
def minor_loses_sudden () :
    minor_loses = 0
    return minor_loses

#Gradually
def minor_loses_gradually() : 
    minor_loses = 0
    return minor_loses

def minor_loses_selection (selection,JT, status_type, nominal_diameter, theta, radius) :
    selection_set = ["Usual Joint Type", "Partially Open", "Pipe Bend", "Inlets", "Sudden", "Gradually"]
    selection_current = str(selection).lower()
    minor_loses = 0

    for i in range (len(selection_set)): 
        if selection_set[i].lower() == selection_current :
            type_selection = i 
    
    if type_selection == 0 :
        minor_loses = minor_loses_usual_join(JT, status_type, nominal_diameter)
    elif type_selection == 1 :
        minor_loses = minor_loses_partial_open(JT, status_type)
    elif type_selection == 2 :
        minor_loses = minor_loses_bending(theta, radius, nominal_diameter)
    elif type_selection == 3 :
        minor_loses = minor_loses_inlet () #Need Update ya
    elif type_selection == 4 :
        minor_loses = minor_loses_sudden ()
    elif type_selection == 5 :
        minor_loses = minor_loses_gradually()

    return minor_loses


#Table A-15 Thermo Text book
def A_15 (temp) : 
    temp_data_set = [-150, -100, -50, -40, -30, -20, -10, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100, 120, 140, 160, 180, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800, 900, 1000, 1500, 2000]
    density_data_set = [2.866, 2.038, 1.582, 1.514, 1.451, 1.394, 1.341, 1.292, 1.269, 1.246, 1.225, 1.204, 1.184, 1.164, 1.145, 1.127, 1.109, 1.092, 1.059, 1.028, 0.9994, 0.9718, 0.9458, 0.8977, 0.8542, 0.8148, 0.7788, 0.7459, 0.6746, 0.6158, 0.5664, 0.5243, 0.488, 0.4565, 0.4042, 0.3627, 0.3289, 0.3008, 0.2772, 0.199, 0.1553]
    specific_heat_data_set = [983, 966, 999, 1002, 1004, 1005, 1006, 1006, 1006, 1006, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1007, 1008, 1008, 1009, 1011, 1013, 1016, 1019, 1023, 1033, 1044, 1056, 1069, 1081, 1093, 1115, 1135, 1153, 1169, 1184, 1234, 1264]
    thermal_conductivity_data_set = [0.01171, 0.01582, 0.01979, 0.02057, 0.02134, 0.02211, 0.02288, 0.02364, 0.02401, 0.02439, 0.02476, 0.02514, 0.02551, 0.02588, 0.02625, 0.02662, 0.02699, 0.02735, 0.02808, 0.02881, 0.02953, 0.03024, 0.03095, 0.03235, 0.03374, 0.03511, 0.03646, 0.03779, 0.04104, 0.04418, 0.04721, 0.05015, 0.05298, 0.05572, 0.06093, 0.06581, 0.07037, 0.07465, 0.07868, 0.09599, 0.11113]
    thermal_diffusivity_data_set = [0.000004158, 0.000008036, 0.00001252, 0.00001356, 0.00001465, 0.00001578, 0.00001696, 0.00001818, 0.0000188, 0.00001944, 0.00002009, 0.00002074, 0.00002141, 0.00002208, 0.00002277, 0.00002346, 0.00002416, 0.00002487, 0.00002632, 0.0000278, 0.00002931, 0.00003086, 0.00003243, 0.00003565, 0.00003898, 0.00004241, 0.00004593, 0.00004954, 0.0000589, 0.00006871, 0.00007892, 0.00008951, 0.0001004, 0.0001117, 0.0001352, 0.0001598, 0.0001855, 0.0002122, 0.0002398, 0.0003908, 0.0005664]
    dynamic_viscosity_data_set = [0.000008636, 0.00001189, 0.00001474, 0.00001527, 0.00001579, 0.0000163, 0.0000168, 0.00001729, 0.00001754, 0.00001778, 0.00001802, 0.00001825, 0.00001849, 0.00001872, 0.00001895, 0.00001918, 0.00001941, 0.00001963, 0.00002008, 0.00002052, 0.00002096, 0.00002139, 0.00002181, 0.00002264, 0.00002345, 0.0000242, 0.00002504, 0.00002577, 0.0000276, 0.00002934, 0.00003101, 0.00003261, 0.00003415, 0.00003563, 0.00003846, 0.00004111, 0.00004362, 0.000046, 0.00004826, 0.00005817, 0.0000663]
    kinematic_viscosity_data_set = [0.000003013, 0.000005837, 0.000009319, 0.00001008, 0.00001087, 0.00001169, 0.00001252, 0.00001338, 0.00001382, 0.00001426, 0.0000147, 0.00001516, 0.00001562, 0.00001608, 0.00001655, 0.00001702, 0.0000175, 0.00001798, 0.00001896, 0.00001995, 0.00002097, 0.00002201, 0.00002306, 0.00002522, 0.00002745, 0.00002975, 0.00003212, 0.00003455, 0.00004091, 0.00004765, 0.00005475, 0.00006219, 0.00006997, 0.00007806, 0.00009515, 0.0001133, 0.0001326, 0.0001529, 0.0001741, 0.0002922, 0.000427]
    prandtl_number_data_set = [0.7246, 0.7263, 0.744, 0.7436, 0.7425, 0.7408, 0.7387, 0.7362, 0.735, 0.7336, 0.7323, 0.7309, 0.7296, 0.7282, 0.7268, 0.7255, 0.7241, 0.7228, 0.7202, 0.7177, 0.7154, 0.7132, 0.7111, 0.7173, 0.7041, 0.7014, 0.6992, 0.6974, 0.6946, 0.6935, 0.6937, 0.6948, 0.6965, 0.6986, 0.7037, 0.7092, 0.7149, 0.7206, 0.726, 0.7478, 0.7539]

    proceed = 0

    if temp < temp_data_set[0] or temp > temp_data_set[-1]: 
        print("The input temperature is out of range. All element set as 1")
        proceed = 1 
    
    if proceed == 0 : 
        for i in range (len(temp_data_set)): 
            if temp_data_set[i] == temp :
                output_density = density_data_set[i]
                output_specific_heat = specific_heat_data_set[i]
                output_thermal_conductivity = thermal_conductivity_data_set[i]
                output_thermal_diffusivity = thermal_diffusivity_data_set[i]
                output_dynamic_viscosity = dynamic_viscosity_data_set [i]
                output_kinematic_viscosity = kinematic_viscosity_data_set[i]
                output_prandtl_number = prandtl_number_data_set[i]
            elif temp > temp_data_set[i] and temp < temp_data_set[i+1] :  
                output_density = density_data_set[i]-(temp_data_set[i]-temp)*(density_data_set[i]-density_data_set[i+1])/(temp_data_set[i]-temp_data_set[i+1])
                output_specific_heat = specific_heat_data_set[i]-(temp_data_set[i]-temp)*(specific_heat_data_set[i]-specific_heat_data_set[i+1])/(temp_data_set[i]-temp_data_set[i+1])
                output_thermal_conductivity = thermal_conductivity_data_set[i]-(temp_data_set[i]-temp)*(thermal_conductivity_data_set[i]-thermal_conductivity_data_set[i+1])/(temp_data_set[i]-temp_data_set[i+1])
                output_thermal_diffusivity = thermal_diffusivity_data_set[i]-(temp_data_set[i]-temp)*(thermal_diffusivity_data_set[i]-thermal_diffusivity_data_set[i+1])/(temp_data_set[i]-temp_data_set[i+1])
                output_dynamic_viscosity = dynamic_viscosity_data_set[i]-(temp_data_set[i]-temp)*(dynamic_viscosity_data_set[i]-dynamic_viscosity_data_set[i+1])/(temp_data_set[i]-temp_data_set[i+1])
                output_kinematic_viscosity = kinematic_viscosity_data_set[i]-(temp_data_set[i]-temp)*(kinematic_viscosity_data_set[i]-kinematic_viscosity_data_set[i+1])/(temp_data_set[i]-temp_data_set[i+1])
                output_prandtl_number = prandtl_number_data_set[i]-(temp_data_set[i]-temp)*(prandtl_number_data_set[i]-prandtl_number_data_set[i+1])/(temp_data_set[i]-temp_data_set[i+1])

    else : 
        output_density = 1
        output_specific_heat = 1
        output_thermal_conductivity = 1
        output_thermal_diffusivity = 1
        output_dynamic_viscosity = 1
        output_kinematic_viscosity = 1
        output_prandtl_number = 1

    return output_density, output_specific_heat, output_thermal_conductivity, output_thermal_diffusivity, output_dynamic_viscosity, output_kinematic_viscosity, output_prandtl_number
