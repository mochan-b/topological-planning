
import numpy as np
from box import Box


class Obstacle(Box):

    def draw_map(self, plt):
        Box.draw_map(self, plt, 'red', draw_arrow=True)

    def draw_trajspace(self, ax):
        X = self.rect[:, 0]
        Y = self.rect[:, 1]
        Z = np.array([[0] * len(X), [10] * len(Y)])
        ax.plot_surface(X, Y, Z, color='lightcoral', alpha=0.8)
