import numpy as np
from plummerModel import plummerModel

N = 100
M0 = 2e32
plummerRadius = 1e15

initialV, initialP, initialM = plummerModel(N, M0, plummerRadius)

pathOfFolder = '/Users/garymagnum/Project/data/23-2-21-MyrCrunchHam/'

np.save(pathOfFolder + '23-2-21-100p-baby-position',
        np.array([initialP]))
np.save(pathOfFolder + '23-2-21-100p-baby-velocity',
        np.array([initialV]))
np.save(pathOfFolder + '23-2-21-100p-baby-mass',
        np.array([initialM]))

initialV, initialP, initialM = plummerModel(N, M0, plummerRadius)

np.save(pathOfFolder + '23-2-21-100p-daddy-position',
        np.array([initialP]))
np.save(pathOfFolder + '23-2-21-100p-daddy-velocity',
        np.array([initialV]))
np.save(pathOfFolder + '23-2-21-100p-daddy-mass',
        np.array([initialM]))

print('finished')
