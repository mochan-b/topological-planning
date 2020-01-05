from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection="3d", azim=-90, elev=10)


goal_pts = np.array([[-2, 10], [-1, 9], [1, 9], [2, 10], [-2, 10]])
X = goal_pts[:, 0]
Y = goal_pts[:, 1]
Z = np.array([[0]*len(X),[10]*len(Y)])

#ax.plot_wireframe(X, Y, Z, color='brown', alpha=0.8)
ax.plot_surface(X, Y, Z, color='lightgreen', alpha=0.8)


ego_pts = np.array([[1/2, 1/2], [-1/2, 1/2], [-1/2, -1/2], [1/2, -1/2], [1/2, 1/2]])
X1 = ego_pts[:, 0]
Y1 = ego_pts[:, 1]
Z1 = np.array([[0]*len(X1),[1/2]*len(Y1)])
ax.plot_surface(X1, Y1, Z1, color='lightblue', alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('t')

plt.show()