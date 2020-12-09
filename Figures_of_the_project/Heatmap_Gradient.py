#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:48:21 2020

@author: FMagnani
GitHub repo: https://github.com/FMagnani
"""

import numpy as np
import matplotlib.pyplot as plt

# Plot parameters
xm, xM = 0, 3.1
ym, yM = 0, 3.1
resolution = .01

# Create grid
X, Y = np.meshgrid(np.arange(xm, xM, resolution), np.arange(ym, yM, resolution))


def Lyapunov(x,y, k1, k2, A=1, B=1):
    """
    Given the grid (x,y)  and the parameters k1, k2, a, b, this function 
    applies the Lyapunov function to each point of the grid and returns
    the grid representing this values, that can be plotted as a heatmap.
    It returns also the string of the parameters, to be used in the legend.

    Parameters
    ----------
    x : numpy.ndarray
    y : numpy.ndarray
        The couple of arrays (x,y) represents the grid onto which the Lyapunov
        function will be evaluated. 
    k1 : float
    k2 : float
    a : float, optional (default is 1) 
    b : float, optional (default is 1)
        These are the parameter of the system of which the Lyapunov function
        is computed (so the parameters of the Lyapunov function itself).

    Returns
    -------
    phi : numpy.ndarray
        This is the matrix representig the Lyapunov function. In each location
        of the matrix it is stored the value of the Lyapunov function 
        evaluated at the corrisponding location of (x,y). 'phi' can be easily 
        plot with a heatmap.
    parameters : String
        To be put in the legend of the graph.

    """
   
    phi = -(A+k1*B)*x + k1*x*x*.5 -(B+k2*A)*y + k2*y*y*.5 + x*y
    
    parameters = "$Parameters$ \n" +\
                 "$k_1$ = "+str(k1)+"   $k_2$ = "+str(k2)+"   $k_1$$k_2$ = "+str(k1*k2)
    
    return phi, parameters


# The parameters A,B are rescaled in order to match the grid used as the result of the evaluation of phi
a = 1/resolution
b = 1/resolution

# Define a figures with three plots inside
fig, (ax1,ax2,ax3) = plt.subplots(1,3)

# Compute three cases (three different parameters choices) 
phi1, pars1 = Lyapunov(X,Y, 2,2)
phi2, pars2 = Lyapunov(X,Y, 1,1)
phi3, pars3 = Lyapunov(X,Y, .5,.5)

# Plot on each graph a different evaluation of phi
# The first is saved as 'map' since then it is needed to create the colorbar
mapp = ax1.imshow(phi1, cmap='viridis', origin='lower')
ax2.imshow(phi2, cmap='viridis', origin='lower')
ax3.imshow(phi3, cmap='viridis', origin='lower')
fig.colorbar(mapp, ax=(ax1,ax2,ax3), shrink=0.5)

# Plot in each graph some level lines
levels = 10
ax1.contour(phi1, colors="white", levels=levels)
ax2.contour(phi2, colors="white", levels=levels)
ax3.contour(phi3, colors="white", levels=levels)

# Add to each graph the legend and the fixed points

size = 30 # Size of points used by the scatter plot, for representing the fixed points

ax1.text(0.03, 0-0.17, pars1, fontsize=12, transform=ax1.transAxes,
            bbox={'facecolor': 'white', 'alpha': 1})
ax1.scatter(b, a, c='cyan', alpha=1, s=size)
ax1.scatter(0, 0, c='y', alpha=1, s=2*size)
ax1.scatter(0, a + b/2, c='r', alpha=1, s=size)
ax1.scatter(b + a/2, 0, c='r',alpha=1, s=size)

ax2.text(0.03, 0-0.17, pars2, fontsize=12, transform=ax2.transAxes,
            bbox={'facecolor': 'white', 'alpha': 1})
ax2.scatter(b, a, c='cyan', alpha=1, s=size)
ax2.scatter(0, 0, c='y', alpha=1, s=2*size)
ax2.scatter(0, a + b/1, c='cyan', alpha=1, s=size)
ax2.scatter(b + a/1, 0, c='cyan',alpha=1, s=size)

# Here a whole line is represented, made up of fixed points.
N = 15
for i in range(2*N):
    ax2.scatter(i/(N*resolution), -i/(N*resolution)+2/resolution, c='cyan', alpha=1, s=.2*size)

ax3.text(0.03, 0-0.17, pars3, fontsize=12, transform=ax3.transAxes,
            bbox={'facecolor': 'white', 'alpha': 1})
ax3.scatter(b, a, c='red', alpha=1, s=size)
ax3.scatter(0, 0, c='y', alpha=1, s=2*size)
ax3.scatter(0, a + b/.5, c='cyan', alpha=1, s=size)
ax3.scatter(b + a/.5, 0, c='cyan',alpha=1, s=size)

# The scale of all the axis is removed, since it's not correct. 
ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])
ax3.set_xticks([])
ax3.set_yticks([])

# Show the graph
plt.show()























