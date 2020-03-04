import numpy as np
import matplotlib.pyplot as plt

# circle parameter
# x` = cos(a) + dx
# y` = sin(a) + dy


def xy(dx, yd):
    r = np.arange(0, 2 * np.pi, .001)
    x = (np.cos(r) + dx) / (np.sin(r) + yd)
    y = -1 / (np.sin(r) + yd) + 1
    return x, y


x1, y1 = xy(0, 2)

x2, y2 = xy(0, 6)

x3, y3 = xy(0, 4)

x4, y4 = xy(2, 4)

# draw circle
plt.axis([-1, 3, -2, 1])

plt.scatter(x1, y1, s=1, c='green', alpha=.5)
plt.scatter(x2, y2, s=1, c='red', alpha=.5)
plt.scatter(x3, y3, s=1, c='purple', alpha=.5)
plt.scatter(x4, y4, s=1, c='blue', alpha=.3)
plt.axis('equal')
plt.show()
