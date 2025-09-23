import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

%matplotlib QT
G=6.67430e-11 #m^3 kg^-1 s^2
m_sun=1.98892e30 #kg
m_earth=5.9742e24 #kg
#r=0.4+(5280/25000) #AU   #part 3
AU=1.495978707e11 #m
day=86400 #s
year=365.25 #days
#r=r*AU
tmax=1010*year*day
dt=86400 #losses accuracy quicker for inner planets 

n=3 #number of bodies

r= np.full((n,n),0.)

name=[]
m=[]
x=[]
m.append(m_sun); name.append("sun");x.append(0) #0
#m.append(0.33e24); name.append("mercury");x.append(57.9e9) #1
m.append(4.87e24); name.append("venus");x.append(108.2e9) #2
#m.append(m_earth); name.append("earth");x.append(1*AU)  #3
#m.append(0.642e24); name.append("mars");x.append(228e9) #4
m.append(1.8986e27); name.append("jupiter");x.append(778.5e9) #5 
#m.append(568e24); name.append("saturn");x.append(1432e9) #6
#m.append(86.8e24); name.append("uranus");x.append(2867e9) #7
#m.append(102e24); name.append("neptune");x.append(4515e9) #8
#m.append(0.95e18); name.append("astroid"); x.append(4.279*AU) #9

y=[0]*n
vx=[0.0]*n
vy=[0.0]*n
vtotal=[0]*n

files=[]
for i in range (n):
    files.append("null")
    files[i]= open(f"{name[i]}.txt","w")
    if i==0 :
        pass
    else:
        vtotal[i]=(G*m_sun/(r[0][i]))**0.5
        vy[i]=float(vtotal[i])
        vy[0]+= float(-vy[i]*m[i]/m[0])
    for j in range (n):
        r[i][j]=((x[i]-x[j])**2+(y[i]-y[j])**2)**0.5    

def runge_v(g,h,i):
    sumvx=0
    sumvy=0
    for j in range(n):
        if j==i: pass
        else:
            r[i][j]=((g-x[j])**2+(h-y[j])**2)**0.5
            sumvx+=G*m[j]*(x[j]-g)/(r[i][j])**3
            sumvy+=G*m[j]*(y[j]-h)/(r[i][j])**3
    return sumvx, sumvy

#runge cutta does not appear to conserve energy unlike Cromer
#things are going wrong by ax and av 
a=0
x2=([0]*n)
y2=([0]*n)
x2=(x2*0)+x
y2=(y2*0)+y

for t in np.arange(dt,tmax,dt):
    if a==1:
        a=0
    for i in range (0,n):
            if a==0:   
                files[i].write(str(x[i])+" "+str(y[i])+"\n")
              
            ax=vx[i] 
            ay=vy[i]   
            av=runge_v(x[i], y[i], i)
            avx, avy=av
            
            bx=vx[i]+dt*(avx)/2
            by=vy[i]+dt*(avy)/2
            bv=runge_v((x[i]+(dt*ax/2)), (y[i]+(dt*ay/2)), i)
            bvx, bvy=bv
            
            cx=vx[i]+dt*(bvx)/2
            cy=vy[i]+dt*(bvy)/2        
            cv=runge_v((x[i]+(dt*bx/2)), (y[i]+(dt*by/2)), i)
            cvx, cvy=cv
            
            dx=vx[i]+dt*(cvx)
            dy=vy[i]+dt*(cvy)
            dv=runge_v((x[i]+(dt*cx)), (y[i]+(dt*cy)), i)
            dvx, dvy=dv
            
            x2[i]=x[i]+dt*(ax+(2*bx)+(2*cx)+dx)/6
            y2[i]=y[i]+dt*(ay+(2*by)+(2*cy)+dy)/6   
            vx[i]=vx[i]+dt*(avx+(2*bvx)+(2*cvx)+dvx)/6
            vy[i]=vy[i]+dt*(avy+(2*bvy)+(2*cvy)+dvy)/6
            
    a=a+1       
    x=(x*0)+x2
    y=(y*0)+y2


for i in range (n):
    xplot=[];yplot=[]
    files[i].close()
    for row in open(f"{name[i]}.txt","r"): 
        row = row.split(' ') 
        xplot.append(float(row[0])) 
        yplot.append(float(row[1]))
    plt.plot(xplot,yplot,label=name[i])

plt.title("Runge Kutta") 
plt.grid()
plt.legend()

print("--- %s seconds ---" % (time.time() - start_time))

# possibly print every hundred iterations to a file to speed thigs up while mentaining
# lower step sizes 

# kirk wood gaps may need to be researched with smaller orbits for effect to be found 
# relatively quickly (still 100s of years )




