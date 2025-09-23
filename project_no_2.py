import numpy as np
import matplotlib.pyplot as plt
G=6.67430e-11 #m^3 kg^-1 s^2

m_sun=1.98892e30 #kg
m_earth=5.9742e24 #kg
#r=0.4+(5280/25000) #AU   #part 3
AU=1.495978707e11 #m
day=86400 #s
year=365.25 #days
#r=r*AU
tmax=1*year*day
dt=1000000


n=2 #number of bodies

r= np.full((n,n),0.)




m=[0]*n
m[0]=m_sun #sun
m[1]=m_earth
#m[2]=2e25


x=[0]*n
x[0]=0 #sun
x[1]=1*AU               #(0.4+(5280/25000))*AU
#x[2]=-15*AU

y=[0]*n
y[0]=0 #sun
y[1]=0
#y[2]=0

vx=[0]*n
vy=[0]*n

for i in range (n):
    for j in range (n):
        r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5


def sec_difx(i,j):
    return (G*m[j]*(x[j]-x[i])/(r[i][j])**3)

def sec_dify(i,j):
    return (G*m[j]*(y[j]-y[i])/(r[i][j])**3)

vtotal=[0]*n

vtotal[1]=(G*m_sun/(r[0][1]))**0.5

x_lists=[[]]*n
y_lists=[[]]*n




vx[1]=0
vy[1]=float(vtotal[1])


for t in np.arange(dt,dt*100,dt):
    
    for i in range (n):
            sumvx=0
            sumvy=0
            x[i]=x[i]+dt*vx[i]
            y[i]=y[i]+dt*vy[i]
            
            x_lists[i]=x_lists[i]+[x[i]]
            
            y_lists[i]=y_lists[i]+[y[i]]
            for j in range(n):
                if j==i: break
                else:
                    r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
                    sumvx+=sec_difx(i,j)
                    sumvy+=sec_dify(i,j)
            vx[i]=vx[i]+dt*sumvx
            vy[i]=vy[i]+dt*sumvy
            
            
        
for i in range (n):
    plt.plot(x_lists[i],y_lists[i])


plt.grid()




















