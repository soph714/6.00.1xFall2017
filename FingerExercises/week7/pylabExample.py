# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:52:53 2018

@author: Ted
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

    
plt.figure('lin')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.title('Linear')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.xlabel('sample points')
plt.ylabel('quad function')
plt.title('Quadratic')
plt.plot(mySamples, myQuadratic)

plt.figure('cube')
plt.xlabel('sample points')
plt.ylabel('cube function')
plt.title('Cubic')
plt.plot(mySamples, myCubic)

plt.figure('expo')
plt.xlabel('sample points')
plt.ylabel('expo function')
plt.title('Exponential')
plt.plot(mySamples, myExponential)



plt.figure('lin')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0,1000)
plt.plot(mySamples, myQuadratic)
plt.figure('lin')
plt.title('Lnear')
plt.figure('quad')
plt.title('Quadratic')

plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0,900)
plt.plot(mySamples, myLinear, 'b-',label = 'linear', linewidth = 2.0)
plt.subplot(212)
plt.ylim(0,900)
plt.plot(mySamples, myQuadratic, 'ro' , label = 'quad', linewidth = 3.0)
plt.legend()
plt.title('lin vs quad')

plt.figure('cube exp log')
plt.clf()
# plt.subplot(121)
# plt.ylim(0,140000)
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0)
# plt.subplot(122)
# plt.ylim(0,140000)
plt.plot(mySamples, myExponential, 'r--', label = 'exp', linewidth = 6.0)
plt.yscale('log')
plt.legend()
plt.title('cube vs exp')













