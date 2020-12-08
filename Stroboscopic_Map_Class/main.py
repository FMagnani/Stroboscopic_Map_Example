#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:57:13 2020

@author: FMagnani
GitHub repo: https://github.com/FMagnani
"""

import matplotlib.pyplot as plt
import system as sys

# Parameters
orbits    = 10       # Number of orbits
size  = 10000        # Number of iterations

Dt = .01              # Time interval for numerical integration
a = 1                # x coord of equilibrium point
b = 1                # y coord of equilibrium point
e = .1               # Amplitude of the periodic perturbation
k = 100              # Period, in units 'Dt'

seed = 1             # For random generation of initial orbits' position

xlim = (-3, 1.5)       # Span of x axis
ylim = (-3, 1.5)       # Span of y axis

# The following variables are boolean
stroboscopic = 1     # Display stroboscopic map over the complete orbit?
modular = 0          # Modulate the evolution over the period?
projection = 1       # Display projection of the stroboscopic map onto xy plane of 3D orbits?



# Main script

# Example 1: Two 2D plots
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8,8))

system1 = sys.system(orbits, size, Dt, e, k, seed, 
               stroboscopic, modular, projection)

system1.apply_Map_Theta()

system1.Plot2D(ax1, (-1.5,1.5), (-1.5,1.5), 0, 0)

system2 = sys.system(orbits, size, Dt, e, k, seed, 
               stroboscopic, modular, projection)

system2.apply_Map_Time()

system2.Plot2D(ax2, (-2.5,1), (-2.5,1), 0, 0)

plt.show()

# Example 2: A 3D plot

system1.Plot3D(xlim, ylim)












