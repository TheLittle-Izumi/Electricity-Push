import pandas as pd
import numpy as np
import pvlib

from pvlib.pvsystem import PVSystem, FixedMount
from pvlib.location import Location
from pvlib.modelchain import ModelChain
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS

def importPSMData(datacwd): 
    df = pd.read_csv(datacwd)
    Lat = df['Latitude'][0]
    Lot = df['Longitude'][0]

    df.rename(columns={'DHI':'dhi','DNI':'dni','GHI':'ghi','Temperature':'temp_air', 
         'Wind Speed':'wind_speed'},inplace=True) 
    df.rename(columns={'Year':'year','Month':'month','Day':'day','Hour':'hour', 
         'Minute':'minute'},inplace=True)
    df['dt'] = pd.to_datetime(df[['year', 'month', 'day', 'hour', 'minute']]) 
    df.set_index(df['dt'],inplace=True) 
    
    return df ,Lat ,Lot


dircwd = 'solar_data/'
temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']
sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')
cec_inverters = pvlib.pvsystem.retrieve_sam('cecinverter')
sandia_module = sandia_modules['BP_Solar_BP3220N_Module___2010_']
cec_inverter = cec_inverters['ABB__ULTRA_1100_TL_OUTD_3_US_690_x_y_z__690V_']



system = PVSystem(surface_tilt=25, surface_azimuth=200,
                module_parameters=sandia_module,
                inverter_parameters=cec_inverter,
                temperature_model_parameters=temperature_model_parameters 
                ,modules_per_string=20,strings_per_inverter=9000
                )

for i in range(1,10) :
    cwd = dircwd + 'station' + str(i) + '/tmy.csv'
    weatherData, Lat, Lot = importPSMData(cwd)

    location = Location(latitude=Lat, longitude=Lot)

    mc = ModelChain(system, location)

    mc.run_model(weatherData)

    # print(mc.results.aoi)  #incident angle
    # print(mc.results.cell_temperature)  #cell_temperature
    # print(mc.results.dc)  #dc power
    # print(mc.results.ac)  #ac power

    aca = mc.results.ac

    outputpath=dircwd + 'station' + str(i) + '/ac.xlsx'

    result = pd.DataFrame({'time':aca.index,'ac':aca.values})

    result.to_excel(outputpath,index=False,header=False)

    sum = 0
    for i in aca :
        if i > 0 :
            sum += i
    print(Lat,Lot,sum/10000000)

print('---')
for i in range(1,4) :
    cwd = dircwd + 'mulhub' + str(i) + '/tmy.csv'
    weatherData, Lat, Lot = importPSMData(cwd)

    location = Location(latitude=Lat, longitude=Lot)

    mc = ModelChain(system, location)

    mc.run_model(weatherData)

    # print(mc.results.aoi)  #incident angle
    # print(mc.results.cell_temperature)  #cell_temperature
    # print(mc.results.dc)  #dc power
    # print(mc.results.ac)  #ac power

    aca = mc.results.ac

    outputpath=dircwd + 'mulhub' + str(i) + '/ac.xlsx'

    result = pd.DataFrame({'time':aca.index,'ac':aca.values})

    result.to_excel(outputpath,index=False,header=False)

    sum = 0
    for i in aca :
        if i > 0 :
            sum += i
    print(Lat,Lot,sum/10000000)