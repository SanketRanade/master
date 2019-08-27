from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from funcs import *
import numpy as np
from coeffs1 import *


#creating x,y for 3D plotting
len = 50
xx, yy = np.meshgrid(range(len), range(len))
xx=xx
yy=-yy
#setting up plot
fig = plt.figure()
ax = fig.gca(projection='3d')
#print ('xx',xx)


A = np.array([8,-6,0])
B = np.array([5.5,-1,-6])
C = np.array([0,0,0])
D = np.array([2.5,-5,6])


#defining planes
n1 = np.array([36,48,25]).reshape((3,1))
c1 = 0

#corresponding z for planes
z1 = ((c1-n1[0]*xx-n1[1]*yy)*1.0)/(n1[2])


#plotting planes
ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)


#plotting point
ax.scatter(A[0],A[1],A[2],'o',label="Point A")
ax.scatter(B[0],B[1],B[2],'o',label="Point B")
ax.scatter(C[0],C[1],C[2],'o',label="Point C")
ax.scatter(D[0],D[1],D[2],'o',label="Point D")


plt.plot([A[0],B[0]],[A[1],B[1]],[A[2],B[2]],label="Line $AB$")
plt.plot([B[0],C[0]],[B[1],C[1]],[B[2],C[2]],label="Line $BC$")
plt.plot([C[0],D[0]],[C[1],D[1]],[C[2],D[2]],label="Line $CD$")
plt.plot([D[0],A[0]],[D[1],A[1]],[D[2],A[2]],label="Line $AD$")
plt.plot([A[0],C[0]],[A[1],C[1]],[A[2],C[2]],label="Line $AC$")
plt.plot([B[0],D[0]],[B[1],D[1]],[B[2],D[2]],label="Line $BD$")

ax.plot_surface(xx, yy, z1, color='r',alpha=0.2)

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()
