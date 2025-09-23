#student number is 40325280
import numpy as np
k=52+1 #53   spring constant
m=80+100 #180    mass 
A=0.1 # displacement start/max amplitude
v=0 #velocity at start
t=0  # time 
w=(k/m)**0.5
tmax=10*2*np.pi*(1/w) #time taken for 10 full oscilations to occur
#(dx/dt)=v
#(dv/dt)=-(k/m)*x
                       #Euler method

dtmax=10    #initial maximum stepsize 
dtmin=1e-9  #initial minimum stepsize
while((dtmax-dtmin)>1e-9):
    dt=0.5*(dtmax+dtmin)
    x=A
    new_x=x
    t=0
    v=0
    flag=0      
    while t<=tmax-dt:
        t=t+dt
        x_an=A*(np.cos(w*t))    
        v_an=-A*w*(np.sin(w*t))
        
        new_x=new_x+dt*v
        v=v+dt*((-k/m)*x)
        x=new_x              
    
        if abs(x-x_an)>0.01*A or abs(v-v_an)>0.01*A*w : 
            flag=1
            break
    if flag ==1:
        dtmax=dt
    else:
        dtmin=dt
print("max time step for Euler method is",dt)


                        #Euler-Cromer method
dtmax=10
dtmin=1e-9
while((dtmax-dtmin)>1e-9):
    dt=0.5*(dtmax+dtmin)
    flag=0
    x=A
    t=0
    v=0
    while t<=tmax-dt:
        t=t+dt
        x=x+dt*v
        v=v+dt*(-k/m)*x
    
        x_an=A*(np.cos(w*t))  
        v_an=-A*w*(np.sin(w*t))
        if abs(x-x_an)>0.01*A or abs(v-v_an)>0.01*A*w: 
            flag=1
            break
      
    if flag==1:
        dtmax=dt
    else:
        dtmin=dt
print("max time step for Euler-Cromer method is",dt)


                        #Runge Kutta method
dtmax=100
dtmin=1e-9 
while((dtmax-dtmin)>1e-9):
    dt=0.5*(dtmax+dtmin)
    flag=0
    t=0
    v=0
    x=A
    while t<=tmax-dt:
        t=t+dt
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
print("max time step for Runge Kutta method is",dt)
