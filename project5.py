#!/usr/bin/env python
# coding: utf-8

# # day5

# In[5]:


num1 = input('enter a number')
num2 = input('enter a number')
sum = float(num1) + float(num2)
print('the addition of {} and {} is {}'.format(num1, num2, sum))


# In[11]:


num1 = input('enter a number')
num2 = input('enter a number')
sum = float(num1) - float(num2)
print('the substraction of {} and {} is {}'.format(num1, num2, sum))


# In[9]:


num1 = input('enter a number')
num2 = input('enter a number')
sum = float(num1) * float(num2)
print('the multiplication of {} and {} is {}'.format(num1, num2, sum))


# In[10]:


num1 = input('enter a number')
num2 = input('enter a number')
sum = float(num1) // float(num2)
print('the division of {} and {} is {}'.format(num1, num2, sum))


# In[20]:


def covid(patientname,body_Temp=98):
    print("Enter patient name",patientname)
    print("patient body temperature is", body_Temp,"degree")
covid("Pratyush")


# In[ ]:




