#!/usr/bin/env python
# coding: utf-8

# # day4

# In[3]:


list1 = [1, 2, 3, 4, 5]
list1.insert(4,10)
print(list1)
list2 = ['a','b','c','d','e']
list2.insert(0, 'z')
print(list2)


# In[5]:


list2 = ['a','b','c','d']
list2.remove('a')
print(list2)


# In[7]:


a=[45, 76, 23, 9, 25]
a.sort()
ln = a[-1]
print("Largest element is: ", ln)


# In[8]:


list1 = [34, 57, 21, 60, 33]
list1.sort()
print("Smallest element is: ", *list1[:1])


# In[7]:



def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


    
tuples = ('e','t','g','t','m','v','w')
Reverse(tuples)


# In[8]:


import itertools
tuple = [(1, 2), (3, 4),(5, 6)]
out = list(itertools.chain(*tuple))
print(out)

