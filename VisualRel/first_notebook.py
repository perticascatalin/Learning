# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

print('start list dir')

for dirname, _, filenames in os.walk('./input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
print('finish list dir')
   
print('start load data')

df_rel = pd.read_csv('./input/challenge-2019-train-vrd.csv')

print ('finish load data')

# Any results you write to the current directory are saved as output.

print (df_rel['RelationshipLabel'].value_counts())
#print (df_rel['LabelName1'].value_counts())
#print (df_rel['LabelName2'].value_counts())
df_rel['ImageID'].value_counts()
df_rel.sample(5)
#df_rel['LabelName1'].head()

class_name_dict = {}

def map_to_name(label_name):
    #class_name = class_name_dict(label_name)
    class_name = 'beer'
    choice = random.choice('ab')
    if choice == 'a':
        class_name = 'milk'
    return class_name

print (map_to_name('alpha'))
print (map_to_name('beta'))
print (map_to_name('gamma'))

same_thing_repeated = df_rel[['LabelName2']][df_rel.LabelName2 == '/m/083vt']
print(same_thing_repeated.head())
translated = same_thing_repeated.apply(lambda x : map_to_name(x), axis = 1)
print(translated.head())

#numerical = ['XMin1', 'XMax1', 'YMin1', 'YMax1', 'XMin2', 'XMax2', 'YMin2', 'YMax2']
#df_rel[numerical].hist(bins=15, figsize=(20, 10), layout=(2, 4));