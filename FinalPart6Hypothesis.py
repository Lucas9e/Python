# -*- coding: utf-8 -*-
"""
Created on Sun Feb  21 4:18 2021

Author: Lucas Edmisten
Date: 3/7/2021
Assignment: Final Part 6 DSC530
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



class HypothesisTest(object):

    def __init__(self, data):
        self.data = data
        self.MakeModel()
        self.actual = self.TestStatistic(data)

    def PValue(self, iters=1000):
        self.test_stats = [self.TestStatistic(self.RunModel()) 
                           for _ in range(iters)]

        count = sum(1 for x in self.test_stats if x >= self.actual)
        return count / iters

    def TestStatistic(self, data):
        raise UnimplementedMethodException()

    def MakeModel(self):
        pass

    def RunModel(self):
        raise UnimplementedMethodException()

class CorrelationPermute(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        xs, ys = data
        test_stat = abs(thinkstats2.Corr(xs, ys))
        return test_stat

    def RunModel(self):
        xs, ys = self.data
        xs = np.random.permutation(xs)
        return xs, ys


cleaned = nfldata.dropna(subset=['Age', 'FantPt'])
data = cleaned.Age.values, cleaned.FantPt.values
ht = CorrelationPermute(data)
pvalue = ht.PValue()
print(pvalue, "= Permutation test to compute the p-value of an observed difference in means, we can assume that there is no difference between the groups and generate simulated results by shuffling the data.")


#  distrubution of the test statistic 
ht.PlotCdf()
thinkplot.Config(xlabel='test statistic',
                   ylabel='CDF')

class DiffMeansPermute(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        group1, group2 = data
        test_stat = abs(group1.mean() - group2.mean())
        return test_stat

    def MakeModel(self):
        group1, group2 = self.data
        self.n, self.m = len(group1), len(group2)
        self.pool = np.hstack((group1, group2))

    def RunModel(self):
        np.random.shuffle(self.pool)
        data = self.pool[:self.n], self.pool[self.n:]
        return data

class DiffMeansOneSided(DiffMeansPermute):

    def TestStatistic(self, data):
        group1, group2 = data
        test_stat = group1.mean() - group2.mean()
        return test_stat
    
ht = DiffMeansOneSided(data)
pvalue = ht.PValue()
print(pvalue, "= pvalue for the null hypothesis.")