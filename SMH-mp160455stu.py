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


x=A
t=0
v=0
#(dx/dt)=v
#(dv/dt)=-(k/m)*x
dt=0.6
run_kutta_disp=[]
an_displ=[]
time=[]
while t<=tmax:
                  

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
        t=t+dt
    
     
print("max time step for Runge Cutta method is ",dt)
print(x_an)
print(x)
print(x/x_an)
plt.plot(time,run_kutta_disp)
plt.plot(time,an_displ)

