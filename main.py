#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 22:33:52 2020

@author: FMagnani
GitHub repo: https://github.com/FMagnani
"""

import numpy as np             # numerical library
import matplotlib.pylab as plt # plot library
#import Stroboscopic as Strb

### Main script ###

orbits    = 15       # Number of orbits
size  = 10000        # Number of iterations

Dt = .5              # Time interval for numerical integration
a = 1                # x coord of equilibrium point
b = 1                # y coord of equilibrium point
e = .1               # Amplitude of the periodic perturbation
k = 2                # Period, in units 'Dt'

T = k*Dt             # Period
W = 2*np.pi/T        # Frequence
invPi = 1/np.pi

seed = 1             # For random generation of initial orbits' position
np.random.seed(seed)

xlim = (-5, 5)       # Span of x axis
ylim = (-5, 5)       # Span of y axis

stroboscopic = 1     # Display stroboscopic map over the complete orbit?
modular = 1          # Modulate over the period for theta?
projection = 1       # Display projection onto xy plane of 3D orbits?


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
# X, Y, th = Strb.map1(X,Y, Modular=modular)


# Stroboscopic map
ind_p = tuple([np.arange(0,size,k)])
Xp = X[ind_p]
Yp = Y[ind_p]
thp = th[ind_p]


#Plotting

Data = { 'X':X, 'Y':Y, 'th':th, 'Xp':Xp, 'Yp':Yp, 'thp':thp }

# Strb.Plot2D(Data, Parameters, Stroboscopic=stroboscopic)
# Strb.Plot3D(Data, Parameters, 
#             Stroboscopic=stroboscopic, Modular=modular, Projection=projection)
















