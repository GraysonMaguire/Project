import numpy as np
from numbaWork import work
from plummerModel import plummerModel
from init import Data
import os
import time
from tqdm import tqdm

# initial data
t = 100 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
N = 100
M0 = 2e32
colRad = 1e7
minParticles = 50
pathOfFolder = '/Users/garymagnum/Project/data/11-2-21-9e13BabyCrunch/'
plummerRadius = 9e13
compressFactor = 100


def compressData(data, compress):
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


def App():

    initialV, initialP, initialM = plummerModel(N, M0, plummerRadius)

    pData, vData, mData = work(
        initialP, initialV, initialM, t, dt, colRad, minParticles)

    np.save(pathOfFolder + '11-2-21-100p-50por100yr-10d-9e13-position',
            compressData(pData, compressFactor))
    np.save(pathOfFolder + '11-2-21-100p-50por100yr-10d-9e13-velocity',
            compressData(vData, compressFactor))
    np.save(pathOfFolder + '11-2-21-100p-50por100yr-10d-9e13-mass',
            compressData(mData, compressFactor))


App()
