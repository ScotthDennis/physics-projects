print("Hello world again")
#n1= input("How many hot dogs")
#n2=25
#print("please may i have \n",n1,"hot dogs and","\n",n2,"burgers")
#d1=float(input("first number?"))
#d2=float(input("second number?"))
#d3=float(input("third number?"))
#d4=float(input("fourth number?"))
#average=(d1+d2+d3+d4)/4

                                            #exercize 10
#n1=int(input("first number?"))
#n2=int(input("second number?"))
#print(n1-n2);print(n1+n2);print(n1*n2)

#string1=input("enter some text.")
#string2=input("enter some text.")
#(string1+"\n"+string2)

#file_out = open("text_output.txt","w")
        # the "w" means write the file
            # ("r" means read the file)
#file_out.write(string1 + "\n" + string2)
#file_out.close()

#fout = open("text.txt","w")
#fout.write("message")
#fout.close()

#n1=6 #int(input("first number?"))
#n2=73 #int(input("second number?"))
#print(n1-n2);print(n1+n2);print(n1*n2)
#fout=open("data.txt","w")
#fout.write(str(n1-n2)+"\n"+str(n1+n2)+"\n"+str(n1*n2))
#fout.close()

#fin=open("data.txt","r") #fin is file_in
#n3= int(fin.readline())
#print(n3)

#d1=float(input("first number?"))
#d2=float(input("second number?"))
#d3=float(input("third number?"))
#d4=float(input("fourth number?"))
#average=(d1+d2+d3+d4)/4
#fout=open("average.txt","w")
#fout.write(str(average))
#fout.close()

#fin=open("average.txt","r")
#print("average is",fin.readline())
                                            #exercise 20
#fout=open("hello.txt","w")
#fout.write(str(input("what is your name?")))
#fout.close()
#fin=open("hello.txt","r")
#print("Hello",fin.readline())
#fin.close()

#file=str(input("file name"))
#file_out=open(file,"w")
#file_out.write("hello")
#file_out.close()

#with open("text2.txt","w") as fout:
    #fout.write("message")

                                           # exercise 25

#a=int(input("first number"))
#b=int(input("second number"))
#print("a to the power b is", a**b)

#import math
#x=int(input("angle in degrees"))
#print(math.sin(math.radians(x)))

#print(math.log2(x));print(math.log10(x))


#print((4>3 or not 12>=3) and 4==3)
#print(4>3 or (not 12>=3 and 4==3))

#m=6
#n=int(input("input number"))
#if n<m:
    #print("you entered",n,"which is less than",m)
#elif n==m:
    #print("you entered",n,"which is equal to",m)
#else:
    #print("you entered",n,"which is more than",m)
 
                                               #exercise 30

#print("quadratic root finder")
#a=float(input("input a."))
#b=float(input("input b."))
#c=float(input("input c."))

#if ((b**2)-(4*a*c))>0:
#    print("there are two real roots")
#    x1=((-b/(2*a))+((((b**2)-(4*a*c))**(0.5))/(2*a)))
#    x2=((-b/(2*a))-((((b**2)-(4*a*c))**(0.5))/(2*a)))
#    print(x1," and ",x2)
#elif ((b**2)-(4*a*c))==0:
#    print("there is one real root")
#    x1=(-b/(2*a))
#    print(x1)
#else:
#    print("there are two complex roots")
#    xend=(((abs((b**2)-(4*a*c)))**(0.5))/(2*a))
#   # #x1=((-b/(2*a)), "+" ,xend, "j")
#    x1=complex((-b/(2*a)),xend)
#   # #x2=((-b/(2*a)),"-",xend,"j")
#    x2=complex((-b/(2*a)),-xend)
#    print(x1," and ",x2)

                                            #exercise 32
#i=0
#while i<=9:
#    print(i*2)
 #   i=i+1

#for i in range(12,-7,-3):
#   print(i)

#for i in range(1,31):
#    if (i/3)==int(i/3):
#        pass
#    else:
 #       print(i)

#for i in range(1,31):
#    if (i/3)==int(i/3) or (i/5)==int(i/5):
#        pass
#    else:
#        print(i)

#x=int(input("number"))
#for i in range(x):
#    print("*",end="")

#for i in range(21):
#    print(i, i/10)

                                    #exercise 40
#a=int(input("start value"))
#b=int(input("end value"))
#c=int(input("stepsize"))
#for i in range(a,b,c):
 #   x=(i)
#    y=(x/(1+(x*x)))
 #   print(x,y)




#a=12
#b=3.145 ; name="computer"
#print(f"{a} hotdogs with {b} g of sause for {name}")

                               # 4.9. Functions.
#def factorial(n):
#    b=1
#    for c in range(2,n+1):
#        b*=c
#        # or b=b*c
#    return b

#w=7
#answer=factorial(w)
# print(answer)


#def hello():
#    print("hello there!!")
    

#def factorial(n):
#    b=1
#    for c in range(2,n+1):
#        b=b*c
#    return b

#for i in range(1,11):
#    a=factorial(i)
#    print(a)

#def astrerisk(n):
#    x=n #int(input("number"))
#    for i in range(x):
#        print("*",end="")


#astrerisk(int(input("number")))

                                #exercise 45

#nums=[]
#for i in range(10):
#    nums.append((i*(i+1)/2))
#    print(i,nums[i])
                                    #exercise 50
import matplotlib.pyplot as plt
funct=[]
ran=[]
funct2=[]
for x in range(-10,11):
    funct.append(x**2)
    ran.append(x)
    funct2.append(x**3)

plt.plot(ran,funct)
plt.plot(ran,funct2)






