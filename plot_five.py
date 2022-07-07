import numpy as np # For mathematics, and making arrays
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 

# Arrays x, y and z for data plot visualization
x = np.arange(0, 25, 1)
y = np.arange(0, 25, 1)
# meshgrid makes a retangular grid out of two 1-D arrays. 
x, y = np.meshgrid(x, y)
z = x**2 + y**2  # x^2+y^2 
  
# surface plot for x^2 + y^2 
fig = plt.figure() # creates space for a figure to be drawn 

# Uses a 3d prjection as model is supposed to be 3D
axes = fig.gca(projection ='3d')

# Plots the three dimensional data consisting of x, y and z 
axes.plot_surface(x, y, z) 

# show command is used to visualize data plot   
plt.show() 
