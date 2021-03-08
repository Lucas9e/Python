# -*- coding: utf-8 -*-
"""
Created on Sun Feb  21 4:18 2021

Author: Lucas Edmisten
Date: 3/7/2021
Assignment: Final Part 3 DSC530
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



def EvalCdf(sample, x):
    count = 0.0
    for value in sample:
        if value <= x:
            count += 1

    prob = count / len(sample)
    return prob

# fantasyptslist = nfldata["FantPt"].tolist()
# print(fantasyptslist)

cdf = thinkstats2.Cdf(nfldata.FantPt, label='Fantasy Points')
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Fantasy Points', ylabel='CDF', loc='upper right')