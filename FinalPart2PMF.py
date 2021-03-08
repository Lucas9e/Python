# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 17:58:05 2021

Author: Lucas Edmisten
Date: 3/7/2021
Assignment: Final Part 2 DSC530
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


pmf = thinkstats2.Pmf(nfldata.FantPt)

Age = first.MakeFrames()
College_Wins_pmf = thinkstats2.Pmf(nfldata.Collegewins, label='College Wins PMF')
College_Losses_pmf = thinkstats2.Pmf(nfldata.Collegelosses, label="College Losses PMF")

thinkplot.PrePlot(2, cols=2)
thinkplot.Hist(College_Wins_pmf, align='right')
thinkplot.Hist(College_Losses_pmf, align='left')
thinkplot.Config(xlabel='Amount of Wins or Losses', ylabel='PMF')
