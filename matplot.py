# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:08:14 2023

@author: Prachi
"""

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.xlabel('x points')
plt.ylabel('y points')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

#plot 1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])

plt.subplot(1,2,1)#(one row,three column,list position)
plt.plot(x,y)

#plot 2
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()

#task1
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.xlabel('x points')
plt.ylabel('y points')
plt.show()

#task2
xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints, ypoints)
plt.xlabel('x points')
plt.ylabel('y points')
plt.show()

