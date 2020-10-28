import os
os.system('clear')

import numpy as np
import pandas as pd
import datetime

from termcolor import colored
from SecretColors.palette import Palette
material = Palette("material", color_mode = 'hexa')

hex_salmon = '#F68F83'
hex_gold = '#BC9661'
hex_indigo = '#2D2E5F'
hex_maroon = '#8C4750'
hex_white = '#FAFAFA'
hex_blue = '#7EB5D2'

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.dates import DateFormatter
import matplotlib.dates as dates
mpl.rcParams['font.family'] = 'SF Compact Text'
mpl.rcParams['font.weight'] = 'medium'
mpl.rcParams['axes.titleweight'] = 'semibold'
mpl.rcParams['axes.labelweight'] = 'medium'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=[hex_indigo, hex_salmon, hex_maroon])

import pygrib

# os.chdir("./nordpool")

import numpy as np
import matplotlib.pyplot as plt
import pygrib # import pygrib interface to grib_api

def grab_data(s):
    gribs = pygrib.open(s)

    gribs.seek(0)
    for grb in gribs:
        print(grb) 

    print('Success')

    # print('Grabbing reference to all temperature values')
    # tempObj = gribs.select(name='2 metre temperature')

    print('Grabbing reference to all pressure values')
    pressureObj = gribs.select(name='Mean sea level pressure')

    # print('Grabbing reference to all relative humidity values')
    # humidityObj = gribs.select(name='Relative humidity')

    # print('Grabbing reference to all u-wind components')
    # uwindObj = gribs.select(name='U component of wind')

    # print ('Grabbing reference to all v-wind components')
    # vwindObj = gribs.select(name='V component of wind')

    ylen = len(pressureObj[0].values)
    xlen = len(pressureObj[0].values[0])

    data = [[[[]]]]
    for h in range(0, len(pressureObj)):
        print('Loading values from height:', h)
        types = [[[]]]
        # types.append(tempObj[h].values)
        if h < len(pressureObj):
            types.append(pressureObj[h].values)
        else:
            types.append([[0]*xlen]*ylen)

        # if h < len(humidityObj):
        #     types.append(humidityObj[h].values)
        # else:
        #     types.append([[0]*xlen]*ylen)

        # # if h < len(uwindObj):
        # #     types.append(uwindObj[h].values)
        # # else:
        # #     types.append([[0]*xlen]*ylen)

        # # if h < len(vwindObj):
        # #     types.append(vwindObj[h].values)
        # else:
        #     types.append([[0]*xlen]*ylen)
        data.append(types)
    npdata = np.array(data)
    return npdata


data = grab_data('./harmonie/20201027_154453_.grb')
# data = grab_data('./harmonie/HA40_N25_201910290000_04800_GB.grb')
# data = grab_data('./harmonie/test.grb2')

Z = data[-4][1]

Y = list(range(0, len(data[1][1])))
X = list(range(0, len(data[1][1][0])))
print(Y)
print(X)

X, Y = np.meshgrid(X, Y)

plt.figure()
plt.contourf(X, Y, Z)
plt.colorbar()
plt.show()