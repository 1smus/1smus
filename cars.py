#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


cars = pd.read_csv(r"C:\Users\User\Documents\Python Projects\2. Cars Data1.csv")


# In[3]:


cars.head(5)


# Find all the null vaues in the data set. If there is ant null value in any column, then fill it with the mean of that column

# In[4]:


cars.shape


# In[7]:


cars.isnull().sum()


# In[11]:


cars["Cylinders"].fillna(cars["Cylinders"].mean(), inplace = True)


# In[12]:


cars.isnull().sum()


# In[15]:


cars["EngineSize"].fillna(cars["EngineSize"].mean(), inplace = True)


# Check what are the differnet types of make are there in our dataset and what is the count (occurence) of each make in the data

# In[16]:


cars.head(2)


# In[17]:


cars["Make"].value_counts()


# Show all the records where Origin is Asia or Europe

# In[18]:


cars.head()


# In[23]:


cars[cars["Origin"].isin(["Asia","Europe",])].head(30)


# Check what are the differnt types of Make are there in our dataset. And, what is the count(occurence) of each Make in the data?

# In[28]:


cars["Make"].value_counts()


# Show the records where Origin is Asia or America

# In[40]:


cars[cars["Origin"].isin(["Asia","America"])]


# Remove all the records(rows) where Weight is above 4000

# In[41]:


cars.head()


# In[47]:


cars[~(cars["Weight"]>4000)]


# Increase all the values of MPG_city column by 3

# In[48]:


cars.head()


# In[49]:


cars["MPG_City"] = cars["MPG_City"].apply(lambda x:x+3)


# In[52]:


cars


# In[ ]:





# In[ ]:




