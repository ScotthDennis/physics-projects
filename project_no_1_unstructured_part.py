import numpy as np
import matplotlib.pyplot as plt
                    #runge cutta method
                    # dampend or driven pendulum
#d^2θ/dt^2=-(g/L)sin(θ)
#dθ/dt=w
#dw/dt=-(g/L)sin(θ)

#g=gravity=9.81 m/s^2
#L=length of pendulum=0.5+(5480/10000) m

L=0.5+(5280/10000)
g=9.81
tmax=100
dt=0.01

#θ(t+dt)=θ(t)+dt*(dθ(t)/dt)
#dθ/dt=w
#w(t+dt)=w(t)+dt*(dw(t)/dt)
#dw/dt=-(g/L)sin(θ)-q*w+ F*sin(u*t)
# q is the damping coefficient 
# F is the maximum angular acceleration due to the periodic driving force
# u is the angular driving frequency 
#  y=θ

#y=10 #degrees


def dif_w(y):
    return (-(g/L)*np.sin(np.deg2rad(y))-(q*w)+(F*np.sin(np.deg2rad(u)*t)))

y=3
q=0.02
F=1
u=50


#amplitude=[]                  
#frequency=[]
      
#for i in range(3):    
while y<=20:
#while F<=2:
#while q<=1:
#while u<=40
    y_initial=y
    #amplitude.append(y_initial)         
    
    time=[]
    angle=[]
    #angvel=[]
    halfperiod_list=[]
    w=0
    y_old=0
    flag=0
    old_mark=0
    for t in np.arange(0,tmax,dt):
        
        time.append(t)
        angle.append(y)
        #angvel.append(w)
        ay=w             
        aw=dif_w(y)
        by=(w+(dt/2)*aw)
        bw=dif_w(y+(dt/2)*ay)
        cy=(w+(dt/2)*bw)
        cw=dif_w(y+(dt/2)*by)
        dy=(w+dt*cw)
        dw=dif_w(y+dt*cy)
        
        y=y+dt*(ay+(2*by)+(2*cy)+dy)/6
        w=w+dt*(aw+(2*bw)+(2*cw)+dw)/6
        
        if y*y_old<0:
             halfperiod_mark=t-((y/(y-y_old))*dt)
             if flag==1:
               halfperiod=halfperiod_mark-old_mark
               halfperiod_list.append(halfperiod)
             else:
                flag=1
             old_mark=halfperiod_mark
        y_old=y
    
    period=2*np.average(halfperiod_list)            #part 2
    y=y_initial*2                               #part 2
    #F=F*2
    #q=q*2 
    #u=u*2
    freq= 1/period                               #part 2
    
    
    #frequency.append(freq)          #part 3
    
    
    print("frequency of",y_initial," degrees is", freq)
    plt.plot(time,angle,label=f"θ={y_initial}, q={q},F={F}, u={u}")
    #plt.plot(time,angvel)


#plt.plot(amplitude,frequency)
plt.grid()
plt.legend()


