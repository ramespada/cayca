#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#### Pluma Guaussiana
#

from numpy import *
from matplotlib import pyplot as plt

## Parámetros
Q = 1.0      #Emisión
H=5.0        #altura de la fuente.
Kx=0.2       #difusividad-x
Ky=0.5       #difusividad-y
Kz=1.0       #difusividad-z
lambda1=0.0001  #tasa de decaimiento
U= .75       #velocidad del viento
## Grilla 
xmin = 0.	  ; xmax = 100.
ymin = -50. ; ymax = 50.         
x = linspace(xmin,xmax,1000)
y = linspace(ymin,ymax,1000)
z = 0.0
X,Y = meshgrid(x,y)
## Cálculo
sigmaX = sqrt(2*Kx*X/U)
sigmaY = sqrt(2*Ky*X/U)
sigmaZ = sqrt(2*Kz*X/U)

C=Q/(sqrt(2*pi)*sigmaY*sigmaZ)* \
    #exp(-0.5*(X/sigmaX)**2 )/(sigmaX)* \
    exp(-0.5*(Y/sigmaY)**2 ) * \
    (exp(-0.5*((z-H)/sigmaZ)**2) + exp(-0.5*((z+H)/sigmaZ)**2))* \
    exp(-lambda1*X/U)

## Plot
plt.clf()
plt.imshow(C, extent=(xmin,xmax,ymin,ymax))
plt.xlabel('X'); plt.ylabel('Y'); plt.title('Pluma Gaussiana')
plt.colorbar()
plt.savefig('Pluma_Gaussiana.png')
