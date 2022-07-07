# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Creating dataset
x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )

# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')

# Creating color map
my_cmap = plt.get_cmap('hot')

# Creating plot
surf = ax.plot_surface(x, y, z,
          rstride = 8,
          cstride = 8,
          alpha = 0.8,
          cmap = my_cmap)
cset = ax.contourf(x, y, z,
        zdir ='z',
        offset = np.min(z),
        cmap = my_cmap)
cset = ax.contourf(x, y, z,
        zdir ='x',
        offset =-5,
        cmap = my_cmap)
cset = ax.contourf(x, y, z,
        zdir ='y',
        offset = 5,
        cmap = my_cmap)
fig.colorbar(surf, ax = ax,
      shrink = 0.5,
      aspect = 5)

# Adding labels
ax.set_xlabel('X-axis')
ax.set_xlim(-5, 5)
ax.set_ylabel('Y-axis')
ax.set_ylim(-5, 5)
ax.set_zlabel('Z-axis')
ax.set_zlim(np.min(z), np.max(z))
ax.set_title('3D surface having 2D contour plot projections')

# show plot
plt.show()
