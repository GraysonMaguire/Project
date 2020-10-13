import numpy as np
import display
import work
import init

P = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [0, 0, 0],
])
M = np.array([1, 1, 1, 2])

x = work.forceCalculator(P, M)

print(x)
