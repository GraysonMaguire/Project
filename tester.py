import numpy as np
# from display import Display
# from numba import jit
# from work import Work
from numbaWork import work
# from init import Data
# from tqdm import tqdm
from time import time
# import os

normal = np.linalg.norm

# constants
G = 6.67e-11
# initial data
N = 100
M0 = 1e32
R = 1e14
t = 10000 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
colRad = 1e7
sunMass = 1e30
vMax = np.sqrt(2 * G * M0 / R)
minParticles = 50
compressFactor = 100

print('loading data')
P = np.load('/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-position.npy')
M = np.load('/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-mass.npy')
V = np.load('/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-velocity.npy')
print('finished loading')

def thinData(data, compress):
    shape = list(np.shape(data))
    oldLength = shape[0]

    if oldLength <= compress:
        return data

    newLength = int(oldLength / compress)
    shape[0] = newLength

    newShape = tuple(shape)

    newData = np.full((newShape), 0.0)

    for i in range(newLength):
        newData[i] = data[i * compress]

    return newData
tick = time()
initialM = M[-1]
initialP = P[-1]
initialV = V[-1]

pData, vData, mData = work(
    initialP, initialV, initialM, t, dt, colRad, minParticles)

thinP = thinData(pData, compressFactor)
thinV = thinData(vData, compressFactor)
thinM = thinData(mData, compressFactor)

newP = np.concatenate((P[:-1], thinP))
newV = np.concatenate((V[:-1], thinV))
newM = np.concatenate((M[:-1], thinM))

# np.save(pathOfFolder + date + '200p-Myr-position',
#         newP)
# np.save(pathOfFolder + date + '200p-Myr-velocity',
#         newV)
# np.save(pathOfFolder + date + '200p-Myr-mass',
#         newM)

print('Saved')
tock = time()

print('time taken: ',tock-tick)
