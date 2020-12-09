#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 15:30:17 2020

@author: FMagnani
GitHub repo: https://github.com/FMagnani
"""

import matplotlib.pyplot as plt
import numpy as np

# Parameters of the flow
a = 1 
b = 1 


# Lotka Volterra Predator Prey classical coordinates
def LV_PP_class():
    """
    Creates a grid of points (X,Y) and an associated flow (U,V). The flow is 
    the Lotka Volterra Predator Prey system in classical coordinates. 
    
    Returns
    -------
    X : numpy.ndarray
        X values of the grid.
    Y : numpy.ndarray
        Y values of the grid.    
    U : numpy.ndarray
        X component of the resolved flow, ready to be plot together with V.
    V : numpy.ndarray
        Y component of the resolved flow, ready to be plot together with U.
    xm : float, x axis lower limit.
    xM : float, x axis upper limit. 
    ym : float, y axis lower limit.
    yM : float, y axis upper limit.

    """
    xm = 0
    xM = 3
    ym = 0
    yM = 3
    
    X, Y = np.meshgrid(np.arange(xm, xM+1, .1), np.arange(ym, yM+1, .1))
    
    U = X*(a-Y)
    V = Y*(X-b)
    
    return (X, Y, U, V, xm,xM,ym,yM)

# Lotka Volterra Predator Prey canonical coordinates
def LV_PP_canon():   
    """
    Creates a grid of points (X,Y) and an associated flow (U,V). The flow is 
    the Lotka Volterra Predator Prey system in canonical coordinates. 
    
    Returns
    -------
    X : numpy.ndarray
        X values of the grid.
    Y : numpy.ndarray
        Y values of the grid.    
    U : numpy.ndarray
        X component of the resolved flow, ready to be plot together with V.
    V : numpy.ndarray
        Y component of the resolved flow, ready to be plot together with U.
    xm : float, x axis lower limit.
    xM : float, x axis upper limit. 
    ym : float, y axis lower limit.
    yM : float, y axis upper limit.

    """
    xm = -3
    xM = 2.5
    ym = -3
    yM = 2.5
    
    X, Y = np.meshgrid(np.arange(xm-1, xM+1, .15), np.arange(ym-1, yM+1, .15))
    
    U = (a-np.exp(Y))
    V = (np.exp(X)-b)
    
    return (X, Y, U, V, xm,xM,ym,yM)

# Lotka Volterra Competing Preys 
def LV_Competing(k1, k2):
    """
    Creates a grid of points (X,Y) and an associated flow (U,V). The flow is 
    the Lotka Volterra Competing Preys system with parameters k1 and k2. 
   
    Parameters
    ----------
    k1 : float
    k2 : float

    Returns
    -------
    X : numpy.ndarray
        X values of the grid.
    Y : numpy.ndarray
        Y values of the grid.    
    U : numpy.ndarray
        X component of the resolved flow, ready to be plot together with V.
    V : numpy.ndarray
        Y component of the resolved flow, ready to be plot together with U.
    
    xm : float, x axis lower limit.
    xM : float, x axis upper limit. 
    ym : float, y axis lower limit.
    yM : float, y axis upper limit.
    
    parameters : string
        The string to be shown in the legend of the plot.

    """
    
    xm = 0
    xM = 3.1
    ym = 0
    yM = 3.1
    
    X, Y = np.meshgrid(np.arange(xm-1, xM+1, .15), np.arange(ym-1, yM+1, .15))
    
    U = X*((a-Y) - k1*(X-b))
    V = Y*((b-X) - k2*(Y-a))

    
    parameters = "$Parameters$ \na=1\nb=1\n" +\
                 "$k_1$ = "+str(k1)+" \n$k_2$ = "+str(k2)+"\n$k_1$$k_2$ = "+str(k1*k2)

    return (X, Y, U, V, xm,xM,ym,yM, parameters)

# Setting common to every plot
def common_setting(ax):
    """
    Set the ticks and the axis limits of the given graph.

    Parameters
    ----------
    ax : matplotlib.axes

    """
    ax.xaxis.set_ticks(np.arange(xm,xM,.5))
    ax.yaxis.set_ticks(np.arange(ym,yM,.5))
    ax.axis([xm, xM, ym, yM])
    ax.set_aspect('equal')



# -------------------------------------------------- #

### FIGURE 1.1   Lotka Volterra Predator Prey Flow ###

# Define a figure with 2 plots inside
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

# Initialize the data using the LV Predator Prey flow in classical coordinates
X,Y,U,V, xm,xM,ym,yM = LV_PP_class()

# Plot on the first graph
common_setting(ax1)
color_array = np.log(V**2 + U**2)
strm1 = ax1.streamplot(X, Y, U, V, color=color_array, linewidth=1.5, 
                         cmap='viridis', density=[2.5,2.5])

# Add legend and title
pars = "$Parameters$ \n\u03B1=1\n\u03B2=1\n"
ax1.text(1-0.3, 1-0.2, pars, fontsize=12, transform=ax1.transAxes,
            bbox={'facecolor': 'white', 'alpha': 1})
ax1.set_title("Classical coordinates")

# Initialize the data using the LV Predator Prey flow in canonical coordinates
X,Y,U,V, xm,xM,ym,yM = LV_PP_canon()

# Plot on the second graph
common_setting(ax2)
color_array = np.log(V**2 + U**2)
strm2 = ax2.streamplot(X, Y, U, V, color=color_array, linewidth=1.5, 
                         cmap='viridis', density=[2.5,2.5])

# Add legend and title
ax2.text(1-0.3, 1-0.2, pars, fontsize=12, transform=ax2.transAxes,
            bbox={'facecolor': 'white', 'alpha': 1})
ax2.set_title("Hamiltonian coordinates")

# Show the figure 
plt.show()



# ---------------------------------------------------- #

### FIGURE 1.2   Competing Preys Flow ###

# We will overwrite both the data and the plots, since they have been already shown

# Define a figure with 2 plots inside
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

# Inizialize all the data using the Lotka Volterra Competing Preys flow
# Parameters = 2,2
X,Y,U,V, xm,xM,ym,yM, pars = LV_Competing(2,2)

# Plot on the first graph
common_setting(ax1)
color_array = np.log(V**2 + U**2)
strm1 = ax1.streamplot(X, Y, U, V, color=color_array, linewidth=1.5, 
                         cmap='viridis', density=[2.5,2.5])

# Add legend
ax1.text(1-0.3, 1-0.3, pars, fontsize=12, transform=ax1.transAxes,
            bbox={'facecolor': 'white', 'alpha': 1})

# Manually add equilibrium points
size = 100
ax1.scatter(b, a, c='b', alpha=1, s=size)
ax1.scatter(0, 0, c='y', alpha=1, s=2*size)
ax1.scatter(0, a + b/2, c='r', alpha=1, s=size)
ax1.scatter(b + a/2, 0, c='r',alpha=1, s=size)

# Now solve for parameters = 0.5, 0.5
X,Y,U,V, xm,xM,ym,yM, pars = LV_Competing(.5,.5)

# Plot on the second graph of the figure
common_setting(ax2)
color_array = np.log(V**2 + U**2)
strm2 = ax2.streamplot(X, Y, U, V, color=color_array, linewidth=1.5, 
                         cmap='viridis', density=[2.5,2.5])

# Add legend
ax2.text(1-0.3, 1-0.3, pars, fontsize=12, transform=ax2.transAxes,
            bbox={'facecolor': 'white', 'alpha': 1})

# Manually add equilibrium points
size = 100
ax2.scatter(b, a, c='r', alpha=1, s=size)
ax2.scatter(0, 0, c='y', alpha=1, s=2*size)
ax2.scatter(0, a + b/.5, c='b', alpha=1, s=size)
ax2.scatter(b + a/.5, 0, c='b',alpha=1, s=size)

# Add colorbar
fig.colorbar(strm1.lines, ax=(ax1,ax2), shrink=0.7)

# Show the figure
plt.show()







