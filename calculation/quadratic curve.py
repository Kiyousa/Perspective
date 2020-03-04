import sympy as sy
import cv2
import numpy as np

# Another way to compute projective matrix
A = np.array([0, 0])
a = np.array([0, -1])
B = np.array([-1, 1])
b = np.array([-1 / 2, -1 / 2])
C = np.array([1, 1])
c = np.array([1 / 2, -1 / 2])
D = np.array([0, 3])
d = np.array([0, -1 / 4])

pst1 = np.float32([A, B, C, D])
pst2 = np.float32([a, b, c, d])

H = cv2.getPerspectiveTransform(pst1, pst2)

a, b, c, d, e, f = sy.symbols('a b c d e f')

C = sy.Matrix([[a, c/2, d/2],
               [c/2, b, e/2],
               [d/2, e/2, f]])


C = C.subs({a: 1, b: 1, c: 0, d: 0, e: -2, f: 0})


H = sy.Matrix(H.astype(int))  # H.astype(int) 'Cuz I know all the elements in H must be integer, if not don't do this
Cp = H.inverse_GE().T * C * H.inverse_GE()

print(Cp)
