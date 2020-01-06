
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

        X1 = np.array([X[0:2], X[2:4][::-1]])
        Y1 = np.array([Y[0:2], Y[2:4][::-1]])
        Z1 = np.array([[1/2] * 2, [1 / 2] * 2])
        ax.plot_surface(X1, Y1, Z1, color='lightblue', alpha=0.8)
        Z2 = np.array([[0] * 2, [0] * 2])
        ax.plot_surface(X1, Y1, Z2, color='lightblue', alpha=0.8)
