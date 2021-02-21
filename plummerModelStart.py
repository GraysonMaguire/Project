import numpy as np
from plummerModel import plummerModel

N = 100
M0 = 2e32
plummerRadius = 1e16

initialV, initialP, initialM = plummerModel(N, M0, plummerRadius)

pathOfFolder = '/Users/garymagnum/Project/data/19-2-21-e16Crunch/'

np.save(pathOfFolder + '16-2-21-100p-baby-position',
        np.array([initialP]))
np.save(pathOfFolder + '16-2-21-100p-baby-velocity',
        np.array([initialV]))
np.save(pathOfFolder + '16-2-21-100p-baby-mass',
        np.array([initialM]))

print('finished')
