#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv(r"C:\Users\Admin\Downloads\world_population (1).csv")


# In[3]:


df


# In[4]:


pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[6]:


df.info()


# In[7]:


df.describe()


# In[10]:


df.isnull().sum()


# In[12]:


df.nunique()


# In[16]:


df.sort_values(by="2022 Population", ascending=False).head(10)


# In[25]:


df.corr(numeric_only=True)


# In[31]:


sns.heatmap(df.corr(numeric_only=True), annot=True)

plt.rcParams['figure.figsize']=(20,7)

plt.show()


# In[36]:


df.groupby("Continent").mean(numeric_only=True)


# In[37]:


df[df['Continent'].str.contains('Oceania')]


# In[43]:


df.groupby("Continent").mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)


# In[60]:


df2 = df.groupby("Continent")[['1980 Population',
       '1990 Population', '2000 Population', '2010 Population',
       '2015 Population', '2020 Population', '2022 Population']].mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)
df2


# In[55]:


df.columns


# In[61]:


df3 = df2.transpose()


# In[62]:


df3.plot()


# In[66]:


df.boxplot()


# In[70]:


df.select_dtypes(include='float')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




