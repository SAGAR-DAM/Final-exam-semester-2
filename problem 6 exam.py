'''Problem 6 final exam
solving 1st order diff eq
NAME: SAGAR DAM;  DNAP'''

import numpy as np
import matplotlib.pyplot as plt
#defining variables
a=0
b=0.5
n=1000
h=(b-a)/n
t=np.arange(a,b,h)
x=np.zeros(len(t))
y=np.zeros(len(t))
x[0]=1/3
y[0]=1/3

def e(t,x,y):
    return (32*x+66*y+2*t/3+2/3)
def f(t,x,y):
    return (-66*x-133*y-t/3-1/3)

# The RK 4 method implementation....
for i in range(len(y)-1):
    n1=h*e(t[i],x[i],y[i])
    k1=h*f(t[i],x[i],y[i])

    
    n2=h*e(t[i]+h/2,x[i]+n1/2,y[i]+k1/2)
    k2=h*f(t[i]+h/2,x[i]+n1/2,y[i]+k1/2)

    
    n3=h*e(t[i]+h/2,x[i]+n2/2,y[i]+k2/2)
    k3=h*f(t[i]+h/2,x[i]+n2/2,y[i]+k2/2)
    
    n4=h*e(t[i]+h,x[i]+n3,y[i]+k3)
    k4=h*f(t[i]+h,x[i]+n3,y[i]+k3)
    
    x[i+1]=x[i]+(n1+2*n2+2*n3+n4)/6
    y[i+1]=y[i]+(k1+2*k2+2*k3+k4)/6
    
#plotting the graph
plt.plot(t,x,label='y1')
plt.plot(t,y,label='y2')  
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('plot of x vs y')
plt.grid()
plt.show() 

#checking error
t1=np.zeros(len(t)-1)
dx=np.zeros(len(t1))
dxtrue=np.zeros(len(t1))
dytrue=np.zeros(len(t1))
dy=np.zeros(len(t1))
for i in range(len(t1)):
    t1[i]=(t[i]+t[i+1])/2
    dx[i]=(x[i+1]-x[i])/h
    dy[i]=(y[i+1]-y[i])/h
    dxtrue[i]=e(t1[i],x[i],y[i])
    dx[i]=abs(dx[i]-dxtrue[i])/abs(dxtrue[i])*100
    dytrue[i]=f(t1[i],x[i],y[i])
    dy[i]=abs(dy[i]-dytrue[i])/abs(dytrue[i])*100
    
plt.plot(t1,dx,label='absolute of relative percentage error in y1')
plt.plot(t1,dy,label='absolute of relative percentage error in y2')
plt.title('plotting errors of y1 and y2')
plt.grid()
plt.legend()
plt.show()