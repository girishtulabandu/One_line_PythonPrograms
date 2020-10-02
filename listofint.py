#!/usr/bin/env python
# coding: utf-8

# In[10]:


#shows the list only upto the input number eg.input list=3 2 3 5 5 6 7 ,input number=4 output=[3,2,3,5]
list(map(int,input("Enter the list elements:").split()[:int(input("enter the number: "))]))

