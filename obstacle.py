
import numpy as np
from box import Box


class Obstacle(Box):
    def __init__(self, x, y, length, width, heading):
        Box.__init__(self, x, y, length, width, heading)
        self.endx = x
        self.endy = y
        self.manifold_angle = heading - 90

    def draw_map(self, plt):
        Box.draw_map(self, plt, 'red', draw_arrow=True)

    def draw_trajspace(self, ax):
        X = self.rect[:, 0]
        Y = self.rect[:, 1]
        Z = np.array([[0] * len(X), [10] * len(Y)])
        ax.plot_surface(X, Y, Z, color='lightcoral', alpha=0.8)

        # Plot the manifold
        p1 = np.array([-10, 0])
        p2 = np.array([10, 0])
        p1 = self.rotate(p1, self.manifold_angle)
        p2 = self.rotate(p2, self.manifold_angle)

        x1 = self.x
        y1 = self.y
        x2 = self.x
        y2 = self.y

        X = np.array([[p1[0]+x1,p2[0]+x1], [p1[0]+x2,p2[0]+x2]])
        Y = np.array([[p1[1]+y1,p2[1]+y1], [p1[1]+y2,p2[1]+y2]])
        Z = np.array([[0,0], [10,10]])
        ax.plot_surface(X, Y, Z, color='lightcoral', alpha=0.3)

