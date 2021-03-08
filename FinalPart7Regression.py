# -*- coding: utf-8 -*-
"""
Created on Sun Feb  21 4:18 2021

Author: Lucas Edmisten
Date: 3/7/2021
Assignment: Final Part 7 DSC530
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

print(nfldata["FantPt"])


nfldata, live, others = first.MakeFrames()
nfldata = nfldata[nfldata.FantPt>30]


import statsmodels.formula.api as smf
model = smf.ols('Height', data=nfldata)
results = model.fit()
results.summary()