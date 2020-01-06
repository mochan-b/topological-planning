from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

from ego import Ego
from goal import Goal
from obstacle import Obstacle
from lane import Lane

e = Ego(0, 0, 2, 1, 100)
goal_pts = [[-2,10], [-1,9], [1,9], [2,10],[-2,10]]
g = Goal(goal_pts)
o1 = Obstacle(0, 5, 0.5, 0.5, 75)
l1 = Lane(0, 4, 12, 2, 90)
#l2 = Lane(-2, 4, 12, 2, 90)

fig = plt.figure()
plt.axes()

plt.subplot(1, 2, 1)
l1.draw_map(plt)
#l2.draw_map(plt)
e.draw_map(plt)
g.draw_map(plt)
o1.draw_map(plt)
plt.axis('scaled')
plt.title('Map')
plt.xlabel('x')
plt.ylabel('y')

ax = fig.add_subplot(1, 2, 2, projection="3d", azim=-90, elev=10)
l1.draw_trajspace(ax)
#l2.draw_trajspace(ax)
e.draw_trajspace(ax)
g.draw_trajspace(ax)
o1.draw_trajspace(ax)

ax.set(xlabel='x', ylabel='y', zlabel='t', title="Trajectory Space")
ax.set_xlim3d([-5.0, 5.0])

plt.show()