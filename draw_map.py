
import matplotlib.pyplot as plt

from ego import Ego
from goal import Goal
from obstacle import Obstacle
from lane import Lane

e = Ego(0, 0, 2, 1, 100)
l1 = Lane(0, 4, 12, 2, 90)
goal_pts = [[-2,10], [-1,9], [1,9], [2,10],[-2,10]]
g = Goal(goal_pts)
o1 = Obstacle(0.5, 5, 1, 0.5, 75)

plt.axes()

l1.draw_map(plt)
e.draw_map(plt)
g.draw_map(plt)
o1.draw_map(plt)

plt.axis('scaled')
plt.show()