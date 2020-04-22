#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#### Puff Guaussiano
#

from numpy import *
from matplotlib import pyplot as plt

## Parámetros 

tfin = 5	     #iteraciones 
tini = 0.1	     #tiempo inicial
dt= .2		#time-step

M = 3.0         #Emisión

H=10.0          #altura de la fuente.

Kx=0.5       #difusividad-x
Ky=0.5       #difusividad-y
Kz=0.5       #difusividad-z

lambda1=0.00001  #tasa de decaimiento

U= 1.5     #velocidad-X del viento
V= 2.		#velocidad-Y del viento

## Grilla 
xmin = -10. ; xmax = 10.
ymin = -10. ; ymax = 10.         

x = linspace(xmin,xmax,500)
y = linspace(ymin,ymax,500)
z = 1.0

X,Y = meshgrid(x,y)

## Cálculo

for i in range(int((tfin-tini)/dt)):
	t=tini+dt*i

	sigmaX = sqrt(2*Kx*t)
	sigmaY = sqrt(2*Ky*t)
	sigmaZ = sqrt(2*Kz*t)

	C = M/(sqrt(2*pi)*sigmaX*sigmaY*sigmaZ)*\
	    exp(-0.5*(X-(U*t))**2/(sigmaX*sigmaX) ) *\
	    exp(-0.5*(Y-(V*t))**2/(sigmaY*sigmaY) ) *\
	    (exp(-0.5*((z-H)/sigmaZ)**2) + exp(-0.5*((z+H)/sigmaZ)**2) )*\
	    exp(-lambda1*t)

	## Plot
	plt.clf()
	plt.imshow(C, extent=(xmin,xmax,ymin,ymax))#,vmin=1e-6,vmax=1e-3
	plt.xlabel('X'); plt.ylabel('Y'); plt.title('Puff Gaussiano')
	plt.colorbar()
	plt.savefig('PuffGauss_'+str(i)+'.png')
