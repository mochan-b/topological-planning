
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
import random


def rotate(p, angle):
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])
    return np.matmul(R, p)


fig = plt.figure()
ax = plt.axes(projection="3d")

heading = 45

p1 = np.array([-10, 0])
p2 = np.array([10, 0])
p1 = rotate(p1, heading)
p2 = rotate(p2, heading)
x_line = [p1[0], p2[0]]
y_line = [p1[1],p2[1]]
z_line = [0,0]
#ax.plot3D(x_line, y_line, z_line, 'gray')

x1 = 2
y1 = 1
x2 = 2
y2 = 5

X = np.array([[p1[0]+x1,p2[0]+x1], [p1[0]+x2,p2[0]+x2]])
Y = np.array([[p1[1]+y1,p2[1]+y1], [p1[1]+y2,p2[1]+y2]])
Z = np.array([[0,0], [10,10]])
ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.8)

x_line = [x1, x2]
y_line = [y1, y2]
z_line = [0, 10]
ax.plot3D(x_line, y_line, z_line, 'red')

ax.set(xlabel='x', ylabel='y', zlabel='z')
plt.show()