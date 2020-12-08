#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:04:49 2020

@author: FMagnani
GitHub repo: https://github.com/FMagnani
"""

import numpy as np             # numerical library
import matplotlib.pylab as plt # plot library

invPi = 1/np.pi

def Map_theta(Parameters, X, Y, th, Modular):
    
    """
    """
    a = Parameters['a']
    b = Parameters['b']
    size = Parameters['size']
    Dt = Parameters['Dt']
    T = Parameters['T']
    e = Parameters['e']

    # In fact, if mod = size there is no modularity at all, 
    # since the number of iterations is size itself.
    if (Modular):
        mod = 2*np.pi
    else:
        mod = size*2*np.pi*Dt
    
    # Integration algorithm
    for i in range(size-1):            
        Y[i+1] = Y[i] + 2*np.pi*Dt*(np.exp(invPi*X[i]) - b*b)  
        X[i+1] = X[i] + 2*np.pi*Dt*(a*a - np.exp(invPi*Y[i+1])) + e*2*np.pi*Dt*np.cos(th[i])
        th[i+1] = np.mod(th[i] + 2*np.pi*Dt/T, mod)
        
    return X, Y, th

def Map_time(Parameters, X, Y, t, Modular):
    
    """
    """
    a = Parameters['a']
    b = Parameters['b']
    size = Parameters['size']
    Dt = Parameters['Dt']
    T = Parameters['T']
    e = Parameters['e']
    k = Parameters['k']
    W = 2*np.pi/T

    # In fact, if mod = size there is no modularity at all, 
    # since the number of iterations is size itself
    if (Modular):
        mod = k
    else:
        mod = size
    
    # Integration algorithm
    for i in range(size-1):            
        Y[i+1] = Y[i] + Dt*(np.exp(2*X[i]) - b*b)  
        X[i+1] = X[i] + Dt*(a*a - np.exp(2*Y[i+1])) + e*Dt*np.cos(W*t[i])
        t[i+1] = np.mod(t[i] + Dt, mod*Dt)
        
    return X, Y, t


def Plot2D(ax, Data, Pars, Stroboscopic):
  """    
  """
  X = Data['X']
  Y = Data['Y']
  Xp = Data['Xp']
  Yp = Data['Yp']
  xlim = Pars['xlim']
  ylim = Pars['ylim']
      
  # Plotting
  ax.plot(X, Y, 'k,')
  
  if (Stroboscopic):
      ax.plot(Xp, Yp, 'ro', markersize=1)
  
  # Axis limits
  ax.set_xlim(xlim)
  ax.set_ylim(ylim)
  
  # Legend
  fnt =15
  ax.set_xlabel("x", fontsize=fnt)
  ax.set_ylabel("y", fontsize=fnt)

  parameters = "$Parameters$"+'\n'+\
               "Orbits: "+str(Pars['orbits'])+\
               "    Iterations: "+str(Pars['size'])+'\n'+\
               "$\Delta$t: "+str(Pars['Dt'])+\
               "     $\epsilon$: "+str(Pars['e'])+\
               "     $T$: "+str(Pars['k'])+" $\Delta$t"+\
               "     $\lambda$: "+str(Pars['k'])
               
  ax.text(xlim[0], ylim[0], parameters, fontsize=12,
        bbox={'facecolor': 'white', 'alpha': 1})



def Plot3D(Data, Pars, Stroboscopic, Modular, Projection):
    """
    """
    X = Data['X']
    Y = Data['Y']
    th = Data['th']
    Xp = Data['Xp']
    Yp = Data['Yp']
    thp = Data['thp']
    xlim = Pars['xlim']
    ylim = Pars['ylim']
       
    # 3D figure initialization
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    zmax = np.max(Data['th'])

    # Axis limits
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(0, zmax)

    # Axis labels
    fnt =15
    ax.set_xlabel("x", fontsize=fnt)
    ax.set_ylabel("y", fontsize=fnt)
    ax.set_zlabel("\u03B8", fontsize=fnt)

    # Plotting
    ax.plot(X, Y, th, 'k,', zdir = 'z')
    
    if (Stroboscopic):
        ax.plot(Xp,Yp,thp,'ro', zdir = 'z', markersize=1.5)

    if (Projection):
        ax.plot(Xp, Yp, 'ro', zdir='z', markersize=1.5)













