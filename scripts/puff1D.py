#!/usr/bin/python
# -*- coding: utf-8 -*-
# Puff Guaussiano-1D

from numpy import *
from matplotlib import pyplot as plt

# Parámetros 
max_iter = 50   #iteraciones 
tini = 1        #tiempo inicial
dt= .1          #time-step
Xini=5.
M = 3.0         #Emisión
H=10.0          #altura de la fuente.
Kx=0.5          #difusividad-x
lambda1=0.00001 #tasa de decaimiento
U= 1.0          #velocidad-X del viento

# Grilla 
xmin = 0. ; xmax = 20.

x = linspace(xmin,xmax,100)

X=x; #Y=y #X,Y = meshgrid(x,y)
# Cálculo
C=0
for i in range(max_iter):
    t=tini+dt*i
    sigmaX = sqrt(2*Kx*t)
    C = M/(sqrt(2*pi)*sigmaX)*exp(-0.5*(X-(Xini+U*t))**2/(sigmaX*sigmaX) )
 
    # Plot
    if (i%10 == 0):
                plt.plot(x,C,"-o",linewidth=1.2);

