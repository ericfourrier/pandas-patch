# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 00:34:33 2015

@author: efourrier

Purpose : the puropose of this modest patch is to create some new methods for
the class Dataframe in order to simplify a data scientist life 
"""
import pandas as pd 
from pandas import DataFrame
from pandas import read_csv

test = DataFrame(read_csv('lc_test.csv'))

def nacolcount(self):
    """ count the number of missing values per columns """
    return self.apply(lambda x: sum(pd.isnull(x)),axis = 0 )
    
def narowcount(self):
    """ count the number of missing values per rows """
    return self.apply(lambda x: sum(pd.isnull(x)),axis = 1 )

pd.DataFrame.nacolcount = nacolcount
pd.DataFrame.narowcount = narowcount

# test 
test.nacolcount()
test.narowcount()