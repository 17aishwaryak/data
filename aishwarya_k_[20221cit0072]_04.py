# -*- coding: utf-8 -*-
"""Aishwarya k [20221cit0072] 04

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18MhgYTC5WvLxIyDuohOv2lThKhmt65Wi
"""

import pandas as pd
meteorites = pd.read_csv('/content/Meteorite_Landings_20240305 (1).csv',nrows=5)
meteorites

meteorites.name

meteorites.columns

meteorites.index

import requests

response = requests.get(
    'https://data.nasa.gov/resource/gh4g-9sfh.json',
    params={'$limit':50_000}
)

if response.ok:
  payload = response.json()
else:
  print(f'Request was not successful and returned code:{response.status_code}.')
  payload = None

import pandas as pd
df=pd.DataFrame(payload)
df.head(3)

meteorites.info()

meteorites[100:104]

meteorites.iloc[100:104,[0,3,4,6]]



import pandas as pd
import numpy as np
import matplotlib.pyplot as pllt

cars_data=pd.read_csv("/content/archive (1).zip",index_col=0,na_values=['??','????'])

cars_data.info()

cars_data.dropna(axis=0,inplace=True)
cars_data

plt.scatter(cars_data['Age'],cars_data['Price'],c ='red')
plt.title('scatter plot of Price VS Age')
plt.xlabel('Age(month)')
plt.ylabel('Price(Euros)')
plt.show()

plt.hist(cars_data['KM'])

plt.hist(cars_data['KM'], color ='green', edgecolor='white', bins=30)
plt.title('Histogram of KM')
plt.xlabel('Kilometers')
plt.ylabel('Frequency')
plt.show()

counts=[979,120,2]
fueltype=('Petrol','Diesel','CNG')
index = np.arange(len(fueltype))

plt.bar(index, counts, color=['red', 'blue', 'cyan'])
plt.title('Barplot plot of FuelType')
plt.xlabel('Fuel Type')
plt.ylabel('Frequency')
plt.xticks(index, fueltype,rotation = 90)
plt.show()