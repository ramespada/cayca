# -*- coding: utf-8 -*-
"""
Created on Wed May  2 16:40:07 2018
@author: ram
"""
import os
#os.chdir("/home/ram/Desktop/puff/")

from matplotlib import pyplot as plt
from numpy import *
#from math import *

#params
maxiter=70

dt=.5      #Time step
Kx=Ky=Kz=.25
M=1.       #Masa en el puff

Xi=-20      #X-coord inicial
Yi=-10      #Y-coord inicial
Zi=0.05      #Alt inicial
H=5.       #Altura efectiva
lambda1=0.001
#grid
x=linspace(-50,50,1000);y=linspace(-50,50,1000)
Xr,Yr=meshgrid(x,y)

#traj
def traj(t):
    X=10.*cos(t*0.1)+Xi
    Y=t*1.5 + Yi
    Z=sqrt(sqrt(t))*0.1+Zi
    return(X,Y,Z)
    
#solve puff
def C(t):
    
    Cx=exp(-0.5* ((X-Xr)/(sigmaX))**2 )/(sigmaX)
    Cy=exp(-0.5* ((Y-Yr)/(sigmaY))**2 )/(sigmaY)
    Cz=1.#(exp(-0.5*((Z-H)/sigmaZ)**2) + exp(-0.5*((Z+H)/sigmaZ)**2) ) / (sigmaZ) 
    
    return( M*Cx*Cy*Cz+exp(-lambda1*t))

#integr
t=1.
CC=0.
Xf,Yf,Zf=traj(dt*maxiter)
#DELTA_S1=sqrt(Xf-Xi + Yf-Yi + Zf-Zi)
for i in range(maxiter):

    t+=dt
    
    sigmaX=sqrt(2*pi*Kx*t)
    sigmaY=sqrt(2*pi*Ky*t)
    sigmaZ=sqrt(2*pi*Kz*t)

    X,Y,Z=traj(t)    
    
    dx= X-traj(t-dt)[0]
    dy= Y-traj(t-dt)[1]
    
    #ds=sqrt(dx*dx + dy*dy)
    #DELTA_S2=sqrt(X-Xi + Y-Yi + Z-Zi)

    CC+= (C(t)+C(t-dt))*0.5*dt /(maxiter*dt)
    #CC= CC/DELTA_S2/DELTA_S1*0.5#(1- (DELTA_S2/DELTA_S1))
    print(sum(CC))
    if(i%10==0):
        levs=linspace(0,0.01,25)
        plt.clf()
        plt.contourf(Xr,Yr,CC)#,levels=levs)
        #plt.show()
        plt.savefig('puff_ram.'+str(i)+'.png')

#plt.clf()
#plt.contourf(Xr,Yr,CC)
#plt.show()
#plt.savefig('puff.'+str(i)+'.png')

t=linspace(1,dt*maxiter,maxiter)
xx,yy,zz=traj(t)
plt.clf()
plt.plot(xx,yy)
