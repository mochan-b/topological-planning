
class Goal:
    def __init__(self, goal_poly):
        self.goal_poly = goal_poly

    def draw_map(self, plt):
        polygon = plt.Polygon(self.goal_poly, ec="black", fc="white", hatch='//')
        plt.gca().add_patch(polygon)

    def draw_trajspace(self):
        pass