import numpy as np
import matplotlib.pyplot as plt
G=6.67430e-11 #m^3 kg^-1 s^2

#%matplotlib QT

m_sun=1.98892e30 #kg
m_earth=5.9742e24 #kg
#r=0.4+(5280/25000) #AU   #part 3
AU=1.495978707e11 #m
day=86400 #s
year=365.25 #days
#r=r*AU
tmax=15*year*day
dt=10000 #losses accuracy quicker for inner planets 


n=2 #number of bodies

r= np.full((n,n),0.)




m=[]
m.append(m_sun) #sun
# m.append(0.33e24) #mercury
# m.append(4.87e24) #venus
# m.append(m_earth) #earth
# m.append(0.642e24) #mars
m.append(1.8986e27) #jupiter
# m.append(568e24) #saturn
# m.append(86.8e24) #uranus
# m.append(102e24) #neptune
# m.append(0.95e21) #astroid 

x=[]
x.append(0) #sun   0
# x.append(57.9e9) #mercury  1
# x.append(108.2e9) #venus  2
# x.append(1*AU)  #earth   3
# x.append(228e9) #mars    4
x.append(778.5e9) #jupiter   5
# x.append(1432e9) #saturn   6
# x.append(2867e9) #uranus   7
# x.append(4515e9) #neptune   8
# x.append(2.5*AU) #astroid  9



y=[0]*n





vx=[0.0]*n
vy=[0.0]*n

vtotal=[0]*n


for i in range (n):
    if i==0 :
        pass
    else:
        #find the suns momentum in here with a sum array
        vtotal[i]=(G*m_sun/(r[0][i]))**0.5
        vy[i]=float(vtotal[i])
        vy[0]+= float(-vy[i]*m[i]/m[0])
        
    for j in range (n):
        r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5


def sec_difx(i,j):
    return (G*m[j]*(x[j]-x[i])/(r[i][j])**3)

def sec_dify(i,j):
    return (G*m[j]*(y[j]-y[i])/(r[i][j])**3)




x_lists=[[]]*n
y_lists=[[]]*n



# can try to change code to runge cutta

a=0

for t in np.arange(dt,tmax,dt):
    
    if a==100:
        a=0
        
    
    
    for i in range (n):
            sumvx=0
            sumvy=0
            x[i]=x[i]+dt*vx[i]
            y[i]=y[i]+dt*vy[i]
            
            if a==0:
                x_lists[i]=x_lists[i]+[x[i]]
                
                y_lists[i]=y_lists[i]+[y[i]]
                
            for j in range(n):
                r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
            for j in range(n):
                if j==i: pass
                else:
                    r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5
                    sumvx+=sec_difx(i,j)
                    sumvy+=sec_dify(i,j)
            vx[i]=vx[i]+dt*sumvx
            vy[i]=vy[i]+dt*sumvy
            
    a=a+1     
        
for i in range (n):
    plt.plot(x_lists[i],y_lists[i],label=i)


plt.grid()
plt.legend()




# possibly print every hundred iterations to a file to speed thigs up while mentaining
# lower step sizes 

# kirk wood gaps may need to be researched with smaller orbits for effect to be found 
# relatively quickly (still 100s of years )




