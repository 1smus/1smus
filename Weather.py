#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

data = pd.read_csv(r"C:\Users\User\Documents\Python Projects\1. Weather Data (3).csv")


# In[3]:


data


# In[ ]:



data.head()


# In[5]:


data.shape


# In[6]:


data.index


# In[8]:


data.columns


# In[9]:


data.dtypes


# In[11]:


data["Weather"].unique()


# In[12]:


data.nunique()


# In[15]:


data.count()


# In[16]:


data["Weather"].value_counts()


# In[17]:


data.info()


# Find all the unique "Wind Speed" values in the data

# In[19]:


data.head(3)
data.nunique()


# In[20]:


data["Wind Speed_km/h"].nunique()


# In[21]:


data["Wind Speed_km/h"].unique()


# Find the number of times when the "Weather is exactly clear"

# In[23]:


data.head(3)


# In[24]:


#value_counts
data["Weather"].value_counts()


# In[26]:


#filtering
data[data.Weather == "Clear"]


# In[28]:


#groupby()
data.groupby("Weather").get_group("Clear")


# Find the number of times when the "Wind Speed was exactly 4 knm/h"

# In[30]:


data[data["Wind Speed_km/h"] == 4]


# Find out all the Null values in the data

# In[34]:


data.isnull().sum()


# In[35]:


data.notnull().sum()


# Rename the coloumn name "Weather" of the dataframe to Weather Condition"

# In[36]:


data.head(2)


# In[42]:


data.rename(columns = {"Weather" : "Weather Condition"},inplace = True) #renamed permanently


# What is the mean "Visibility"

# In[44]:


data.head(3)


# In[45]:


data["Visibility_km"].mean()


# What is the standard deviation of "Pressure" in this data

# In[47]:


data["Press_kPa"].std()


# What is the variance of "Relative humidity" in this data

# In[49]:


data["Rel Hum_%"].var()


# Find all instances when "Snow" was recorded

# In[50]:


#value_counts()
data["Weather Condition"].value_counts()


# In[52]:


#filtering
data[data["Weather Condition"] == "Snow"]


# In[54]:


#str.contains
data[data["Weather Condition"].str.contains("Snow")].head(50)


# Find all the instances when "Wind speed is above 24" and "Visibility is 25"
# 

# In[55]:


data.head(2)


# In[65]:


data[(data["Wind Speed_km/h"]>24) & (data["Visibility_km"] == 25)]


# What is the mean value of each column aganist each "Weather Condition"

# In[67]:


data.head(2)


# In[68]:


data.groupby("Weather Condition").mean()


# What is the minimun and maximum value of each column aganist each "Weather condition"

# In[71]:


data.groupby("Weather Condition").min()


# In[72]:


data.groupby("Weather Condition").max()


# Show all the records where Weather Condition is Fog

# In[73]:


data.head(3)


# In[82]:


data[data["Weather Condition"] == "Fog"]


# Find all the instances when "Weather is Clear" or "Visibilty is above 40"

# In[85]:


data[(data["Weather Condition"] == "Clear") | (data["Visibility_km"] >40)]


# Find all instances when
# 
# A. "Weather is clear" and "Relative humidity is greater than 50"
# 
# or
# 
# B. "Visibity is above 40"

# In[92]:


data[(data["Weather Condition"]=="Clear")&(data["Rel Hum_%"] >50)|(data["Visibility_km"] > 40)]


# In[ ]:





# In[ ]:





# In[ ]:




