
import numpy as np
from box import Box


class Ego(Box):

    def draw_map(self, plt):
        Box.draw_map(self, plt, 'blue', draw_arrow=True)

    def draw_trajspace(self, ax):
        X = self.rect[:, 0]
        Y = self.rect[:, 1]
        Z = np.array([[0] * len(X), [1 / 2] * len(Y)])
        ax.plot_surface(X, Y, Z, color='lightblue', alpha=0.8)
