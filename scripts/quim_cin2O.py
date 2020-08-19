#!/bin/python

import numpy as np
from matplotlib import pyplot as plt
# A + B  -->  C
# dA/dt = -k0 * [A]*[B]
# dB/dt = -k0 * [A]*[B]
A0=0.5
B0=1.2
C0=0.1
k0=0.001

t_ini=0.
t_fin=1.0
dt=0.0001

t=np.linspace(t_ini,t_fin,dt)

A=np.zeros((t_fin-t_ini)/dt)
B=np.zeros((t_fin-t_ini)/dt)
C=np.zeros((t_fin-t_ini)/dt)

A[0]=A0
B[0]=B0
C[0]=C0
for i in range(len(A)-1):
	A[i+1]=A[i]-k0*A[i]*B[i]
	B[i+1]=B[i]-k0*A[i]*B[i]
	C[i+1]=C[i]+k0*A[i]*B[i]
	

plt.plot(A);plt.plot(B);plt.plot(C);plt.show()

