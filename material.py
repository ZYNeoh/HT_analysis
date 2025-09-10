# Material Properties Reading

import numpy as np 
import pandas as pd

# File path
filename = "C:\\Users\\zyneo\\OneDrive\\Desktop\\P5_Neoh\\1 Main File\\Data\\library_sheet.xlsx"

"""
Data with equations
"""
# Crude Oil

def crude_oil (T) :
    density = (0.902 - (T) * 8.177e-4 + T*T * 1.54e-6) * 1000
    
    if T >= 42 :
        k = 0.152 * np.power(np.e,T*(-9.18e-4))
    elif T >= 32 and T < 42 :
        k = 0.60576 - 0.01186 * T
    elif T < 32 :
        k = 0.25
    
    if T >= 40 :
        dynamic_viscosity_power = 5.06039 - 0.01951 * (T+273.15)
    elif T >= 25 and T < 40 :
        dynamic_viscosity_power = 37.30785 - 0.12235 * (T+273.15)
    elif T >= 23 and T < 25 :
        dynamic_viscosity_power = -14.44979 - 0.0511 * (T+273.15)
    elif T < 23 :
        dynamic_viscosity_power = 20.81207 - 0.06799 * (T+273.15)
    dynamic_viscosity = np.power(10,dynamic_viscosity_power)
    kinematic_viscosity = dynamic_viscosity / density

    if T >= 52 :
        cp = 809.717 + 3.607 * (T+273.15)
    elif T >= 32 and T < 52 :
        cp = -76349.22 + 568.75 * (T+273.15) - 1.01 * (T+273.15) * (T+273.15) 
    elif T < 32 :
        cp = -11987.72 + 82.15 * (T+273.15) - 0.10979 * (T+273.15) * (T+273.15)

    pr = dynamic_viscosity * cp / k

    return density, cp, k, kinematic_viscosity, pr


"""
Directly Read From Sources (Excel)
"""
def data_set_clean_float(sample_set) :
    clean_data_set = []
    for i in range (len(sample_set)) :
        if str(sample_set[i]).lower() != "nan" :
            clean_data_set.append(float(sample_set[i]))
    return clean_data_set 

def data_set_clean_str(sample_set) :
    clean_data_set = []
    for i in range (len(sample_set)) :
        if str(sample_set[i]).lower() != "nan" :
            clean_data_set.append(str(sample_set[i]))
    return clean_data_set 

def clean_float_data(series): # Remove Nan and conver tupe to float
    return series.dropna().astype(float).tolist()

def read_excel_data(file, sheet, columns):
    df = pd.read_excel(file, sheet_name=sheet)
    return {col: clean_float_data(df[col]) for col in columns}



# Fluid Properties
fluid_sheets = {
    "sat_water": {
        "sheet": "A-9 Sat_water",
        "columns": ['Temp', 'Density_L', 'Cp_L', 'k_L', 'Kinematic_viscosity_L', 'Pr_L']
    },
    "air": {
        "sheet": "A-15 Ambient Air",
        "columns": ['Temp', 'Density', 'Cp', 'k', 'Kinematic Viscosity', 'Pr']
    },
    "engine_oil": {
        "sheet": "Engine_Oil",
        "columns": ['Temp', 'Density', 'Cp', 'k', 'Kinematic_Viscosity', 'Pr']
    },
    "methane": {
        "sheet": "Methane_Gas",
        "columns": ['Temp', 'Density', 'Cp', 'k', 'Kinematic_Viscosity', 'Pr']
    }
}

# Read and clean all fluids
fluid_data = {}
for fluid, info in fluid_sheets.items():
    fluid_data[fluid] = read_excel_data(filename, info["sheet"], info["columns"])


def fluid_material (selection, temperature) :
    data_set_wfluid_temp = [
        fluid_data["sat_water"]["Temp"],
        fluid_data["engine_oil"]["Temp"],
        fluid_data["methane"]["Temp"],
        [0]# Crude Oil
    ]

    data_set_wfluid_density = [
        fluid_data["sat_water"]["Density_L"],
        fluid_data["engine_oil"]["Density"],
        fluid_data["methane"]["Density"],
        [0]# Crude Oil
    ]

    data_set_wfluid_cp = [
        fluid_data["sat_water"]["Cp_L"],
        fluid_data["engine_oil"]["Cp"],
        fluid_data["methane"]["Cp"],
        [0]# Crude Oil
    ]

    data_set_wfluid_k = [
        fluid_data["sat_water"]["k_L"],
        fluid_data["engine_oil"]["k"],
        fluid_data["methane"]["k"],
        [0]# Crude Oil
    ]

    data_set_wfluid_kinematic_viscosity = [
        fluid_data["sat_water"]["Kinematic_viscosity_L"],
        fluid_data["engine_oil"]["Kinematic_Viscosity"],
        fluid_data["methane"]["Kinematic_Viscosity"],
        [0]# Crude Oil
    ]

    data_set_wfluid_pr = [
        fluid_data["sat_water"]["Pr_L"],
        fluid_data["engine_oil"]["Pr"],
        fluid_data["methane"]["Pr"],
        [0]# Crude Oil
    ]

    if selection == 3 : 
        out_density, out_cp, out_k, out_kinematic_viscosity, out_pr = crude_oil (temperature)
    else :
        temp            = data_set_wfluid_temp [selection]
        dens            = data_set_wfluid_density [selection]
        cp              = data_set_wfluid_cp [selection]
        k               = data_set_wfluid_k [selection]
        kinematic_vis   = data_set_wfluid_kinematic_viscosity [selection]
        pr              = data_set_wfluid_pr [selection]

        out_density             = np.interp(temperature, temp, dens)
        out_cp                  = np.interp(temperature, temp, cp)
        out_k                   = np.interp(temperature, temp, k)
        out_kinematic_viscosity = np.interp(temperature, temp, kinematic_vis)
        out_pr                  = np.interp(temperature, temp, pr)

    return out_density, out_cp, out_k, out_kinematic_viscosity, out_pr


# Ambient Air Properties

def amb_prop (selection, temeprature) :
    
    data_set_air_prop = [
        fluid_data['air']['Temp'],
        fluid_data['air']['k'],
        fluid_data['air']['Pr'],
        fluid_data['air']['Kinematic Viscosity']
    ]

    out_k = np.interp(temeprature, data_set_air_prop[0], data_set_air_prop[1])
    out_Pr = np.interp(temeprature, data_set_air_prop[0], data_set_air_prop[2])
    out_kinematic_vis = np.interp(temeprature, data_set_air_prop[0], data_set_air_prop[3])

    return out_k, out_Pr, out_kinematic_vis


# Pipe Material
pipe_mat_sheets = {
    "Copper": {
        "sheet": "TC_Pipe_Mat",
        "columns": ['Temp_K', 'Copper']
    },
    "Aluminum": {
        "sheet": "TC_Pipe_Mat",
        "columns": ['Temp_K', 'Aluminum']
    },
    "Iron": {
        "sheet": "TC_Pipe_Mat",
        "columns": ['Temp_K', 'Iron']
    }
}

pipe_mat_data = {}
for mat_data, info in pipe_mat_sheets.items():
    pipe_mat_data[mat_data] = read_excel_data(filename, info["sheet"], info["columns"])

def pipe_mat_prop (selection, temperature) : 
    temperature_K = temperature + 273.15
    data_set_p_mat_k = [
        pipe_mat_data["Copper"]["Copper"],
        pipe_mat_data["Aluminum"]["Aluminum"],
        pipe_mat_data["Iron"]["Iron"]
    ]
    
    data_set_p_mat_Temp = [
        pipe_mat_data["Copper"]["Temp_K"],
        pipe_mat_data["Aluminum"]["Temp_K"],
        pipe_mat_data["Iron"]["Temp_K"]
    ]

    out_k = np.interp(temperature_K, data_set_p_mat_Temp[selection], data_set_p_mat_k[selection])

    return out_k


# Insulator Properties
def read_excel_sheet (filename, sheet_name) :
    df = pd.read_excel(filename, sheet_name)
    return df

sheet_name_insulator = "TC_Insulator"

dr = read_excel_sheet(filename, sheet_name_insulator)

data_set_insulator_mat = np.array(dr['Material'])
data_set_insulator_mat_k = np.array(dr['Thermal_Conductivity'])

if __name__ == "__main__" : 
    print("Complete Run")