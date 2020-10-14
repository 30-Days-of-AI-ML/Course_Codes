# 3d plotting 
# Surface Plot 
# Countour Plot
# Wirframes
# Surface Triangulation 
# We need a support Library to do 3D plotting in Matplotlib : 
# MPL Tool Kit

from mpl_toolkits import mplot3d


# In[2]:


import numpy as np 
import matplotlib.pyplot as plt 
fig = plt.figure()
ax = plt.axes(projection='3d') #Represented Space


# In[5]:


# Represent a spiral line 
# Growth Curve , Or Medical image plotting 

ax = plt.axes(projection='3d')

#data for 3d
zline = np.linspace(0 , 15 , 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline , yline , zline , 'gray')

#plotting little data on the space 
zdata = 15 * np.random.random(100) #constant
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata , ydata , zdata , c= zdata , cmap='Greens');


# In[6]:


# 3D Contour plot 
# Required in Image Pixel Analyis , SDG - Projects 
# sin(sqrt((x^2 + y^2))
#This plots use Mesh architechture hence meshgrid()

def f(x,y): 
    return np.sin(np.sqrt(x**2 + y**2))

x = np.linspace(-6, 6 , 30)
y=  np.linspace(-6, 6 , 30)

x,y =np.meshgrid(x , y)
z= f(x,y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x,y,z , 50 , cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


# In[9]:


#Wireframes 
#Used for dealing with same above additional sales dataets
fig = plt.figure()
ax= plt.axes(projection='3d')
ax.plot_wireframe(x,y,z, color='black')


# In[10]:


#Surface Plot 
# Is dealing with Satellite imageries and Disaster datasets
ax = plt.axes(projection='3d')
ax.plot_surface(x,y,z, rstride=1 , cstride=1 , cmap='viridis' , edgecolor='none')
