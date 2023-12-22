#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'20',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '5249b94d-4aba-4672-a900-e21ab78a6673',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


# In[2]:


type(data)


# In[3]:


import pandas as pd

#This allows you to see all the columns
pd.set_option('display.max_columns', None)


# In[4]:


#Normalizing the data
df = pd.json_normalize(data['data'])
df['timestamp'] = pd.to_datetime('now')
df


# In[5]:


def api_runner():
    global df
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'20',
        'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '5249b94d-4aba-4672-a900-e21ab78a6673',
    }

    session = Session()
    session.headers.update(headers)

    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
    
    import pandas as pd

    #This allows you to see all the columns
    pd.set_option('display.max_columns', None)
    
    #Normalizing the data
    
    df2 = pd.json_normalize(data['data'])
    df2['timestamp'] = pd.to_datetime('now')
    df= pd.concat([df, df2])
    
    if not os.path.isfile(r"C:\Users\Admin\Downloads\csv files\API3.csv"):
        df.to_csv(r"C:\Users\Admin\Downloads\csv files\API3.csv", header='column_names')
    else:
        df.to_csv(r"C:\Users\Admin\Downloads\csv files\API3.csv", mode='a', header=False)


# In[6]:


import os
from time import time
from time import sleep

for i in range(333):
    api_runner()
    print('API ran sucessfully')
    sleep(60)
exit()
    


# In[7]:


df


# In[9]:


pd.set_option('display.float_format', lambda x: '%5f' % x)


# In[16]:


df


# In[17]:


df6= df.groupby('name', sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d']].mean()
df6


# In[18]:


df7 = df6.stack()
df7


# In[19]:


type(df7)


# In[20]:


df8 = df7.to_frame(name='values')
df8


# In[ ]:





# In[21]:


df8.count()


# In[22]:


index= pd.Index(range(120))

df8= df7.reset_index()
df8


# In[ ]:





# In[23]:


df9= df8.rename(columns= {'level_1': 'percent_change'})
df9


# In[25]:


df10= df9.rename(columns= {0: 'values'})
df10


# In[26]:


df10['percent_change']= df10['percent_change'].replace(['quote.USD.percent_change_1h', 'quote.USD.percent_change_24h', 'quote.USD.percent_change_7d', 'quote.USD.percent_change_30d', 'quote.USD.percent_change_60d', 'quote.USD.percent_change_90d'], ['1H', '24H', '7D', '30D', '60D', '90D'])
df10


# In[27]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[28]:


sns.catplot(x='percent_change', y='values', hue= 'name', data=df10, kind='point')


# In[29]:


df11= df[['name', 'quote.USD.price', 'timestamp']]
df11= df11.query('name =="Bitcoin"')
df11


# In[30]:


sns.set_theme(style= "darkgrid")

sns.lineplot(x= 'timestamp', y= 'quote.USD.price', data=df11)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




