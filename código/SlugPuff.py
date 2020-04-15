import os
os.chdir("/home/ram/Desktop/puff/") # Elijo directorio de trabajo
os.getcwd()                    # Consulto directorio actual
#
#
from numpy import *
from math import *

ERF=vectorize(erf)

#params:


#grid
x=linspace(-50,50,1000); y=linspace(-50,50,1000)

z=open('volcano','r').read().split('\n')
z=map(lambda i: z[i].split(','),range(len(z)))


#solve

sigma_x=sigma_y=sigma_z=2.
sigma_u=3.
uu=sqrt(u*u + sigma_u*sigma_u)

Q / (2*sqrt(2*pi)*uu*sigma_x) * exp(- (dc*dc*u*u) / (2*sigma_x*sigma_y*uu*uu) ) * ERF( (da2) / (sqrt(2)*sigma_y2) ) - ERF( (da2)/(sqrt(2)sigma))


