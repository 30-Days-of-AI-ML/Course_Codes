import matplotlib.pyplot as plt # plt is nothing but a variable
import numpy as np #deals with mathematical linear algebra
import pandas as pd # deals with data frames
#%matplotlib inline #magic command 

x1= np.linspace(0, 10 , 100)
fig = plt.figure() #inbuild func
plt.plot(x1 , np.sin(x1) , '-')
plt.plot(x1 , np.cos(x1) , '--')

plt.figure()
plt.subplot(10, 10 ,10)
plt.subplot(2, 2 ,2) #row coloumn pannel no
plt.plot(x1 , np.sin(x1))

x3 = range(6)
plt.plot(x3 , [xi**2 for xi in x3])
plt.show()

x4 = range(1, 5 )
plt.plot(x4 , [xi**1.5 for xi in x4])

data2 = [50. , 25. , 50. , 20.]
plt.barh(range(len(data2)) , data2)
plt.show()
