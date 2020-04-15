## Puff-Lagrangiano

#Packages:
from math import *
from numpy import *
from numpy.linalg import *

#Functions:
ERF=vectorize(erf)

#traj
def traj(t):
    X=30*cos(t*0.05)+Xi
    Y=t*1.5 + Yi
    Z=sqrt(sqrt(t))*0.1+Zi
    return(X,Y,Z)

def C(t):
    #Trayectoria:

    X2,Y2,Z2 = traj(t)
    X1,Y1,Z1 = traj(t-dt)

    dx= X2-X1
    dy= Y2-Y1
    dQ= Q*exp(-lambda1*t) - Q*exp(-lambda1*(t-dt))
    
    g=1.#(2/(sqrt(2*pi)*sigma_z))
    
    sigma_x=sqrt(Kx*pi*2*t);
    sigma_y=sqrt(Ky*pi*2*t);
    sigma_z=sqrt(Kz*pi*2*t);

    #   
    a= (dx*dx + dy*dy) / (sigma_x*sigma_y)
    b= (dx*(X1-X) + dy*(Y1-Y)) /(sigma_x*sigma_y)
    c= ((X1-X)**2 + (Y1-Y)**2) /(sigma_x*sigma_y)

    I1= sqrt(pi*0.5/a) * exp( (0.5*(b**2) /a) - (c*0.5) ) * (ERF( (a+b)/sqrt(2*a))- ERF(b/sqrt(2*a)))
    I2=( (-b*I1) /a) + (1/a)  * exp( b*b*0.5/a - c*0.5 ) * ( exp(-(b*b)*0.5/a)  - exp(-0.5* (a+2*b+b*b/a) ))  
    #
    C=g/(2*pi*sigma_x*sigma_y) *( Q*I1 + dQ*I2)
    return(C)    
    
#Params:
maxiter=70

dt=.5      #Time step
Kx=Ky=Kz=.25
M=1.       #Masa en el puff

Xi=-20     #X-coord inicial
Yi=-10     #Y-coord inicial
Zi=0.05    #Alt inicial
H=5.       #Altura efectiva
lambda1=0.001


#Grid:
x=linspace(-50,50,1000)
y=linspace(-50,50,1000)

X,Y= meshgrid(x,y)

#Solve:

CC=X*0.
t=1.
for i in range(maxiter):
    t+=dt
   
    CC+= (C(t)+C(t-dt))*0.5*dt/(maxiter*dt)

    print(sum(CC))
    #Plot:
    levs=linspace(0,.001,11)
    if (i%10 == 0):
        from matplotlib import pyplot as plt
        plt.clf();
        plt.contourf(X,Y,CC)#,levels=levs)

        plt.savefig("puff_int."+str(i)+".png")