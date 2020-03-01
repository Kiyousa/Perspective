from scipy import linalg
import numpy as np
import sympy

# region points used for determining the projective matrix
# all the points are writen in homogeneous coordinates
A = np.array([0, 0, 1])
a = np.array([0, -1, 1])
B = np.array([-1, 1, 1])
b = np.array([-1 / 2, -1 / 2, 1])
C = np.array([1, 1, 1])
c = np.array([1 / 2, -1 / 2, 1])
D = np.array([0, 2, 1])
d = np.array([0, -1 / 3, 1])
# endregion

x, y = sympy.symbols('x y')
m0, m1, m2, m3, m4, m5, m6, m7 = sympy.symbols('m0 m1 m2 m3 m4 m5 m6 m7')
u, v = sympy.symbols('u v')

cof = m0, m1, m2, m3, m4, m5, m6, m7

expr_x = u * m0 + v * m1 - x * u * m6 - x * v * m7 - x + m2
expr_y = u * m3 + v * m4 - y * u * m6 - y * v * m7 - y + m5

eqs = []  # form linera equations system

for p in [(A, a), (B, b), (C, c), (D, d)]:
    eqs.append(expr_x.subs({u: p[0][0], v: p[0][1], x: p[1][0], y: p[1][1]}))
    eqs.append(expr_y.subs({u: p[0][0], v: p[0][1], x: p[1][0], y: p[1][1]}))

A_, B_ = sympy.linear_eq_to_matrix(eqs, cof)  # get the linear equation system coefficient matrix

solution = linalg.solve(np.mat(A_, float), np.array(B_, float))  # solve for the projective matrix

pro = np.mat(np.append(solution, [1]).reshape(3, 3))

print(pro)

# Verification
print("Points in xy plane by project:")
for j in [i.reshape(3, 1) for i in [A, B, C, D]]:
    v = np.array(pro * j).reshape(3)
    v = (v / v[2])
    print(v)

print("\nOrigin points on xy plane:")
for i in [a, b, c, d]:
    print(i)
