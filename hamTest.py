import numpy as np
from numbaWork import work
from plummerModel import plummerModel
from init import Data
import os
from time import time
from tqdm import tqdm

t = 100 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
N = 200
M0 = 2e32
colRad = 1e7
minParticles = 50
compressFactor = 100
pathOfFolder = 'hamData/'
pathOfStore = '/ddn/data/xnlg39/'


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


oldP = np.load(
    pathOfFolder + '16-2-21-200p-Myr-position.npy')
oldV = np.load(
    pathOfFolder + '16-2-21-200p-Myr-velocity.npy')
oldM = np.load(
    pathOfFolder + '16-2-21-200p-Myr-mass.npy')

initialM = oldM[-1]
initialP = oldP[-1]
initialV = oldV[-1]

tick = time()

pData, vData, mData = work(
    initialP, initialV, initialM, t, dt, colRad, minParticles)

thinP = thinData(pData, compressFactor)
thinV = thinData(vData, compressFactor)
thinM = thinData(mData, compressFactor)

np.save(pathOfStore + '16-2-21-200p-Myr-position-final',
        thinP)
np.save(pathOfStore + '16-2-21-200p-Myr-velocity-final',
        thinV)
np.save(pathOfStore + '16-2-21-200p-Myr-mass-final',
        thinM)

tock = time()

print('time taken: ', tock - tick)
