import os
os.system('clear')
import cv2
import time
import numpy as np
import imutils
from datetime import datetime
from SecretColors.palette import Palette
material = Palette("material",color_mode="rgb255")
from termcolor import colored
import matplotlib.pyplot as plt
from tkinter import Tk
from scipy.spatial.distance import pdist, squareform
import seaborn
import pandas as pd

os.chdir("./Elbas volumes")
df = pd.read_html("./elbas-volumes_2019_hourly.xls", header=[2,3], decimal=',', thousands='.')
df = df[0]
df = df[['NL']]
df.to_csv("./csv.csv", index=False)
print(df)

from matplotlib.pyplot import figure
figure(num=None, figsize=(16, 12), dpi=80, facecolor='w', edgecolor='k')

df.plot(legend=False)
# plt.axis('off')
plt.show()
# plt.xticks(np.arange(min(df), max(df)+1, 1000))