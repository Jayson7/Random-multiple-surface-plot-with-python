import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

def midpoint(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2
        sl += np.index_exp[:]
        return x
    # prepare some coordinates and attach rgb values to each
    r, theta, z = np.mgrid[0:1:11j, 0:np.pi*2:25j, -1:1:11j]
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    rc, thetac, zc = midpoint(r), midpoint(theta), midpoint(z)
    
    # define a wobbly torus about [0.7, *, 0]
    sphere = (rc - 0.7) ** 2 + (zc + 0.2 * np.cos(thetac)) ** 2
    
    # combine the color components 
    hsv = np.zeros ((x.shape + (3,)))
    hsv [..., 0] = thetac / (2 * np.pi)
    hsv [..., 1] = rc
    hsv [..., 2] = zc + 0.5
    colors = colors.hsv_to_rgb(hsv)
    
    #  general plotting stuff
    ax = plt.subplot(111, projection='3d')
    ax.voxels (x, y, z, colors, facecolors=colors, edgecolors=colors)
    plt.show()
    

