''' Problem 8 final exam
Solving 2nd order diff eq
NAME: SAGAR DAM;    DNAP
'''

import numpy as np
import matplotlib.pyplot as plt

#defining variables:
a=0
b=60
g=10
h=0.01
t1=1
xend=2
err=0.01 #which I have initially set as error limit
t=np.arange(0,t1+h,h) #independent variable
x=np.ones(len(t)) #dependent variable
x[0]=0
v=np.zeros(len(t))

#defining function for euler technique in shooting loop
def f(t,x,v):
    return v
def f1(t,x,v):
    return 4*(x-t)

# Introducing Shooting condition:

while (abs(x[len(t)-1]-xend)>err):
    r=(a+b)/2    
    v[0]=r
    x[0]=0
    
# Doing the Euler solution:
    for i in range(len(t)-1):
        v[i+1]=v[i]+h*f1(t[i],x[i],v[i])
        x[i+1]=x[i]+h*f(t[i],x[i],v[i])
    if(x[len(t)-1]<xend):
        a=r
    elif(x[len(t)-1]>xend):
        b=r  
#    plt.plot(t,x,'y')
        
#defining true solution
def true(t):
    z=np.exp(2)*(np.exp(2*t)-np.exp(-2*t))/(np.exp(4)-t)+t
    return z

#calculation of true solution and error
truesol=np.zeros(len(t))
error=np.zeros(len(t))
for i in range(len(t)):
    truesol[i]= true(t[i])
    if(truesol[i]==0):
        error[i]=0
    else:
        error[i]=abs(truesol[i]-x[i])*100/(truesol[i])
 
#plotting the true and numerical solution.....    
plt.plot(t,x,'b',label='numerical solution')
plt.title('I have used shooting method')
plt.suptitle('Solving the eqn y"(x)=4(y-x) with y(0)=0; y(1)=2')
plt.plot(t,truesol,'r',label='true solution')
plt.legend()
plt.grid()
plt.xlabel('t')
plt.ylabel('x')
plt.show()

#plotting the relative percentage error
plt.plot(t,error,'k',markersize=0.5)
plt.title('percentage relative error in the numerical siolution')
plt.xlabel('indp variable value')
plt.ylabel('relative percentage error')
plt.legend()
plt.grid()
plt.show()