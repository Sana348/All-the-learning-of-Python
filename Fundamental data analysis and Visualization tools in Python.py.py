#!/usr/bin/env python
# coding: utf-8

# In[85]:


print('hello world')


# In[86]:


import numpy as np


# In[87]:


a = np.array([1,2,3])
print(a)
print(a.shape)
print(a[0],a[1],a[2])
a[0] = 5
print(a)
b = np.array([[1,2,3],
              [4,5,6]])
print(b)
print(b.shape)
print(b[0,0])

c = np.array([1.0, 2.1, 3.4])
print(c)


# In[88]:


a = np.zeros((2,3))
print(a)

b = np.ones((1,2))
print(b)

c = np.full((2,3),7)
print(c)

e = np.random.random((3,3))
print(e)


# In[89]:


a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9,10,11,12]])
print(a)

b = a[:2,1:3]
print(b)

print(a[0,1])
b[0,0] = 75
print(a[0,1])
print(a)


# In[90]:


a = np.array([[1,2],
              [3,4],
              [5,6]])

print(a)

print(a > 2)

print(a[a>2])


# In[91]:


x = np.array([[1,2],
              [3,4]])
y = np.array([[5,6],
              [7,8]])

print(np.add(x,y))

print(np.subtract(x,y))

print(np.multiply(x,y))

print(x/y)


# In[92]:


print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))


# In[93]:


import pandas as pd


# In[94]:


s = pd.Series(['sam','nam','sue','ehte','romi'])
print(s)

print(s[0])

print(s[1:4])

print(s[[0,1,3]])

param = s != 'sam'
print(s[param])


# In[95]:


d = {'new york':1300,
     'chicago':900,
     'san francisco':1100,
     'austin':450}

cities = pd.Series(d)
print(cities)


# In[96]:


cities[['chicago','san francisco']]


# In[97]:


cities[cities < 1000]


# In[98]:


cities[cities < 1000] = 750
print(cities)


# In[99]:


import numpy as np
import matplotlib.pyplot as plt


# In[100]:


plt.plot([1,7,9,14])


# In[101]:


plt.plot([1,2,7,8],[1,9,7,14])


# In[102]:


plt.plot([1,2,7,8],[1,9,7,14],'ro')


# In[103]:


a= np.array([[1,2,3,4],
             [5,6,7,8]])

plt.plot(a[0], a[1], 'go')


# In[104]:


plt.xlabel('x-aixs')
plt.ylabel('y-aixs')

plt.plot(a[0], a[1], 'b--')


# In[105]:


t = np.linspace(0,5,20)

plt.plot(t, t**2, color ='coral', linestyle='--')
plt.plot(t, 4*t, color='indigo', linewidth=2)


# In[106]:


plt.subplot(1,3,1)
plt.plot(t,t,'c--')

plt.subplot(1,3,2)
plt.plot(t,t**2,'b-')

plt.subplot(1,3,3)
plt.plot(t,t**3,'mo')


# In[107]:


grades = {'sam':70,
          'nam':82,
          'sue':92,
          'ehte':76,
          'romi':97}

plt.bar(range(len(grades)), list(grades.values()), color='darkturquoise')
plt.xticks(range(len(grades)),list(grades.keys()))
plt.xlabel('students')
plt.ylabel('grades')


# In[108]:


x= np.random.randn(1000)

plt.hist(x, color='seagreen')


# In[109]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[117]:


df = pd.read_csv('Data.txt', index_col=0, encoding='unicode-escape')

df.head()


# In[ ]:





# In[ ]:





# In[ ]:


df_copy = df.drop(['total', 'stage', 'legendary'], axis=1)

sns.boxplot()


# In[1]:


get_ipython().system('python -m pip install --upgrade pip')


# In[2]:


get_ipython().system('pip3 install plotly')


# In[3]:


import plotly.express as px
import pandas as pd
import numpy as np


# In[ ]:




