from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

from ego import Ego
from goal import Goal
from obstacle import Obstacle

e = Ego(0, 0, 90, 2, 1)
goal_pts = [[-2,10], [-1,9], [1,9], [2,10],[-2,10]]
g = Goal(goal_pts)
o1 = Obstacle(0, 5, 90, 1, 1)

fig = plt.figure()
plt.axes()

plt.subplot(1, 2, 1)
e.draw_map(plt)
g.draw_map(plt)
o1.draw_map(plt)
plt.axis('scaled')
plt.title('Map')
plt.ylabel('x')
plt.ylabel('y')

ax = fig.add_subplot(1, 2, 2, projection="3d", azim=-90, elev=10)
e.draw_trajspace(ax)
g.draw_trajspace(ax)
o1.draw_trajspace(ax)
plt.xlabel('x')
plt.ylabel('y')

plt.show()