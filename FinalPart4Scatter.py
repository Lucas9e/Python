# -*- coding: utf-8 -*-
"""
Created on Sun Feb  21 4:18 2021

Author: Lucas Edmisten
Date: 3/7/2021
Assignment: Final Part 4 DSC530
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

nfldatas = nfldata.dropna()


def SampleRows(nfldata, nrows, replace=False):
    indices = np.random.choice(nfldata.index, nrows, replace=replace)
    sample = nfldata.loc[indices]
    return sample


sample = SampleRows(nfldata, 3000)
FantPtsamp, Fortysamp, Wonderlicsamp = sample.FantPt, sample.Forty, sample.Wonderlic

thinkplot.Scatter(FantPtsamp, Fortysamp, alpha=1)
thinkplot.Config(xlabel='Fantasy Points',
                 ylabel='Forty Yard Dash Time')

