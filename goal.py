
import numpy as np

class Goal:
    def __init__(self, goal_poly):
        if goal_poly[0] != goal_poly[-1]:
            goal_poly.append(goal_poly[0])
        self.goal_poly = np.array(goal_poly)

    def draw_map(self, plt):
        polygon = plt.Polygon(self.goal_poly, ec="green", fc="white", hatch='//')
        plt.gca().add_patch(polygon)

    def draw_trajspace(self, ax):
        X = self.goal_poly[:, 0]
        Y = self.goal_poly[:, 1]
        Z = np.array([[0] * len(X), [10] * len(Y)])
        ax.plot_surface(X, Y, Z, color='lightgreen', alpha=0.8)