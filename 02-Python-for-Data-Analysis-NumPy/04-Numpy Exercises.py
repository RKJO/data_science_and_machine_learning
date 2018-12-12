#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# In[2]:


import numpy as np


# #### Create an array of 10 zeros 

# In[6]:


np.zeros(10)


# In[2]:





# #### Create an array of 10 ones

# In[7]:


np.ones(10)


# #### Create an array of 10 fives

# In[13]:


np.ones(10) * 5


# In[4]:





# #### Create an array of the integers from 10 to 50

# In[16]:


np.arange(10,51)


# In[5]:





# #### Create an array of all the even integers from 10 to 50

# In[18]:


np.arange(10,51,2)


# In[6]:





# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[19]:


np.arange(9).reshape(3,3)


# In[7]:





# #### Create a 3x3 identity matrix

# In[20]:


np.eye(3)


# In[8]:





# #### Use NumPy to generate a random number between 0 and 1

# In[25]:


np.random.laplace()


# In[15]:





# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[27]:


np.random.randn(25)


# In[33]:





# #### Create the following matrix:

# In[49]:


np.arange(1,101).reshape(10,10)/100


# In[56]:


np.linspace(0.01,1,100).reshape(10,10)


# In[35]:





# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[32]:


np.linspace(0,1,20)


# In[36]:





# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[33]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[34]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[2:,1:]


# In[40]:





# In[36]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[3,-1]


# In[41]:





# In[40]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[:3,1:2]


# In[42]:





# In[57]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[-1,:]


# In[46]:





# In[32]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[43]:


mat[-2:]


# ### Now do the following

# #### Get the sum of all the values in mat

# In[58]:


mat.sum()


# In[59]:


np.sum(mat)


# In[50]:





# #### Get the standard deviation of the values in mat

# In[45]:


mat.std()


# In[51]:





# #### Get the sum of all the columns in mat

# In[61]:


mat.sum(axis=0)


# In[53]:





# # Great Job!
