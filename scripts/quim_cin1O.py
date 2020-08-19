#!/bin/python

import numpy as np
from matplotlib import pyplot as plt
# A  -->  B	
# dA/dt = -ka * A

A0=0.5
ka=0.001

t_ini=0.
t_fin=1.0
dt=0.0001

t=np.linspace(t_ini,t_fin,dt)

A=np.zeros((t_fin-t_ini)/dt)

A[0]=A0
for i in range(len(A)-1):
	A[i+1]=A[i]-ka*A[i]


plt.plot(A);plt.show()

