#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression


# In[8]:


df = pd.read_csv('sample.csv',index_col = 'Index')


# In[9]:


df['test_score'].fillna(df['test_score'].mean(),inplace=True)


# In[10]:


df['experience'].fillna(0,inplace=True)


# In[11]:


x = df.drop(['Unnamed: 5','Unnamed: 6'],axis=1)


# In[12]:


y = df['salary']


# In[13]:


lr = LinearRegression()


# In[14]:


lr.fit(x,y)


# In[15]:


pickle.dump(lr,open('model.pkl','wb'))

