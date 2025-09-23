import numpy as np
# student number =40325280
T= np.full((4,4),0.)
T_2= np.full((4,4),0.)
a=5;b=2;c=8;d=0

T[3][1]=T[3][2]=a
T[1][3]=T[2][3]=b
T[0][1]=T[0][2]=c
T[1][0]=T[2][0]=d

T_2=T_2*0+T
start=0

while start==0 or np.all(T==T_2)==False:
    T=T*0+T_2
    start=1        # flag that the loop has done one iteration 
    for j in range(1,2+1):
        for i in range(1,2+1):
            T_2[j][i]=(T[j][i-1]+T[j][i+1]+T[j-1][i]+T[j+1][i])/4        
    
print(T)
print("T11 is",T[2][1])
print("T12 is",T[2][2])
print("T21 is",T[1][1])
print("T22 is",T[1][2])