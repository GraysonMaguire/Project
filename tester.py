import numpy as np
from display import Display
from numba import jit
from work import Work
from numbaWork import work
from init import Data
import time
import os

normal = np.linalg.norm

# constants
G = 6.67e-11
# initial data
N = 100
M0 = 1e32
R = 1e14
t = 370 * 24 * 60 * 60
dt = 24 * 60 * 60
colRad = 1e7
sunMass = 1e30
vMax = np.sqrt(2 * G * M0 / R)

P0 = np.load('baby/babyP0.npy')
V0 = np.load('baby/babyV0.npy')
M0 = np.load('baby/babyM.npy').flatten()

tick = time.time()
pData, vData, mData = work(P0, V0, t, dt, M0, colRad)
tock = time.time()


def reshapeData(data):
    totalSteps = len(data)
    Dimensions = len(data[0][0])
    totalParticles = len(data[0])

    newData = np.full((totalParticles, Dimensions, totalSteps), 0.0)

    for i in (range(totalSteps)):
        for j in range(Dimensions):
            for k in range(totalParticles):
                newData[k][j][i] = data[i][k][j]

    return newData


np.save('numbaP', reshapeData(pData))
np.save('numbaV', vData)
# newPData = np.load('numbaP.npy')
# # newMData = np.load('numbaM.npy')
oldPData = np.load('data/30-1-21-150p-2000y-10d-baby-position.npy')
# oldMData = np.load('M.npy')
#
#
# print(newPData)
# print(oldMData)
display1 = Display(reshapeData(pData), 0, t, dt, M0, R)
display2 = Display((oldPData), 0, t, dt, M0, R)
display1.xyAnimation()
display2.xyAnimation()
