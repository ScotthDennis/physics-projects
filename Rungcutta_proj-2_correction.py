import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time() #calculates run time of program


G=6.67430e-11 #m^3 kg^-1 s^2
m_sun=1.98892e30 #kg
m_earth=5.9742e24 #kg
AU=1.495978707e11 #m
day=86400 #s
year=365.25 #days
tmax=1*year*day
dt=5000000 #losses accuracy quicker for inner planets 

n=3 #number of bodies (including sun)

r= np.full((n,n),0.) # empty array of distance between bodies

name=[]  #an empty array of names for graph legend
m=[]   #an empty array of masses
x=[]    # an empty array of x position 
m.append(m_sun); name.append("Sun");x.append(0) #0     
#m.append(0.33e24); name.append("Mercury");x.append(57.9e9) #1
# m.append(4.87e24); name.append("Venus");x.append(108.2e9) #2
# m.append(m_earth); name.append("Earth");x.append(1*AU)  #3
# m.append(0.642e24); name.append("Mars");x.append(228e9) #4
m.append(1.8986e27); name.append("Jupiter");x.append(778.5e9) #5 
# m.append(568e24); name.append("Saturn");x.append(1432e9) #6
# m.append(86.8e24); name.append("Uranus");x.append(2867e9) #7
# m.append(102e24); name.append("Neptune");x.append(4515e9) #8
m.append(0.95e20); name.append("astroid"); x.append(70) #9

y=[0]*n
vx=[0.0]*n
vy=[0.0]*n
vtotal=[0]*n

files=[] # an array for making file names same as the associated bodies name
astro_KE=open("astro_KE1.txt","w")
for i in range (n):
    files.append("null")
    files[i]= open(f"{name[i]}.txt","w")
    if i==0 :
        pass
    else:
        vtotal[i]=(G*m_sun/(r[0][i]))**0.5 #finds inital velocity of all planets
        vy[i]=float(vtotal[i])
        vy[0]+=float(-vy[i]*m[i]/m[0]) # finds inital velocity of sun
    for k in range (n):
        r[i][k]=((x[i]-x[k])**2+(y[i]-y[k])**2)**0.5    



def pull(xi,yi,xk,yk,mk):       #function calculates the pull of one body on another
    r=((xi-xk)**2+(yi-yk)**2)**0.5
    sumvx=G*mk*(xk-xi)/(r)**3
    sumvy=G*mk*(yk-yi)/(r)**3
    return sumvx, sumvy         

 
flag=0  #flag to reduce how often data is writen to file hopefully speed up program
ax=[0]*n; ay=[0]*n; avx=[0]*n; avy=[0]*n;
bx=[0]*n; by=[0]*n; bvx=[0]*n; bvy=[0]*n; 
cx=[0]*n; cy=[0]*n; cvx=[0]*n; cvy=[0]*n; 
dx=[0]*n; dy=[0]*n; dvx=[0]*n; dvy=[0]*n;  #Empty lists used in Runge Kutta 

y_old=[0]*n
halfperiod_list=[[]]*n
old_mark=[0]*n


for t in np.arange(dt,tmax,dt):
    if flag==1: #change this to get only 1/flag loops writen to file
        flag=0
    for i in range (0,n):
            ax[i]=vx[i] 
            ay[i]=vy[i]   
            sumvx=0
            sumvy=0
            for k in range(n):
                if k==i: pass
                else:
                    a,b=pull(x[i],y[i],x[k],y[k],m[k])
                    sumvx+=a
                    sumvy+=b
            avx[i]=sumvx
            avy[i]=sumvy
            
    for i in range (0,n):        
            bx[i]=vx[i]+dt*(avx[i])/2
            by[i]=vy[i]+dt*(avy[i])/2
            sumvx=0
            sumvy=0
            for k in range(n):
                if k==i: pass
                else:
                    a,b=pull(x[i]+(dt*ax[i]/2),(y[i]+(dt*ay[i]/2)),(x[k]+(dt*ax[k]/2)),(y[k]+(dt*ay[k]/2)),m[k])
                    sumvx+=a
                    sumvy+=b
            bvx[i]=sumvx
            bvy[i]=sumvy
    for i in range (0,n):        
            cx[i]=vx[i]+dt*(bvx[i])/2
            cy[i]=vy[i]+dt*(bvy[i])/2        
            sumvx=0
            sumvy=0
            for k in range(n):
                if k==i: pass
                else:
                    a,b=pull(x[i]+(dt*bx[i]/2),(y[i]+(dt*by[i]/2)),(x[k]+(dt*bx[k]/2)),(y[k]+(dt*by[k]/2)),m[k])
                    sumvx+=a
                    sumvy+=b
            cvx[i]=sumvx
            cvy[i]=sumvy        
                    
    for i in range (0,n):        
            dx[i]=vx[i]+dt*(cvx[i])
            dy[i]=vy[i]+dt*(cvy[i])
            sumvx=0
            sumvy=0
            for k in range(n):
                if k==i: pass
                else:
                    a,b=pull(x[i]+(dt*cx[i]),(y[i]+(dt*cy[i])),(x[k]+(dt*cx[k])),(y[k]+(dt*cy[k])),m[k])
                    sumvx+=a
                    sumvy+=b
            dvx[i]=sumvx
            dvy[i]=sumvy
    for i in range (0,n):        
            x[i]=x[i]+dt*(ax[i]+(2*bx[i])+(2*cx[i])+dx[i])/6
            y[i]=y[i]+dt*(ay[i]+(2*by[i])+(2*cy[i])+dy[i])/6   
            vx[i]=vx[i]+dt*(avx[i]+(2*bvx[i])+(2*cvx[i])+dvx[i])/6
            vy[i]=vy[i]+dt*(avy[i]+(2*bvy[i])+(2*cvy[i])+dvy[i])/6
            if flag==0:   
                files[i].write(str(x[i])+" "+str(y[i])+"\n")
                if i==2:
                    astro_KE.write(str((m[2])*(((vx[2])**2)+((vy[2])**2))/2)+" "+str(t)+"\n")
                
            if y[i]*y_old[i]<0:
                 halfperiod_mark=t-((y[i]/(y[i]-y_old[i]))*dt)
                 halfperiod=halfperiod_mark-old_mark[i]
                 halfperiod_list[i]=halfperiod_list[i]+[halfperiod]
                 
                 old_mark[i]=halfperiod_mark
            y_old[i]=y[i]
        
     
                
    flag=flag+1       


astro_KE.close()
#import matplotlib.pyplot as plt
# KEplot=[]
# tplot=[]
# for row in open("astro_KE.txt","r"): 
#         row = row.split(' ')                  #for astroid kenetic energy
#         KEplot.append(float(row[0])) 
#         #yplot.append(float(row[1]))
# plt.plot(KEplot)

for i in range (n):
    xplot=[];yplot=[]
    files[i].close()
    for row in open(f"{name[i]}.txt","r"): 
        row = row.split(' ') 
        xplot.append(float(row[0])) 
        yplot.append(float(row[1]))
    plt.plot(xplot,yplot,label=name[i])
    plt.scatter(x[i],y[i])

plt.title("Model of the Solar System") 
plt.xlabel("x position (m)")
plt.ylabel("y position (m)")
plt.grid()
plt.legend(loc='upper right')

print("--- %s seconds ---" % (time.time() - start_time))

# possibly print every hundred iterations to a file to speed thigs up while mentaining
# lower step sizes 

# kirk wood gaps may need to be researched with smaller orbits for effect to be found 
# relatively quickly (still 100s of years )

