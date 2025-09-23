# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:39:32 2023

@author: 40325280
"""
#In this assignment you will determine the maximum stepsize permissable
#for the Euler, Euler-Cromer and Runge-Kutta methods in the simulation of
#a simple harmonic oscillator.




#student number is 40325280
import math
import matplotlib.pyplot as plt

#print("start")
k=52+1 #53   spring constant
m=80+100 #180    mass kg
A=0.1 # meters displacement start
v=0 #meters per sec start
t=0

tmax=116 #116 is 10 occilations



# #(dx/dt)=v
# #(dv/dt)=-(k/m)*x
# x=A
# ix=x
# t=0

# dtmax=10
# dtmin=0.00001
# while((dtmax-dtmin)>1e-6):
#     eul_disp=[]
#     an_displ=[]
#     time=[]
#     while t<=tmax:
#         dt=0.5*(dtmax+dtmin)
#         x_an=A*(math.cos(((k/m)**0.5)*t))
#         time.append(t)
#         an_displ.append(x_an)
        
#         ix=ix+dt*v
#         v=v+dt*((-k/m)*x)
#         eul_disp.append(x)
#         x=ix              
    
#         if abs(x-x_an)>0.01*A: 
#             print(t)
#             break
#         t=t+dt
#     if t<tmax:
#         dtmax=dt
#         print("1")
#     else:
#         dtmin=dt
#         print("2")
#     x=A
#     ix=x
#     t=0
#     v=0
# print("max time step for Euler method is ",dt)
# plt.plot(time,an_displ)
# plt.plot(time,eul_disp)






# x=A
# t=0
# v=0

# dtmax=10
# dtmin=0.00001
# while((dtmax-dtmin)>1e-6):
#     cromer_disp=[]
#     an_displ=[]
#     time=[]
#     while t<=tmax:
#         dt=0.5*(dtmax+dtmin)
#         x=x+dt*v
#         v=v+dt*(-k/m)*x
#         cromer_disp.append(x)
    
#         x_an=A*(math.cos(((k/m)**0.5)*t))
#         time.append(t)
#         an_displ.append(x_an)
    
#         if abs(x-x_an)>0.01*A: 
#             print(t)
#             break
#         else:
#             t=t+dt
#     if t<tmax:
#         dtmax=dt
#         print("1")
#     else:
#         dtmin=dt
#         print("2")
#     x=A
#     t=0
#     v=0
# print("max time step for Euler-Cromer method is ",dt)
# plt.plot(time,cromer_disp)
# plt.plot(time,an_displ)





x=A
t=0
v=0
#(dx/dt)=v
#(dv/dt)=-(k/m)*x

dtmax=10
dtmin=0.00001
while((dtmax-dtmin)>1e-6):
    run_kutta_disp=[]
    an_displ=[]
    time=[]
    while t<=tmax:
               
        dt=0.5*(dtmax+dtmin)
        x_an=A*(math.cos(((k/m)**0.5)*t))
        time.append(t)
        an_displ.append(x_an)
        
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
        run_kutta_disp.append(x)
        if abs(x-x_an)>0.1*A: 
            print(t)
            break
        else:
            t=t+dt
    if t<tmax:
        dtmax=dt
        print("1")
    else:
        dtmin=dt
        print("2")
    t=0
    v=0
    x=A
     
print("max time step for Runge Cutta method is ",dt)

plt.plot(time,run_kutta_disp)
plt.plot(time,an_displ)



















