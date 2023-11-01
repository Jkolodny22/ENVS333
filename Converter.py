#!/usr/bin/env python
# coding: utf-8

# In[15]:


latdirection=1
latdegree=42
latminute=13
latsecond=6.49

latitudeN = latdirection * (latdegree + (latminute + latsecond / 60.) / 60.)
print(latitudeN)

latdirection=-1
latdegree=71
latminute=7
latsecond=4.43

latitudew = latdirection * (latdegree + (latminute + latsecond / 60.) / 60.)
print(latitudew)


# In[16]:


Celsius = 25

Fahrenheit = (Celsius * 9/5) + 32
print(Fahrenheit)


# In[26]:


Miles = 2
Feet = (Miles*5280)
print(Feet)


# In[27]:


Feet=2
Inches=(Feet*12)
print(Inches)


# In[43]:


Gallon=2
Liter=(Gallon*3.785411784)
print(Liter)


# In[45]:


Acre=2
Hectare=(Acre*0.4046856422)
print(Hectare)


# In[ ]:




