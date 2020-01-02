import matplotlib.pyplot as plt

plt.axes()

# Draw the ego vehicle
x = 0
y = 0
l = 2
w = 1

x1 = x - w/2
y1 = y - l/2
x2 = x + w/2
y2 = y + l/2

rectangle = plt.Rectangle((x1, y1), x2-x1, y2-y1, fc='white', ec="black")
plt.gca().add_patch(rectangle)
line1 = plt.Line2D((x1,x2), (y1,y2), color='black')
line2 = plt.Line2D((x2,x1), (y1,y2), color='black')
plt.gca().add_line(line1)
plt.gca().add_line(line2)

# Draw the goal rectangle
goal_pts = [[-2,10], [-1,9], [1,9], [2,10]]
polygon = plt.Polygon(goal_pts, ec="black", fc="white", hatch='//')
plt.gca().add_patch(polygon)

plt.axis('scaled')
plt.show()
