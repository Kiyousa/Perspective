import numpy as np
import matplotlib.pyplot as plt


n = -1
f = -3
u = (1, 0, 0)
v = (0, 0, 1)
w = (0, -1, 0)
e = [0, 0, 1]

# form matrix for perspective
M_p = np.mat([[n, 0, 0, 0],
              [0, n, 0, 0],
              [0, 0, n + f, -f * n],
              [0, 0, 1, 0]])

# form matrix camera 1
M_cam1 = np.mat([np.append(u, 0),
                 np.append(v, 0),
                 np.append(w, 0),
                 [0, 0, 0, 1]])

# form matrix camera 2
i = np.identity(4)
i[3:] = np.append(-np.array(e), 1)

M_cam2 = np.mat(i.T).astype(int)

res = M_p * M_cam1 * M_cam2

# region draw the curve

d1 = 2
d2 = 3
d3 = 4

r = np.arange(0, 2 * np.pi, .01)

x1 = np.cos(r) / (np.sin(r) + d1)
y1 = -1 / (np.sin(r) + d1)

x2 = np.cos(r) / (np.sin(r) + d2)
y2 = -1 / (np.sin(r) + d2)

x3 = np.cos(r) / (np.sin(r) + d3)
y3 = -1 / (np.sin(r) + d3)

# x4 = (np.cos(r) + 2) / (np.sin(r) + d2)
# y4 = -1 / (np.sin(r) + d2)

plt.axis([-1, 1, -1.5, .5])

plt.scatter(x1, y1, s=1, c='green', alpha=.5)
plt.scatter(x2, y2, s=1, c='red', alpha=.5)
plt.scatter(x3, y3, s=1, c='purple', alpha=.5)
# plt.scatter(x4, y4, s=1, c='blue', alpha=.3)

M_p * np.array([0, 5, -1, 1]).reshape(4, 1)