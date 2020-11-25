#!/usr/bin/env python
# coding: utf-8

# # day 3
# 

# In[5]:


def merge(dict1,dict2):
    return(dict2.update(dict1))

d1={'a': 100, 'b': 200}
d2={'x': 300, 'y': 400}
print(merge(d1,d2))
print(d2)


# In[6]:


myDict={'a':1,'b':2,'c':3,'d':4}
print(myDict)
if 'a' in myDict:
    del myDict['a']
print(myDict)


# In[7]:


keys =['red','green','blue']
values=['#FF0000','#008000','#000FF']
colour_dictionary=dict(zip(keys,values))
print(colour_dictionary)


# In[8]:


seta = set([5, 10, 3, 15, 2, 20])
#Find the length use len()
print(len(seta))


# In[9]:


sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Original sets:")
print(sn1)
print(sn2)
print("Remove the intersection of a 2nd set from the 1st set using difference_update():")
sn1.difference_update(sn2)
print(sn1)
sn1 = {1,2,3,4,5}
sn2 = {4,5,6,7,8}
print("Remove the intersection of a 2nd set from the 1st set using -= operator:")
print(sn1-sn2)


# In[ ]:





# In[ ]:




