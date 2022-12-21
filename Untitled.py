#!/usr/bin/env python
# coding: utf-8

# # Lab Session Notebook - Returns
# 
# ## From Prices to Returns
# 
# In this lab we'll work the very basics of Returns - computing returns, and compounding a sequence of returns.
# 
# Let's start with a set of prices for a stock "A", in a python list:

# In[2]:


prices_a = [8.70, 8.91, 8.71]


# Recall that the return from time $t$ to time ${t+1} is given by:
# 
# $$ R_{t,t+1} = \frac{P_{t+1}-P_{t}}{P_{t}} $$
# 
# or alternately
# 
# $$ R_{t,t+1} = \frac{P_{t+1}}{P_{t}} - 1 $$
# 
# If you come from R or another language that supports vectors, you might expect something like this to work:
# 
# ```python
# returns_a = prices_a[:-1]/prices_a[1:] - 1
# ```
# 
# However, since Python lists do not operate as vectors, that will not work, generating an error about "/" not working for lists.

# In[5]:


# WILL NOT WORK - THIS WILL GENERATE AN ERROR!
# prices_a[1:]/prices_a[:-1] -1


# Instead, we can convert them to a numpy array. Numpy arrays do behave like vectors, so this works:

# In[6]:


import numpy as np

prices_a = np.array([8.70, 8.91, 8.71])
prices_a


# In[7]:


prices_a[1:]


# In[8]:


prices_a[:-1]


# In[12]:


prices_a[:2]


# In[15]:


prices_a[1:]/prices_a[:-1] - 1


# In[16]:


import pandas as pd


# In[23]:


prices = pd.DataFrame({"BLUE": [8.7, 8.91, 8.71, 8.43, 8.73],
                      "ORANGE": [10.66, 11.08, 10.71, 11.59, 12.11]
                      })


# In[24]:


prices


# In[25]:


prices.iloc[1:]


# In[26]:


prices.iloc[:-1]


# In[28]:


prices.iloc[1:]/prices.iloc[:-1]


# To solve the unusual results on the table cell above you can refer to the course crash course. But the solution is to add .Values

# In[31]:


prices.iloc[1:].values/prices.iloc[:-1] - 1


# In[34]:


prices.iloc[1:]/prices.iloc[:-1].values


# In[36]:


prices/prices.shift(1)


# In[37]:


prices.pct_change()


# In[45]:


import pandas as pd


# In[46]:


df = pd.read_csv("C:\\Users\\user\\Desktop\\sample_prices.csv")


# In[47]:


df.head()


# In[48]:


prices = pd.read_csv("C:\\Users\\user\\Desktop\\sample_prices.csv")
prices


# In[49]:


returns = prices.pct_change()


# In[50]:


returns


# In[51]:


prices.plot()


# In[52]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[53]:


returns.plot.bar()


# In[54]:


returns.std()


# In[55]:


returns.tail()


# In[56]:


returns.mean()


# In[57]:


returns.median()


# In[58]:


returns+1


# In[59]:


np.prod(returns+1)


# In[60]:


np.prod(returns+1) - 1


# In[62]:


(returns+1).prod()-1


# In[63]:


((returns+1).prod()-1)*100


# In[64]:


(((returns+1).prod()-1)*100).round(2)


# # ANNUALIZATION

# In[65]:


rm = 0.01
(1+rm)**12


# In[68]:


rq = 0.04
(1+rq)**4 - 1


# In[69]:


rd = 0.0001
(1+rd)**252-1


# In[ ]:




