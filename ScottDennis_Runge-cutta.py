# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 14:50:06 2023

@author: denni
"""
import numpy as np


k=52+1 #53   spring constant
m=80+100 #180    mass kg
A=0.1 # meters displacement start
v=0 #meters per sec start
t=0  # time 
w=(k/m)**0.5
tmax=10*2*np.pi*(1/w) 

                        #Runge Cutta method
x=A
v=0
dtmax=100
dtmin=1e-9 
while((dtmax-dtmin)>1e-9):
    dt=0.5*(dtmax+dtmin)
    flag=0
    
    for t in np.arange(dt,tmax+dt,dt):
        
        x_an=A*(np.cos(w*t))
        v_an=-A*w*(np.sin(w*t))
                
        ax=v             
        av=(-k/m)*x
        bx=(v+(dt/2)*av)
        bv=(-k/m)*(x+(dt/2)*ax)
        cx=(v+(dt/2)*bv)
        cv=(-k/m)*(x+(dt/2)*bx)
        dx=(v+dt*cv)
        dv=(-k/m)*(x+dt*cx)
        
        x=x+dt*(ax+(2*bx)+(2*cx)+dx)/6
        v=v+dt*(av+(2*bv)+(2*cv)+dv)/6
        if abs(x-x_an)>0.01*A or abs(v-v_an)>0.01*A*w: 
            flag=1
            break
       
    if flag==1:
        dtmax=dt
    else:
        dtmin=dt
    
    v=0
    x=A
print("max time step for Runge Cutta method is",dt)
