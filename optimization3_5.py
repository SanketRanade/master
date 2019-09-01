import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#Plotting the circle
x = 8*np.ones(8)
y = 6*np.ones(8)
r = np.arange(8)/np.sqrt(2)
phi = np.linspace(0.0,2*np.pi,100)
na=np.newaxis
# the first axis of these arrays varies the angle, 
# the second varies the circles
x_line = x[na,:]+r[na,:]*np.sin(phi[:,na])
y_line = y[na,:]+r[na,:]*np.cos(phi[:,na])
ax=plt.plot(x_line,y_line,'-')

#Plotting the line
x1 = np.linspace(0,10,100)
x2 = 9*np.ones(100) - x1
bx=plt.plot(x1,x2,label="$x_1+x_2-9=0$")
plt.axis('equal')
plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend([ax[5], bx[0]],['$(x_1-8)^2+(x_2- 6)^2=\\frac{25}{2}$','$x_1+x_2-9=0$'], loc='best')

print(x)
print(y)
print(r)

O = np.array([8,6])

m1 = np.array([1,1])
m2 = np.array([1,-1])


N = np.vstack((m1,m2))
q = np.zeros(2)

q[0] = 9
q[1] = 2

P = np.linalg.inv(N)@q

x_OP = line_gen(O,P)

plt.plot(x_OP[0,:],x_OP[1,:], label='$OP$')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.05), P[1] * (1 - 0.03) , 'P')
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0), O[1] * (1 + 0.03) , 'O')

print(P)

#plt.savefig('../figs/2.1.eps')
plt.show()
