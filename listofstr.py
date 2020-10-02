#!/usr/bin/env python
# coding: utf-8

# In[22]:


#prints the list of strings e.g. input list=hello how r you ,output=['hello','how','r','you']
'\n'.join(str(line) for line in (str,input("Enter the list elements:").split()))

