
class Ego:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def draw_map(self, plt):
        x1 = self.x - self.width / 2
        y1 = self.y - self.length / 2
        x2 = self.x + self.width / 2
        y2 = self.y + self.length / 2

        rectangle = plt.Rectangle((x1, y1), x2 - x1, y2 - y1, fc='white', ec="black")
        plt.gca().add_patch(rectangle)
        line1 = plt.Line2D((x1, x2), (y1, y2), color='black')
        line2 = plt.Line2D((x2, x1), (y1, y2), color='black')
        plt.gca().add_line(line1)
        plt.gca().add_line(line2)

    def draw_trajspace(self):
        pass
