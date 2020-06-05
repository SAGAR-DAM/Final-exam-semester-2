'''problem 10 code 2
plotting of FT of box for 3 different sapling rate
SAGAR DAM;  DNAP'''

'''
DUE TO 3 DIFFERENT PLOTS, THIS CODE TAKES LONGER TIME THAN JUST THE 
PLOTTING OF FT OF BOX LIKE PREVIOUS CODE OF PROBLEM 10. HENCE I HAVE MADE THS DIFFERENT
CODE. FOR TRILING I HAD TO RUN THE PREVIOUS CODE SEVERAL TIMES. IF I PLOTTED THREE IN SAME 
CODE THEN THAT TRILING WOULD TAKE A LONGER TIME. HENCE I HAVE DONE THIS

I THINK THIS CODE IS NOT SO IMPORTENT. I HAVE JUST RAN THE PREVIOUS CODE 3 TIMES
IN THIS ONE AT A TIME. 
'''

import numpy as np
import matplotlib.pyplot as plt

#initializing variables
a=100
r=[0.090,0.1,0.11]

for q in range(3):
    h=r[q]
    #defining box function
    def f(x):
        if(abs(x)<=1):
            z=1
        else:
                z=0
        return z

    #taking arrays for FT
    x=np.arange(-a,a+h,h)
    X=np.ones(len(x))
    W=np.zeros(len(x),dtype=complex)
    for i in range(len(x)):
        X[i]=f(x[i])
    
    N=int(len(x))
    freq=np.zeros(N)
    kmin=-np.pi*(N-1)/(h*N)

    #taking frequency points
    for j in range(len(x)):
        freq[j]=kmin+j*2*np.pi/(h*N)

    #doing fourier transform
    for i in range(len(x)-1):
        for k in range(len(x)-1):
            W[i]=W[i]+(X[k]*np.exp(-complex(0,1)*freq[i]*x[k]))
        W[i]=W[i]/np.sqrt(N/np.pi)
    if(q==0):
        plt.plot(freq,W,label='numerical FT with spacing at real space=0.090')
    elif(q==1):
        plt.plot(freq,W,label='numerical FT with spacing at real space=0.100')
    else:
        plt.plot(freq,W,label='numerical FT with spacing at real space=0.110')
        
'''#creating true (analytic) FT of box. i.e sinc
w=np.arange(-10,10,0.1)
sinc=np.zeros(len(w))
box=np.zeros(len(w))
def true(t):
    if(t!=0):
        z=np.sin(t)/t
    else:
        z=1
    return z*np.sqrt(2/np.pi)'''
w=np.arange(-10,10,0.1)
box=np.zeros(len(w))
for j in range(len(w)):
#    sinc[j]=true(w[j])
    box[j]=f(w[j])

#plotting box function, numerical FT of box function and true FT of box (sinc)    
#plt.plot(freq,W,label='numerical FT')
#plt.plot(w,sinc,'ro',markersize='2',label='analytic FT (true sinc function)')
plt.plot(w,box,'k',label='box function')
plt.gca().set_xlim(-10,10)
plt.title('plotting FT of box function for 3 different sampling rates')
plt.legend()
plt.grid()
plt.show()