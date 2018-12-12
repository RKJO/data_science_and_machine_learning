#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../../Pierian_Data_Logo.png' /></a>
# ___

# # SF Salaries Exercise 
# 
# Welcome to a quick exercise for you to practice your pandas skills! We will be using the [SF Salaries Dataset](https://www.kaggle.com/kaggle/sf-salaries) from Kaggle! Just follow along and complete the tasks outlined in bold below. The tasks will get harder and harder as you go along.

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[3]:


sal = pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[8]:


sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[9]:


sal.info()


# In[9]:





# **What is the average BasePay ?**

# In[10]:


sal['BasePay'].mean()


# In[10]:





# ** What is the highest amount of OvertimePay in the dataset ? **

# In[11]:


sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[20]:


sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']  


# In[12]:





# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[27]:


JP = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']


# In[13]:





# ** What is the name of highest paid person (including benefits)?**

# In[29]:


sal[sal['TotalPayBenefits']==sal['TotalPayBenefits'].max()]['EmployeeName']


# In[14]:





# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[31]:


sal[sal['TotalPay']==sal['TotalPay'].min()]['EmployeeName']


# In[15]:





# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[35]:


sal.groupby('Year').mean()['BasePay']


# In[16]:





# ** How many unique job titles are there? **

# In[40]:


sal['JobTitle'].nunique()


# In[17]:





# ** What are the top 5 most common jobs? **

# In[51]:


sal['JobTitle'].value_counts().head(5)


# In[18]:





# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[62]:


sum(sal[sal['Year']==2013]['JobTitle'].value_counts()==1)


# In[19]:





# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# ** My solution =)

# In[99]:


count=0
for job in sal['JobTitle']:
    if 'chief' in job.lower():
         count+=1
            
print(count)


# In[91]:


def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False


# In[92]:


sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[96]:


sal['title_len'] = sal['JobTitle'].apply(len)


# In[97]:


sal[['title_len','TotalPayBenefits']].corr() # No correlation.


# # Great Job!
