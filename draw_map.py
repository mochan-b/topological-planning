
from ego import Ego
from goal import Goal

import matplotlib.pyplot as plt

plt.axes()

e = Ego(0,0,2,1)
goal_pts = [[-2,10], [-1,9], [1,9], [2,10]]
g = Goal(goal_pts)
e.draw_map(plt)
g.draw_map(plt)

plt.axis('scaled')
plt.show()