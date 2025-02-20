# -*- coding: utf-8 -*-
"""Titanic-survival.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xnIbmQ1MzYM7ja9zrfHIGPxduqlgkhpS
"""

pip install scikit-learn

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score

data=pd.read_csv('/content/Titanic-Dataset.csv')
data.head()

data.isnull().sum()

"""**Shuffling and creating Train and train set**"""

from sklearn.utils import shuffle
data=shuffle(data,random_state=42)
#createing 4 division
div=int(data.shape[0]/4)
#3 parts to train and 1 for test
train=data.iloc[:3*div+1]
test=data.iloc[3*div+1:]
train.shape,test.shape

train.head()

test.head()

"""**Simple mode**"""

test['simple_mode']=train['Survived'].mode()[0]
test['simple_mode'].head()

simple_mode_accuracy=accuracy_score(test['Survived'],test['simple_mode'])
simple_mode_accuracy

"""**Mode Based on Gender**"""

gender_mode=train.groupby('Sex')['Survived'].agg(lambda x:x.mode()[0])
gender_mode

test['gender_mode']=test['Sex'].map(gender_mode)
test['gender_mode'].head()

gender_accuracy=accuracy_score(test['Survived'],test['gender_mode'])
gender_accuracy