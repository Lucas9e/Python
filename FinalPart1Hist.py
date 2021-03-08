# -*- coding: utf-8 -*-
"""
Created on Sun Feb  21 4:18 2021

Author: Lucas Edmisten
Date: 3/7/2021
Assignment: Final Part 1 DSC530
"""

from __future__ import print_function, division

import matplotlib.pyplot as plt
%matplotlib inline

import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

import numpy as np
import pandas as pd
import first
import random

import thinkstats2
import thinkplot


nfldata = pd.read_excel(r'C:\Users\jptho\dsc520\NFLdatanew.xlsx')

nfldata = nfldata.dropna()

print (nfldata)


print(nfldata[["Age", "Conference", "DraftRound", "Shuttle"]].describe())
print(nfldata[["Collegewins", "Forty", "Wonderlic", "FantPt"]].describe())

# plt.hist(nfldata['Age'], bins=range(21,38,1), edgecolor="black")
# plt.xlabel("Age of Players")
# plt.ylabel('Number of Players')
# plt.title('Age Distribution')

ax = plt.hist(nfldata['Conference'], edgecolor="black", color="red")         
plt.xlabel("Conference")
plt.ylabel('Number of Players')
plt.title('College Conference Disribution')
plt.xticks(rotation=90)

nfldata.plot(kind='hist',x='FantPt',y='Collegewins', color="yellow", edgecolor="black")

nfldata.plot(kind='hist',x='FantPt',y='Age', color="pink", edgecolor="black")

nfldata.plot(kind='hist',x='FantPt',y='DraftRound', color='green', edgecolor="black")

nfldata.plot(kind='hist',x=None ,y='FantPt', color='purple', edgecolor="black")


# shuttledata = nfldata[nfldata.Shuttle != 0]
# shuttledata.plot(kind='hist',x='FantPt',y='Shuttle', edgecolor="black")




