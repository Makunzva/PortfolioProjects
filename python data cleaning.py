#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


df = pd.read_excel(r"C:\Users\Admin\Downloads\Customer Call List.xlsx")
df


# In[15]:


df = df.drop_duplicates()
df


# In[9]:


df = df.drop(columns = "Not_Useful_Column")
df


# In[21]:


df["Last_Name"] = df["Last_Name"].str.strip("123._/")


# In[22]:


df


# In[47]:


df['Phone_Number']= df['Phone_Number'].str.replace('[^a-zA-Z0-9]', '', regex=True)
df


# In[50]:


df['Phone_Number']= df['Phone_Number'].apply(lambda x: str(x))


# In[54]:


df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])


# In[61]:


df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('N/a','')
df['Phone_Number'] = df['Phone_Number'].str.replace('NaN--','')
df['Phone_Number'] 


# In[70]:


df["Address"]


# In[81]:


df[["Address", "State", "Zip_Code"]] = df["Address"].str.split(',', expand=True)


# In[82]:


df


# In[87]:


df["Paying Customer"] = df["Paying Customer"].str.replace('Yes', 'Y')
df["Paying Customer"] = df["Paying Customer"].str.replace('No', 'N')
df


# In[88]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('Yes', 'Y')
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace('No', 'N')
df


# In[92]:


df = df.fillna('')
df


# In[94]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
        
df


# In[95]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
        df.drop(x, inplace=True)
        
df


# In[98]:


df = df.reset_index(drop=True)


# In[99]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




