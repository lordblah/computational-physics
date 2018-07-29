
# coding: utf-8

# In[32]:


#PLOT SINE AND COSINE OVER THE RANGE{-PI,PI}
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-pi, pi, pi/100)
plt.plot(x, sin(x), 'b-', label='sine')
plt.plot(x, cos(x), 'g--', label='cosine')
plt.xlabel('x vaule')
plt.ylabel('trig function value')
plt.xlim(-pi, pi)
plt.ylim(-1,1)
plt.legend(loc='upper left')
plt.show()


# In[20]:





# In[14]:


plt.plot(x, sin(x), 'b-', label='sine')

