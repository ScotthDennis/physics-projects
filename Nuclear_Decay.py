import math 
import matplotlib.pyplot as plt


N0=1000 
tau=20
tmax=100
dt=10
t=0

Nexactlist=[]
exact_t=[]
while t<=tmax:
    Nexact=N0*math.exp(-t/tau)
    Nexactlist.append(Nexact)
    exact_t.append(t)
    t=t+dt

plt.plot(exact_t,Nexactlist)



 # euler method
 #(dN/dt)=-N/tau
 # N(t+dt)=N(t)+dt*(dN/dt)
t=0
Neu=N0
euler_N=[]
while t<=tmax:
    euler_N.append(Neu)
    Neu=Neu+(dt*(-Neu/tau))
    t=t+dt
plt.plot(exact_t,euler_N)


#Runge-Kutta Method
#N(t+dt)=N(t)+dt(a+2b+2c+d)/6

t=0
Nrk=N0
Run_kut_N=[]

while t<=tmax:
    Run_kut_N.append(Nrk)
    a=(-Nrk/tau)
    b=(-(Nrk+dt*a/2)/tau)
    c=(-(Nrk+dt*b/2)/tau)
    d=(-(Nrk+dt*c)/tau)
    Nrk=Nrk+(dt*(a+(2*b)+(2*c)+d)/6)
    t=t+dt
    
plt.plot(exact_t,Run_kut_N)
