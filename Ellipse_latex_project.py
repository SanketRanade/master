import numpy as np
import math 
import matplotlib.pyplot as plt
from coeffs1 import *


O = np.array([0,0])
a =3
b =3**0.5 

#Generating points on the circle C1
len = 100
theta = np.linspace(0,2*np.pi,len)
x_elips = np.zeros((2,len))
x_elips[0,:] = a*np.cos(theta)
x_elips[1,:] = b*np.sin(theta)
x_elips = (x_elips.T + O).T


n1 = np.array([(3/(2**0.5)),(3*(1.5**0.5))])
n2 = np.array([3/(2**0.5),(1.5**0.5)])
x_N1 = line_dir_pt(n1,n2,-1.7,1)


n3 = np.array([(-3/(2**0.5)),(3*(1.5**0.5))])
n4 = np.array([-3/(2**0.5),(1.5**0.5)])
x_N2 = line_dir_pt(n3,n4,-1.7,1)

#Plotting all lines
plt.plot(x_N1[0,:],x_N1[1,:],label='$N_1$')
plt.plot(x_N2[0,:],x_N2[1,:],label='$N_2$')

plt.plot(n2[0], n2[1], 'o')
plt.text(n2[0] * (1 + 0.1), n2[1] * (1 - 0.1) , 'P')
plt.plot(n4[0], n4[1], 'o')
plt.text(n4[0] * (1 - 0.1), n4[1] * (1-0.2) , 'Q')



plt.plot(x_elips[0,:],x_elips[1,:],label='$ELLIPSE$')

plt.xlabel('$x$');plt.ylabel('$y$')
plt.grid()
plt.legend(loc='best')
plt.axis('equal')
plt.show()

