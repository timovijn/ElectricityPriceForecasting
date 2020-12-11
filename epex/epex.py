# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
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

# os.chdir("./nordpool")


# %%
flist = [f for f in sorted(os.listdir("./raw")) if not (f.startswith('.') or f.startswith('~'))]

print(flist)

for filename in flist:
    print(filename)
    y = int(filename[:4])
    print(y)
    if y == 2019:
        df = pd.read_excel(f"./raw/{filename}", header = None, skip_blank_lines=True, decimal=',', thousands='.')
        df = df.replace('Instrument code', 'Instrumentcode')
        df = df.replace('Contract type', 'Contracttype')
        df = df.dropna(how = 'all', axis = 0)
        df = df.dropna(how = 'all', axis = 1)
        df = df.reset_index(drop = True)
        
        df.columns = df.iloc[0]
        df = df.drop(0)

        df1 = df[~df['Instrumentcode'].str.contains('NL ID ')]
        df2 = df[df['Instrumentcode'].str.contains('NL ID ')]

        df1['Date'] = pd.to_datetime(df1['Instrumentcode'].str[:7], format = '%d%b%y')
        df2['Date'] = pd.to_datetime(df2['Instrumentcode'].str.replace("NL ID ", "").str[:7], format = '%y%b%d')
        df = pd.concat([df1, df2]).sort_index()

        df = df[df['Date'].dt.year == y]

        df['Time'] = (df['Instrumentcode'].str[-2:].astype('int64') - 1).astype('str')
        df['Date'] = pd.to_datetime(df['Date'].dt.strftime("%Y-%m-%d") + ' ' + df['Time'].astype(str) + ':00:00')

        df['Price'] = df['Price'].astype('float')
        df['Volume'] = df['Volume'].astype('float')

        df.to_pickle(f"./{os.path.splitext(filename)[0]}.pkl")


# %%
flist = [f for f in sorted(os.listdir("./close")) if not (f.startswith('.') or f.startswith('~'))]

print(flist)
big_df = pd.DataFrame()

for filename in flist:
    print(filename)
    df = pd.read_excel(f"./close/{filename}", skip_blank_lines=True, decimal=',', thousands='.')
    # df = df.replace('Instrument code', 'Instrumentcode')
    # df = df.replace('Contract type', 'Contracttype')
    df['period_from'] = df['period_from'].astype('str')
    df['period_until'] = df['period_until'].astype('str')
    df['period_from'] = df['period_from'].str[-8:]
    df['period_until'] = df['period_until'].str[-8:]
    df = df.dropna(how = 'all', axis = 0)
    df = df.dropna(how = 'all', axis = 1)
    df = df.reset_index(drop = True)
    df['Time'] = df['period_from'].str[0:2]
    df['Date'] = pd.to_datetime(df['datum'].dt.strftime("%Y-%m-%d") + ' ' + df['Time'] + ':00:00')
    print(df)
    df_group3 = df.drop([], axis=1).groupby([(df['Date'].dt.year), (df['Date'].dt.month), (df['Date'].dt.day), (df['Date'].dt.hour)]).mean()
    df_group3['Date'] = df_group3.index
    df_group3['Date'] = pd.to_datetime(df_group3['Date'], format='(%Y, %m, %d, %H)')
    df_group3 = df_group3.set_index(pd.DatetimeIndex(df_group3['Date']))
    print(df_group3)

    big_df['Imbalance'] = df_group3['take_from_system_EUR_MWh']


# %%



# %%
years = ['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
years = ['2019']
country = 'NL'

dfo = pd.DataFrame()
dfo2 = pd.DataFrame()
price = []
volume = []
breaks = []

for y in years:
    i = years.index(y)

    df = pd.read_pickle(f"./{y}_Intraday.pkl")

    # df['Price'] = df['Price'].astype('float')
    # df['Volume'] = df['Volume'].astype('float')
    # print(df['Price'])
    # print(df['Volume'])

    df['Creation timestamp (GMT)'] = pd.to_datetime(df['Creation timestamp (GMT)'], format='%d-%m-%Y %H:%M:%S')

    volume_buy = df.loc[df['Contracttype'] == 'Spot'].loc[df['Side'] == 'buy', 'Volume'].sum()
    volume_sell = df.loc[df['Contracttype'] == 'Spot'].loc[df['Side'] == 'sell', 'Volume'].sum()

    price_buy = df.loc[df['Contracttype'] == 'Spot'].loc[df['Side'] == 'buy', 'Price'].sum()
    price_sell = df.loc[df['Contracttype'] == 'Spot'].loc[df['Side'] == 'sell', 'Price'].sum()

    df_group = df.drop(['Instrumentcode', 'Contracttype', 'Side'], axis=1).groupby([(df['Date'].dt.year),(df['Date'].dt.month)]).sum()
    df_group['Date'] = df_group.index
    df_group['Date'] = pd.to_datetime(df_group['Date'], format='(%Y, %m)')

    df_group2 = df.drop(['Instrumentcode', 'Contracttype', 'Side'], axis=1).groupby([(df['Date'].dt.year), (df['Date'].dt.month), (df['Date'].dt.day)]).mean()
    df_group2['Date'] = df_group2.index 
    df_group2['Date'] = pd.to_datetime(df_group2['Date'], format='(%Y, %m, %d)')

    df_group3 = df.drop(['Instrumentcode', 'Contracttype', 'Side'], axis=1).groupby([(df['Date'].dt.year), (df['Date'].dt.month), (df['Date'].dt.day), (df['Date'].dt.hour)]).mean()
    df_group3['Date'] = df_group3.index
    df_group3['Date'] = pd.to_datetime(df_group3['Date'], format='(%Y, %m, %d, %H)')
    print(df_group3)

    df_group = df_group.set_index(pd.DatetimeIndex(df_group['Date']))
    df_group2 = df_group2.set_index(pd.DatetimeIndex(df_group2['Date']))
    df_group3 = df_group3.set_index(pd.DatetimeIndex(df_group3['Date']))

    dfo = dfo.append(df_group, ignore_index = False)
    dfo2 = dfo2.append(df, ignore_index = False)
    breaks.append(len(dfo))

    price.append(df['Price'].sum())
    volume.append(df['Volume'].sum())
    
    print('')
    print(colored('...','white'))
    print('')
    print(colored(f'Year: {y}', 'blue'))
    print('')
    print(colored(f'Price: {int(round(price[i]))} Euro', 'blue'))
    print(colored(f'Volume: {int(round(volume[i]))} MWh', 'blue'))
    print('')

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(df_group['Date'], df_group['Volume'], width=10)
    ax.set_title(f'Monthly intraday sum volume for {country} for the year {y} (EPEX)')
    ax.set_xlabel(r'Time (months)')
    ax.set_ylabel(r'Volume (MWh)')
    plt.show()

    fig, ax = plt.subplots(figsize=(50, 5))
    ax.bar(df_group2['Date'], df_group2['Price'])
    ax.set_title(f'Daily intraday mean price for {country} for the year {y} (EPEX)')
    ax.set_xlabel(r'Time (months)')
    ax.set_ylabel(r'Price (€)')
    plt.show()

print('')
print(colored('...','white'))
print('')
print(colored(f'Period: {years[0]}–{years[-1]}', 'blue'))
print(colored(f'Price: {int(round(sum(price)))} Euro', 'blue'))
print(colored(f'Volume: {int(round(sum(volume)))} MWh', 'blue'))
print('')
print(colored('...','white'))
print('')

big_df = big_df.merge(df_group3['Price'], how='outer', left_index=True, right_index=True)
big_df['Percentage'] = np.divide(np.subtract(big_df['Price'], big_df['Imbalance']), big_df['Imbalance'])
print(big_df)

df['Time to delivery'] = df['Date'] - df['Creation timestamp (GMT)']
df['Time to delivery'] = df['Time to delivery'] / np.timedelta64(1, 'h')
# df['Time to delivery'] = (df['Date'] - df['Creation timestamp (GMT)']).astype('timedelta64[h]')
print(df)


# %%
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.bar(big_df.index, big_df['Percentage'], width=20)
# ax.set_title(f'Percentual difference average EPEX Intraday and TenneT Settlement prices for {country} for the period {years[0]}–{years[-1]}')
# ax.set_xlabel(r'Time (months)')
# ax.set_ylabel(r'Percentage (%)')

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(big_df.index, big_df['Percentage'])
ax.set_title(f'Percentual difference average EPEX Intraday and TenneT Settlement prices for {country} for the period {years[0]}–{years[-1]}')
ax.set_xlabel(r'Time (months)')
ax.set_ylabel(r'Percentage (%)')


# %%



# %%
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(dfo['Date'], dfo['Volume'], width=20)
ax.set_title(f'Monthly intraday volume for {country} for the period {years[0]}–{years[-1]} (EPEX)')
ax.set_xlabel(r'Time (months)')
ax.set_ylabel(r'Volume (MWh)')


# %%
datetime_of_interest = '2019-06-03 23:00:00'
filtered_dates = df.loc[df["Date"] == datetime_of_interest]
filtered_dates = df.loc[df["Date"] == datetime_of_interest]

fig, ax = plt.subplots(figsize=(10, 5))
x = filtered_dates['Time to delivery']
y = filtered_dates['Price']
ax.set_xlim(x.min() - 1, x.max() + 1)
ax.set_ylim(y.min() - 1, y.max() + 1)
ax.scatter(x, y, s=filtered_dates['Volume'].apply(lambda x: x*5), alpha=0.5)
ax.set_title(f'Price distribution for {datetime_of_interest} (EPEX)')
ax.set_xlabel(r'Time to delivery (hours)')
ax.set_ylabel(r'Price (€/MWh)')
ax.invert_xaxis()


# %%
# QUANTILES

filtered_dates["Volume_weighted"] = filtered_dates["Price"] * filtered_dates["Volume"]

quantiles = [0, 10, 25, 45, 55, 75, 90, 100]
quantiles_val = list()
quantiles_idx = list()

for q in quantiles:
    quantiles_val.append(filtered_dates['Price'].quantile(q/100))
    quantiles_idx.append(f'Q{q}')

print(quantiles_val)
print(quantiles_idx)

# print(quantiles_val / filtered_dates['Volume_weighted'].sum())

print(filtered_dates['Price'].sort_values().reset_index(drop=True))

fig, ax = plt.subplots(figsize=(10, 5))
x = filtered_dates['Price'].sort_values().reset_index(drop=True).index
y = filtered_dates['Price'].sort_values().reset_index(drop=True)
# ax.set_xlim(x.min() - 1, x.max() + 1)
# ax.set_ylim(y.min() - 1, y.max() + 1)
ax.scatter(x, y)
ax.set_title(f'Cumulative price distribution for {datetime_of_interest} (EPEX)')
ax.set_xlabel(r'-')
ax.set_ylabel(r'Price (€/MWh)')
[ax.axhline(q) for q in quantiles_val]

fig, ax = plt.subplots(figsize=(10, 5))
x = filtered_dates['Volume'].sort_values().reset_index(drop=True).index
y = filtered_dates['Volume'].sort_values().reset_index(drop=True)
# ax.set_xlim(x.min() - 1, x.max() + 1)
# ax.set_ylim(y.min() - 1, y.max() + 1)
ax.scatter(x, y)
ax.set_title(f'Cumulative volume distribution for {datetime_of_interest} (EPEX)')
ax.set_xlabel(r'-')
ax.set_ylabel(r'Volume (MWh)')
# [ax.axhline(q) for q in quantiles_val]


# %%



