#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:21:55 2020

@author: FMagnani
GitHub repo: https://github.com/FMagnani
"""

import numpy as np
import matplotlib.pyplot as plt

class system:
    
    def __init__(self, orbits, size, Dt, e, k, seed, 
               stroboscopic, modular, projection, a=1, b=1):
        """
        

        Parameters
        ----------
        orbits : TYPE
            DESCRIPTION.
        size : TYPE
            DESCRIPTION.
        Dt : TYPE
            DESCRIPTION.
        e : TYPE
            DESCRIPTION.
        k : TYPE
            DESCRIPTION.
        seed : TYPE
            DESCRIPTION.
        stroboscopic : TYPE
            DESCRIPTION.
        modular : TYPE
            DESCRIPTION.
        projection : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.orbits = orbits
        self.size = size
        self.Dt = Dt
        self.e = e
        self.k = k
        self.strob = stroboscopic
        self.modular = modular
        self.proj = projection
        self.a = a
        self.b = b
        
        np.random.seed(seed)
        self.X     = np.empty(shape=(size, orbits), dtype=float)
        self.Y     = np.empty(shape=(size, orbits), dtype=float) 
        self.Z    = np.empty(shape=(size), dtype=float)
        self.X[0]  = np.random.rand(orbits)
        self.Y[0]  = np.random.rand(orbits)
        self.Z[0] = 0
        
    
    def apply_Map_Theta(self):
        """
        

        Returns
        -------
        None.

        """
    
        Dt = self.Dt
        T = self.k*Dt
        invPi = 1/np.pi
        size = self.size
        a = self.a
        b = self.b
        e = self.e
    
        # In fact, if mod = size there is no modularity at all, 
        # since the number of iterations is size itself.
        if (self.modular):
            mod = 2*np.pi
        else:
            mod = size*2*np.pi*Dt

    
        # Integration algorithm
        for i in range(size-1):            
            self.Y[i+1] = self.Y[i] + 2*np.pi*Dt*(np.exp(invPi*self.X[i]) - b*b)  
            self.X[i+1] = self.X[i] + 2*np.pi*Dt*(a*a - np.exp(invPi*self.Y[i+1])) + e*2*np.pi*Dt*np.cos(self.Z[i])
            self.Z[i+1] = np.mod(self.Z[i] + 2*np.pi*Dt/T, mod)    
           
        # Stroboscopic map
        ind_p = tuple([np.arange(0,self.size,self.k)])
        self.Xp = self.X[ind_p]
        self.Yp = self.Y[ind_p]
        self.Zp = self.Z[ind_p]

           
    def apply_Map_Time(self):
        """
        

        Returns
        -------
        None.

        """
     
        Dt = self.Dt
        T = self.k*Dt
        size = self.size
        a = self.a
        b = self.b
        e = self.e
        W = 2*np.pi/T

        
        # In fact, if mod = size there is no modularity at all, 
        # since the number of iterations is size itself.
        if (self.modular):
            mod = self.k
        else:
            mod = size
       
        
        # Integration algorithm
        for i in range(size-1):            
            self.Y[i+1] = self.Y[i] + Dt*(np.exp(2*self.X[i]) - b*b)  
            self.X[i+1] = self.X[i] + Dt*(a*a - np.exp(2*self.Y[i+1])) + e*Dt*np.cos(W*self.Z[i])
            self.Z[i+1] = np.mod(self.Z[i] + Dt, mod*Dt)            
    
        # Stroboscopic map
        ind_p = tuple([np.arange(0,self.size,self.k)])
        self.Xp = self.X[ind_p]
        self.Yp = self.Y[ind_p]
        self.Zp = self.Z[ind_p]

    
    # def getData(self):
    #     """
        

    #     Returns
    #     -------
    #     TYPE
    #         DESCRIPTION.
    #     TYPE
    #         DESCRIPTION.
    #     TYPE
    #         DESCRIPTION.
    #     TYPE
    #         DESCRIPTION.
    #     TYPE
    #         DESCRIPTION.
    #     TYPE
    #         DESCRIPTION.

    #     """
        
    #     return self.X, self.Y, self.Z, self.Xp, self.Yp, self.Zp
    
    
    def Plot2D(self, ax, xlim, ylim, legend_x, legend_y, font=15):
        """
        

        Parameters
        ----------
        ax : TYPE
            DESCRIPTION.
        xlim : TYPE
            DESCRIPTION.
        ylim : TYPE
            DESCRIPTION.
        font : TYPE, optional
            DESCRIPTION. The default is 15.

        Returns
        -------
        None.

        """
        
        # Plot orbits
        ax.plot(self.X, self.Y, 'k,')
        
        # Plot stroboscopic map
        if (self.strob):
            ax.plot(self.Xp, self.Yp, 'ro', markersize=1)
        
        # Setting axis limits
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)

        # Legend
        ax.set_xlabel("x", fontsize=font)
        ax.set_ylabel("y", fontsize=font)

        parameters = "$Parameters$"+'\n'+\
               "Orbits: "+str(self.orbits)+\
               "    Iterations: "+str(self.size)+'\n'+\
               "$\Delta$t: "+str(self.Dt)+\
               "     $\epsilon$: "+str(self.e)+\
               "     $T$: "+str(self.k)+" $\Delta$t"+\
               "     $\lambda$: "+str(self.k)
               
        ax.text(xlim[0]+legend_x, ylim[0]+legend_y, parameters, fontsize=12,
                bbox={'facecolor': 'white', 'alpha': 1})
    
        
    def Plot3D(self, xlim, ylim, font=15):
        
        # 3D figure initialization
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        zmax = np.max(self.Z)

        # Axis limits
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        ax.set_zlim(0, zmax)

        # Axis labels
        ax.set_xlabel("x", fontsize=font)
        ax.set_ylabel("y", fontsize=font)
        ax.set_zlabel("\u03B8", fontsize=font)

        # Plotting
        ax.plot(self.X, self.Y, self.Z, 'k,', zdir = 'z')
    
        if (self.strob):
            ax.plot(self.Xp,self.Yp,self.Zp,'ro', zdir = 'z', markersize=1.5)

        if (self.proj):
            ax.plot(self.Xp, self.Yp, 'ro', zdir='z', markersize=1.5)

        plt.show()
    
    
    
    
    
    
    
    
    
    
    