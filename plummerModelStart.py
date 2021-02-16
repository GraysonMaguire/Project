import numpy as np
from plummerModel import plummerModel

N = 100
M0 = 2e32
plummerRadius = 1e15

initialV, initialP, initialM = plummerModel(N, M0, plummerRadius)

pathOfFolder = '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/'

np.save(pathOfFolder + '16-2-21-100p-daddy-position',
        initialP)
np.save(pathOfFolder + '16-2-21-100p-daddy-velocity',
        initialV)
np.save(pathOfFolder + '16-2-21-100p-daddy-mass',
        initialM)

print('finished')
