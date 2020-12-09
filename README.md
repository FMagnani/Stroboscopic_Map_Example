# Stroboscopic_Map_Example

In this repository the code developed for a university course is stored. The pdf presentation of the project is present as a reference.  
The code has been used in order to plot dynamical flows, gradient maps, or to compute and plot the stroboscopic map of a simple system (both in 3D and 2D). 

## Stroboscopic Map - brief introduction
Let's consider the following system:

![equation1](<https://latex.codecogs.com/gif.latex?\dot{x}=x(a^2&space;-&space;y^2)&plus;x\epsilon&space;\cos{\omega&space;t}>)  
![equation1](<https://latex.codecogs.com/gif.latex?\dot{y}=y(x^2&space;-&space;b^2)>)

that is explicitly dependent on time. We can recover an autonomous description at the cost of increasing the dimensionality by one, defining a new variable ![equation1](<https://latex.codecogs.com/gif.latex?\theta&space;(t)=\omega&space;t>). The system has now the form  

![equation1](<https://latex.codecogs.com/gif.latex?\dot{x}=x(a^2&space;-&space;y^2)+x\epsilon&space;\cos{\theta}>)  
![equation1](<https://latex.codecogs.com/gif.latex?\dot{y}=y(x^2&space;-&space;b^2)>)  
![equation1](<https://latex.codecogs.com/gif.latex?\dot{\theta}=\omega>)

Some further transformations are useful. Noting that for ![equation1](<https://latex.codecogs.com/gif.latex?\epsilon=0>) the system is Hamiltonian, we exploit the coordinate change ![equation1](<https://latex.codecogs.com/gif.latex?x\mapsto&space;log(x)>), ![equation1](<https://latex.codecogs.com/gif.latex?y\mapsto&space;log(y)>) and we then build two different integrators.  
For the first we rescale the spatial coordinates as
![equation1](<https://latex.codecogs.com/gif.latex?(x,y)\mapsto&space;\frac{(x,y)}{2\pi}>)  
in order to have as a final form for the system:  

![equation1](<https://latex.codecogs.com/gif.latex?\frac{\dot{x}}{2\pi}=(a^2-e^{y/\pi})+\epsilon&space;\cos{\theta}>)  
![equation1](<https://latex.codecogs.com/gif.latex?\frac{\dot{y}}{2\pi}=(e^{x/\pi}-b^2)>)  
![equation1](<https://latex.codecogs.com/gif.latex?\dot{\theta}=\omega>)  

from which the following map is derived:  

![equation1](<https://latex.codecogs.com/gif.latex?x_{n+1}=x_n&space;+2\pi&space;\Delta&space;t(a^2-e^{y_{n+1}/\pi})+\epsilon&space;2\pi&space;\Delta&space;t \cos{\theta_{n}}>)  
![equation1](<https://latex.codecogs.com/gif.latex?y_{n+1}=y_n&space;+2\pi&space;\Delta&space;t(e^{x_n/\pi}-b^2)>)  
![equation1](<https://latex.codecogs.com/gif.latex?\theta_{n+1}=\theta_n&space;+\Delta&space;t&space;\omega=\theta_n&space;+2\pi&space;\frac{\Delta&space;t}{T}>)  

We refer to this integrator as "Map_theta" in the code, since it's defined in the (x,y,theta) space.  
A different map can be obtained if we don't make the ![equation1](<https://latex.codecogs.com/gif.latex?\theta&space;(t)=\omega&space;t>) transformation, neither the rescaling of the spatial coordinates, the following:  

![equation1](<https://latex.codecogs.com/gif.latex?x_{n+1}=x_n&space;+&space;\Delta&space;t(a^2-e^{2y_{n+1}})+\epsilon&space;\Delta&space;t&space;\cos{\omega&space;t_{n}}>)  
![equation1](<https://latex.codecogs.com/gif.latex?y_{n+1}=y_n&space;+&space;\Delta&space;t(e^{2x_n}-b^2)>)  
![equation1](<https://latex.codecogs.com/gif.latex?t_{n+1}=t_n&space;+\Delta&space;t>)  

that's called "Map_time" in the code, since it's defined in the (x,y,t) space.  
  
The stroboscopic method, in the 3 dimensional framework, consist in sampling the trajectories at intervals equal to the period of the perturbation. The stroboscopic map is the projection of such a sampling onto the xy plane, and this process reduces in fact the dimensionality of the problem by one. The period T is different for the two maps, since it must be computed in terms of the time or of the angle. In any case, setting the period as an integer multiple of the integration time interval, i.e. ![equation1](<https://latex.codecogs.com/gif.latex?T=k\Delta&space;t>), the stroboscopic map is just a subset of the complete map, specifically is the subsequence in which we take one point every k.

## Software usage
Three directories are present.  
In "Stroboscopic_Map_Script" there is the implementation for the stroboscopic map code, to be used as a script.  
In "Stroboscopic_Map_Class" the same performance is given in Object Oriented version.  
In "Figures_of_the_project" there are the scripts used to plot the dynamical flows and the gradient maps shown in the relation.

Further informations are given inside each subdirectory.

## Warning
I did this code for my personal usage in a project for a university course. The script implementation is a bit messy since I realized it very fast. I personally prefer the class implementation.
