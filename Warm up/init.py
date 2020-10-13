import numpy as np


class data:
    N = 2
    V0 = np.array([[0.0, 0.0, 0.0], [0.0, 1000.0, 0.0]])
    P0 = np.array([[0.0, 0.0, 0.0], [385000000.0, 0.0, 0.0]])
    M = np.array([5.9e24, 7.34e22])
    t = 360
    dt = 60
