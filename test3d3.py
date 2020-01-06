
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
import random

fig = plt.figure()
ax = plt.axes(projection="3d")

X = np.array([[0,1], [0,1]])
Y = np.array([[0,0], [1,1]])
Z = np.array([[1,1], [1,1]])
ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.8)

# x = np.array([[1, 3], [2, 4]])
# y = np.array([[5, 6], [7, 8]])
# z = np.array([[9, 12], [10, 11]])
# ax.plot_surface(x, y, z)

ax.set(xlabel='x', ylabel='y', zlabel='z')
plt.show()