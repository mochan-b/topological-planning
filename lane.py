
import numpy as np
from box import Box


class Lane(Box):
    def __init__(self, x, y, length, width, heading):
        Box.__init__(self, x, y, length, width, heading)
        p1, _, _, p4 = self.rect[0:4]
        self.rect = self.rect

    def draw_map(self, plt):
        Box.draw_map(self, plt, 'grey', fc='lightgrey', draw_arrow=False, alpha=0.4)

    def draw_trajspace(self, ax):
        Xl = self.rect[:, 0][:2]
        #print(Xl)
        Yl = self.rect[:, 1][:2]
        Zl = np.array([[0] * len(Xl), [10] * len(Yl)])
        ax.plot_surface(Xl, Yl, Zl, color='lightgrey', alpha=0.3)
        Xr = self.rect[:, 0][2:4]
        print(Xr)
        Yr = self.rect[:, 1][2:4]
        Zr = np.array([[0] * len(Xr), [10] * len(Yr)])
        ax.plot_surface(Xr, Yr, Zr, color='lightgrey', alpha=0.3)