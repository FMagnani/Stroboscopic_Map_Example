#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 22:33:52 2020

@author: FMagnani
GitHub repo: https://github.com/FMagnani
"""

import numpy as np             # numerical library
import matplotlib.pylab as plt # plot library
import Stroboscopic as Strb

### Main script ###

orbits    = 15       # Number of orbits
size  = 10000        # Number of iterations

Dt = .1              # Time interval for numerical integration
a = 1                # x coord of equilibrium point
b = 1                # y coord of equilibrium point
e = .1               # Amplitude of the periodic perturbation
k = 10                # Period, in units 'Dt'

T = k*Dt             # Period
W = 2*np.pi/T        # Frequency
invPi = 1/np.pi

seed = 1             # For random generation of initial orbits' position
np.random.seed(seed)

xlim = (-3, 3)       # Span of x axis
ylim = (-3, 3)       # Span of y axis

# The following variables are boolean
stroboscopic = 1     # Display stroboscopic map over the complete orbit?
modular = 0          # Modulate the evolution over the period?
projection = 1       # Display projection of the stroboscopic map onto xy plane of 3D orbits?


# Parameters and grid initialization
Parameters = {'orbits':orbits, 'size':size, 'Dt':Dt, 'a':a, 'b':b, 'e':e, 
              'T':T, 'k':k, 'xlim':xlim, 'ylim':ylim}

X     = np.empty(shape=(size, orbits), dtype=float)
Y     = np.empty(shape=(size, orbits), dtype=float) 
th    = np.empty(shape=(size), dtype=float)
X[0]  = np.random.rand(orbits)
Y[0]  = np.random.rand(orbits)
th[0] = 0


# Solution
X, Y, th = Strb.Map_time(Parameters, X,Y,th, modular)


# Stroboscopic map
ind_p = tuple([np.arange(0,size,k)])
Xp = X[ind_p]
Yp = Y[ind_p]
thp = th[ind_p]

Data = { 'X':X, 'Y':Y, 'th':th, 'Xp':Xp, 'Yp':Yp, 'thp':thp }


#Plotting

# Example for a figure with two 2D plots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8,8))
Strb.Plot2D(ax1, Data, Parameters, stroboscopic)
X, Y, th = Strb.Map_theta(Parameters, X,Y,th, modular)
    
ind_p = tuple([np.arange(0,size,k)])
Data['Xp'] = X[ind_p]
Data['Yp'] = Y[ind_p]
Data['thp'] = th[ind_p]

Strb.Plot2D(ax2, Data, Parameters, stroboscopic)


# Example of a 3D figure
Strb.Plot3D(Data, Parameters, 
            stroboscopic, modular, projection)



# Example of a for cycle for 2D figures. 
# Each time is needed to apply the map again and update Parameters and Data.
fig, ax = plt.subplots(nrows=2, ncols=2)

for (e,cell) in [(0,ax[0,0]), (.1,ax[0,1]), (.5,ax[1,0]), (1,ax[1,1])]:
    Parameters['e'] = e
    
    X, Y, th = Strb.Map_theta(Parameters, X,Y,th, modular)
    
    ind_p = tuple([np.arange(0,size,k)])
    Data['Xp'] = X[ind_p]
    Data['Yp'] = Y[ind_p]
    Data['thp'] = th[ind_p]
    
    Strb.Plot2D(cell, Data, Parameters, stroboscopic)


plt.show()















