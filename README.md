# P1 Electricity Push Tree
```
C:. //All tests file are for testing validity
│  ml.py  //Multiple linear regression model for predicting electricity consumption
│  Solar.py //Estimating photovoltaic power generation based on tmy
│  solartest.py
│  test.py
│
├─predict_data
│      data - 副本.xlsx //Data used in multiple linear regression (obtained dataset)
│      data.xlsx //Remove data from the test
│      test.xlsx //Supervised selected (random) test set
│
└─solar_data //Data Source https://nsrdb.nrel.gov/data-viewer
    │  anstest.xlsx
    │  cec.xlsx //Inverter parameters
    │  Railstation Map.xlsx //Station coordinates (highlighted in red as pre screened due to terrain, population, or lighting factors)
    │
    ├─mulhub1
    │      ac.xlsx //Estimated AC power at various time periods throughout the year (calculated)
    │      tmy.csv //Typical meteorological year data (obtained dataset)
    │
    ├─mulhub2
    │      ac.xlsx
    │      tmy.csv
    │
    ├─mulhub3
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station1
    │      2818969_35.25_62.30_2018.csv
    │      2818969_35.25_62.30_2019.csv
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station2
    │      2883805_37.21_65.26_2018.csv
    │      2883805_37.21_65.26_2019.csv
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station3
    │      2909210_30.97_66.42_2018.csv
    │      2909210_30.97_66.42_2019.csv
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station4
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station5
    │      2788265_34.29_60.90_2018.csv
    │      2788265_34.29_60.90_2019.csv
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station6
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station7
    │      2856897_29.45_64.02_2018.csv
    │      2856897_29.45_64.02_2019.csv
    │      ac.xlsx
    │      tmy.csv
    │
    ├─station8
    │      ac.xlsx
    │      tmy.csv
    │
    └─station9
            ac.xlsx
            tmy.csv
```

# P2 The Connection between Photovoltaic Power Generation and Localized Sustainable Development Goals.

- Advantages of Photovoltaic Power Generation: The UN has the six key transitions to the make progess towards the United Nations Sustainable Development Goals, in which Photovoltaic power is clean energy and could be utilized by the country with great solar resources. According to the World Bank Group, Afghanistan happens to be the resourceful one.

- In Afghanistan, extensive sparsely populated regions are located to the north, west, and south of the central mountain range, with the southwestern area, situated at approximately 33 degrees north latitude, serving as a prototypical illustration. Throughout the year, the region experiences ample sunlight and favorable weather conditions, facilitating the operation of photovoltaic modules at full capacity for 7-8 hours per day during the spring and summer seasons.

- Photovoltaic Power Generation not only significantly reduces greenhouse gas emissions but also offers flexible options in both centralized and distributed forms. Given the uneven distribution of urbanization and industrialization in Afghanistan, it is more suitable to adapt to local conditions. For instance, constructing large-scale solar power stations in the industrial zones of the northern and western regions and implementing distributed low-voltage photovoltaic modules near the capital or in mountainous areas can effectively alleviate the problem of excessive grid pressure in certain regions.

- Afghanistan is a major mining country with great potential for industrial development. With the gradual stabilization of the domestic situation and the influx of international capital, the energy issue urgently needs to be addressed. But blindly investing in energy projects, such as traditional thermal power generation, may lead to energy shortages caused by uncontrolled development speed ->improper prediction ->forced reduction of production capacity; Or energy surplus/improper construction planning ->long cost recovery cycle; More importantly, it pollutes the environment. Therefore, we use a multiple linear regression model to predict future development based on 'population trends' and' future industrial development plans', while fully utilizing the characteristics of easy simulation and expansion of photovoltaic power generation to help the Afghan region develop energy more economically.

# P3 Feasibility of integrating photovoltaic power generation into the railway network in Afghanistan

- The main railways in Afghanistan (loop lines and lines connecting various border dry ports) perfectly cover all high population density areas and major mineral areas (or high population density areas and industrial areas are radiating outward along the railway loop line), and the topological structure is simple. The range of radiation along the loop line towards the central and external areas is almost equal and covers most of the electricity consumption areas. Among them, the Kandahar region, Ghazhi region, and various regions in the northwest of the ring road all have conditions for using photovoltaic power generation.

- If the demand for energy in Afghanistan's industry and transportation further increases in the future, the cost of building a traditional power grid will be too high. Many mining areas in Afghanistan are not suitable for building large-scale thermal power plants due to terrain, population density, urban distribution, environmental protection needs, and other reasons. Therefore, photovoltaic power stations distributed on the ring road, land ports, hubs, and industrial areas can not only flexibly choose the construction scale according to local needs or restrictions to meet the local electricity demand, but also flexibly connect surplus electricity to the grid or buy electricity from the railway grid nearby。

- The southwest desert (or further west) in Afghanistan, which is the most suitable area for power generation, requires the connection to the capital and high population density areas or mineral areas in the north to pass through the central mountainous areas, with huge operation and maintenance costs and inconvenient construction of substations or integration into the power grid along the route. Integrating the originally planned transmission network into the railway network not only makes the national power grid more flexible, but also significantly reduces operation and maintenance costs. In addition, Afghanistan may be connected to the Central Asian power grid in the future, and substations located at border dry ports and power grids along border railways can easily connect to external power grids.

# P4 Modelling
## Predicted Electricity Consumption
Using multiple linear regression prediction, the independent variables are [population] [urban population] [industrial GDP], and the dataset is randomly divided into test sets at 8:2. After multiple tests, quadratic regression is the best fit, and it can achieve the score above 0.9 even in very small (very poor) datasets.

Advantages: Compared to traditional fitting, the main consideration is the parameter of industrial GDP, because in the current situation of Afghanistan, industrial electricity needs to be guaranteed first, and Afghanistan should have some planning for future industrial production capacity in the current development situation, which can economically estimate the required electricity consumption to prevent overcapacity from further hitting Afghanistan's already underdeveloped economy

Limitation：Choosing a typical meteorological year as a factor may lead to non-linear effects

## Evaluate and Predict Photovoltaic Production Capacity
Using PVlib, a Python open-source library, and https://nsrdb.nrel.gov/data-viewer Free dataset for. The power generation corresponding to a photovoltaic power station of a certain architecture can be estimated based on regional data of typical meteorological years TMY. Predicting future climate can provide a more accurate understanding of future data. Based on the market price of photovoltaic modules, estimated operation and maintenance costs, it is possible to roughly determine the suitable production capacity and cost recovery period for a certain location. This model was used to evaluate the production capacity of several railway stations that meet the conditions. The same set of photovoltaic modules was used for networking, and the photovoltaic power generation capacity of several stations can be roughly seen.

Limitation: The construction cost and operation and maintenance cost of photovoltaic power plants need to consider factors far beyond the data used in the model, so the most economical networking plan and scale still need to be determined through more detailed on-site investigations.