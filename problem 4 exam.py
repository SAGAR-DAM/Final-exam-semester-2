''' Problem 4 exam
power spectrum of random data
SAGAR DAM'''

import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(1024)
n=len(data)
h=1
x=np.arange(0,n,1)

#plotting data points
plt.plot(x,data,'ko',markersize=1,label='plotting the random points')
plt.xlabel('x')
plt.ylabel('noise value')
plt.legend()
plt.grid()
plt.title('scatter plot of random points')
plt.show()

#histogram of distribution:
plt.hist(data, density='true', color='y',edgecolor='k',bins=np.arange(0,1+0.05,0.05))
plt.title('histogram of random data points')
plt.show()

#Doing DFT of given data (using numpy package)
k=np.fft.fftshift(np.fft.fftfreq(n,h))
print("k_max= ",np.amax(k))
print("k_min= ",np.amin(k))
gk=abs(np.fft.fftshift(np.fft.fft(data,norm='ortho')))
plt.plot(k,gk,'r',label='DFT')
plt.suptitle('Plotting the DFT of given data')
plt.xlabel('w')
plt.ylabel('g(w)')
plt.legend()
plt.grid()
plt.show()

#power spectrum;  p~A**2
plt.plot(k,gk**2)
plt.xlabel('w')
plt.ylabel('Intensity(w)')
plt.title('power spectrum of random numbers')
plt.legend()
plt.show()

#Binning the power spectrum
b=5
no=int(n/b)
ko=np.fft.fftshift(np.fft.fftfreq(no,h))
hk=np.ones(no*b,dtype=float)
hk=hk.reshape(b,no)
s=np.zeros(no,dtype=float)
h=data[0:no*b].reshape(b,no)
for i in range(5):
    hk[i]=np.fft.fftshift(abs(np.fft.fft(h[i],norm='ortho')))
    s=s+((hk[i])**2)
    plt.plot(ko,s,label='binned power spectrum')
plt.legend()
plt.grid()
plt.title('binned power spectrum')
plt.show()