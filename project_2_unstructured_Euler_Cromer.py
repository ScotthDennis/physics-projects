import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

#%matpl#otlib QT
G=6.67430e-11 #m^3 kg^-1 s^2
m_sun=1.98892e30 #kg
m_earth=5.9742e24 #kg
#r=0.4+(5280/25000) #AU   #part 3
AU=1.495978707e11 #m
day=86400 #s
year=365.25 #days
#r=r*AU
tmax=700*year*day
dt=40000 #losses accuracy quicker for inner planets 

n=2 #number of bodies

r= np.full((n,n),0.)

name=[]
m=[]
x=[]
m.append(m_sun); name.append("sun");x.append(0) #0
#m.append(0.33e24); name.append("mercury");x.append(57.9e9) #1
#m.append(4.87e24); name.append("venus");x.append(108.2e9) #2
m.append(m_earth); name.append("earth");x.append(1*AU)  #3
#m.append(0.642e24); name.append("mars");x.append(228e9) #4
#m.append(1.8986e27); name.append("jupiter");x.append(778.5e9) #5 
#m.append(568e24); name.append("saturn");x.append(1432e9) #6
#m.append(86.8e24); name.append("uranus");x.append(2867e9) #7
#m.append(102e24); name.append("neptune");x.append(4515e9) #8
#m.append(0.95e18); name.append("astroid"); x.append(3.279*AU) #9

y=[0]*n
vx=[0.0]*n
vy=[0.0]*n
vtotal=[0]*n

y_old=[0]*n
halfperiod_list=[[]]*n
old_mark=[0]*n


files=[]
for i in range (n):
    files.append("null")
    files[i]= open(f"{name[i]}.txt","w")
    if i==0 :
        pass
    else:
        vtotal[i]=(G*m_sun/(r[0][i]))**0.5
        vy[i]=float(vtotal[i])
        #vy[0]+= float(-vy[i]*m[i]/m[0])
    for j in range (n):
        r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5

def difvx(i,j):
    return (G*m[j]*(x[j]-x[i])/(r[i][j])**3)
def difvy(i,j):
    return (G*m[j]*(y[j]-y[i])/(r[i][j])**3)

flag=0

for t in np.arange(dt,tmax,dt):
    if flag==1:
        flag=0
    for i in range (1,n):
            x[i]=x[i]+dt*vx[i]
            y[i]=y[i]+dt*vy[i]
            if flag==0:
                files[i].write(str(x[i])+" "+str(y[i])+"\n")
                
    flag=flag+1           
    for i in range(1,n):
            sumvx=0
            sumvy=0
            for j in range(n):
                if j==i: pass
                else:
                    r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
                    sumvx+=difvx(i,j)
                    sumvy+=difvy(i,j)
            vx[i]=vx[i]+dt*sumvx
            vy[i]=vy[i]+dt*sumvy
            
            if y[i]*y_old[i]<0:
                 halfperiod_mark=t-((y[i]/(y[i]-y_old[i]))*dt)
                 halfperiod=halfperiod_mark-old_mark[i]
                 halfperiod_list[i]=halfperiod_list[i]+[halfperiod]
                 
                 old_mark[i]=halfperiod_mark
            y_old[i]=y[i]
            
            
for i in range(1,n): #sun doesnt need to be measured
    period=2*np.average(halfperiod_list[i])
    print(f"{name[i]}'s period is {period/day} days or {period/(year*day)} years")
    
for i in range (n):
    xplot=[];yplot=[]
    files[i].close()
    for row in open(f"{name[i]}.txt","r"): 
        row = row.split(' ') 
        xplot.append(float(row[0])) 
        yplot.append(float(row[1]))
    plt.plot(xplot,yplot,label=name[i])
    
plt.title("Euler Cromer") 
plt.grid()
plt.legend()

print("--- %s seconds ---" % (time.time() - start_time))

# possibly print every hundred iterations to a file to speed thigs up while mentaining
# lower step sizes 

# kirk wood gaps may need to be researched with smaller orbits for effect to be found 
# relatively quickly (still 100s of years )




