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

M = cv2.getPerspectiveTransform(pst1, pst2)
