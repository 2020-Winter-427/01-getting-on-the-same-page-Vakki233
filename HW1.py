#!/usr/bin/env python
# coding: utf-8

# In[73]:


#enable the use of matplotlib
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

#create normal and exponential data points
y_norm = np.random.normal(0, 1, 1000)
x_norm = np.random.normal(0, 1, 1000)
y_exp = np.random.exponential(1, 1000)
x_exp = np.random.exponential(1, 1000)

#plot normal distribution histogram and scatter plot
plt.hist(y_norm,bins=100)
plt.title("Normal Distribution")
plt.show()
plt.scatter(x_norm,y_norm,c='b',s=2)
plt.title("Normal Distribution Scatter Plot")
plt.show()
#plot exponential distribution histogram and scatter plot
plt.hist(y_exp,bins=100)
plt.title("Exponential Distribution")
plt.show()
plt.scatter(x_exp,y_exp,c='b',s=2)
plt.title("Exponential Distribution Scatter Plot")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




