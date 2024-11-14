#!/usr/bin/env python
# coding: utf-8

# FINDING THE EVEN AND ODD NUMBERS IN THE LIST

# In[3]:


list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

for n in list:
    if (n % 2 == 0):
        print ("The given number is even number",n)
    else:
        print ("The given number is odd number",n)


# IMPORTING MODULES

# In[7]:


import numpy as np 
import pandas as pd

A = np.random.normal(25.0, 5.0, 10)
print(A)
A


# LISTS

# In[9]:


x = [1,2,3,4,5,6,7,8,9,10]
print(len(x))


# In[10]:


x[:3]


# In[11]:


x[3:]


# In[12]:


x[-2:]


# In[13]:


x[-3:]


# In[15]:


x[3:5]


# In[17]:


x.extend([11,12])
x


# In[18]:


x.append([13,14])
x


# In[19]:


x.append(15)
x


# In[21]:


y = [20,21,22]
y


# In[22]:


listoflist = [x,y]
listoflist


# In[23]:


listoflist[1]


# In[24]:


listoflist[0][12]


# In[25]:


listoflist[0][12][1]


# In[27]:


z = [5,4,3,2,1]
z.sort()
z


# In[29]:


z.sort(reverse=True)
z


# TUPLES

# LISTS ARE MUTABLE BUT TUPLES ARE IMMUTABLE

# In[30]:


x = (1,2,3)
x


# In[31]:


len(x)


# In[32]:


x[0]


# In[33]:


x[-1]


# In[34]:


y = (4,5,6)
y


# In[35]:


listoftuples = [x,y]


# In[36]:


listoftuples


# In[38]:


listoftuples[1]


# In[39]:


x


# In[42]:


(age,income) = "32,12000".split(',')
print(age)
print(income)


# DICTIONARIES

# In[45]:


captain = {}
captain["enterprise"] = "kirk"
captain["enterprise D"] = "picard"
captain["Deep Space Nine"] = "sisko"
captain["voyager"] = "janeway"

print(captain["enterprise"])
print(captain["voyager"])


# In[46]:


print(captain.get("enterprise"))


# In[47]:


print(captain.get("dummy"))


# In[48]:


for ship in captain:
    print(ship + ": " + captain[ship])


# FUNCTIONS

# In[49]:


def squareit(x):
    return x * x


# In[50]:


squareit(10)


# In[51]:


#we can pass a function as an argument 

def dosomething(f,x):
    return f(x)


# In[52]:


dosomething(squareit,5)


# In[53]:


#using lambda functions

dosomething(lambda x:x*x*x,8)


# BOOLEAN EXPRESSIONS

# In[54]:


print (1==3)


# In[55]:


print (1==1)


# In[57]:


print (True or False)


# In[60]:


print (2 == 5)


# In[61]:


if 1==1:
    print ("The expression is correct")
elif 1==2:
    print ("The expression is incorrect")
else:
    print ("Both the expression is incorrect")


# LOOPING

# In[62]:


for x in range(20):
    print(x)


# In[64]:


for x in range(10):
    if (x == 1):
        continue
    if (x > 5):
        break
    print(x)


# In[67]:


x = 0
while (x < 10):
    print(x)
    x += 1


# ACTIVITY 
# 
# Write some code that creates a list of integers, loops through each element of the list, and only prints out even numbers!

# In[73]:


a = range(20)

for n in a:
    if n % 2 == 0:
        print("The given number is an even number",n)

print("All Done")


# In[ ]:




