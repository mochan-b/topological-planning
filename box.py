
import numpy as np


class Box:
    def __init__(self, x, y, length, width, heading):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.heading = heading
        self.rect = self.calc_rect_at_00() + [x, y]

    def rotate(self, p, angle):
        theta = np.radians(angle)
        c, s = np.cos(theta), np.sin(theta)
        R = np.array([[c, -s], [s, c]])
        return np.matmul(R, p)

    def calc_rect_at_00(self):
        p1 = [self.length/2, self.width/2]
        p2 = [-self.length/2, self.width/2]
        p3 = [-self.length/2, -self.width/2]
        p4 = [self.length/2, -self.width/2]
        p1 = self.rotate(p1, self.heading)
        p2 = self.rotate(p2, self.heading)
        p3 = self.rotate(p3, self.heading)
        p4 = self.rotate(p4, self.heading)
        return np.array([p1, p2, p3, p4, p1])

    def draw_map(self, plt, color, fc = 'white', draw_arrow=False, alpha=1):
        polygon = plt.Polygon(self.rect, fc=fc, ec=color, alpha=alpha)
        plt.gca().add_patch(polygon)
        if draw_arrow:
            [x1, y1], [x2, y2], [x3, y3], [x4, y4] = self.rect[0:4]
            line1 = plt.Line2D((x2, (x4 + x1) / 2), (y2, (y4+y1)/2), color=color, alpha=alpha)
            line2 = plt.Line2D((x3, (x4 + x1) / 2), (y3, (y4 + y1) / 2), color=color, alpha=alpha)
            plt.gca().add_line(line1)
            plt.gca().add_line(line2)
