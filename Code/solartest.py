import os 
import pandas as pd 
import numpy as np 
import pvlib 
from pvlib.pvsystem import PVSystem , FixedMount
from pvlib.location import Location 
from pvlib.modelchain import basic_chain, ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

def importPSMData(): 
    df = pd.read_csv('C:\\Users\\ASUS\\Desktop\\Datathon\\code\\solartest.csv')
    #Rename paramters for input to PVlib 
    df.rename(columns={'DHI':'dhi','DNI':'dni','GHI':'ghi','Temperature':'temp_air', 
         'Wind Speed':'wind_speed'},inplace=True) 
    #Rename date parameters in order to run to_datetime 
    df.rename(columns={'Year':'year','Month':'month','Day':'day','Hour':'hour', 
         'Minute':'minute'},inplace=True)
    df['dt'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']]) 
    #Set index to DT for run_model call 
    df.set_index(df['dt'],inplace=True) 
    #Drop unnecessary columns 
    df = df.drop('Dew Point', axis=1) 
    df = df.drop('Pressure', axis=1) 
    df = df.drop('year', axis=1) 
    df = df.drop('month', axis=1) 
    df = df.drop('day', axis=1) 
    df = df.drop('hour', axis=1) 
    df = df.drop('minute', axis=1) 
    df = df.drop('dt',axis=1) 
    return df 

temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod') 
cec_inverters = pvlib.pvsystem.retrieve_sam('cecinverter') 

# module = sandia_modules['BP_Solar_BP3220N_Module___2010_'] #18% eff, c-Si 
# inv = cec_inverters['ABB__ULTRA_1100_TL_OUTD_3_US_690_x_y_z_690V__CEC_2013_'] 

module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
inv = cec_inverters['ABB__MICRO_0_25_I_OUTD_US_208__208V_']

system = PVSystem(surface_tilt=20, surface_azimuth=200,
                  module_parameters=module,
                  inverter_parameters=inv,
                  temperature_model_parameters=temperature_model_parameters,
                  modules_per_string=23,strings_per_inverter=9897, 
            modules_per_string=23,strings_per_inverter=9897)

loc = Location(latitude=31.513,longitude=65.619)

mc = ModelChain(system,loc)

weather = pd.DataFrame([[1034, 919, 139, 33.4, 5.3]],
                       columns=['ghi', 'dni', 'dhi', 'temp_air', 'wind_speed'],
                       index=[pd.Timestamp('20170701 1200', tz = 'Asia/Kabul')])

# weatherData = importPSMData() 
mc.run_model(weather) 
print(mc.ac)