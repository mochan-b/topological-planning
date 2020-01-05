from ego import Ego
from goal import Goal
from obstacle import Obstacle
from lane import Lane

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

e = Ego(0, 0, 2, 1, 100)
goal_pts = [[-2,10], [-1,9], [1,9], [2,10],[-2,10]]
g = Goal(goal_pts)
o1 = Obstacle(0, 5, 1, 1, 75)
l1 = Lane(0, 4, 12, 2, 90)

fig = plt.figure()
ax = plt.axes(projection="3d", azim=-90, elev=10)

l1.draw_trajspace(ax)
e.draw_trajspace(ax)
g.draw_trajspace(ax)
o1.draw_trajspace(ax)

plt.show()