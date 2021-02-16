import numpy as np
from numbaWork import work
from plummerModel import plummerModel
from init import Data
import os
from time import time
from tqdm import tqdm

# initial data
t = 1000 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
N = 200
M0 = 2e32
colRad = 1e7
minParticles = 50
pathOfFolder = '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/'
compressFactor = 100

year1000 = 370
finalLength = 100 * year1000


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


def stitchDataTogether(data, addData):
    return np.concatenate((data[:-1], addData))


def App():

    oldP = np.load(
        pathOfFolder + '16-2-21-200p-Myr-position.npy')
    oldV = np.load(
        pathOfFolder + '16-2-21-200p-Myr-velocity.npy')
    oldM = np.load(
        pathOfFolder + '16-2-21-200p-Myr-mass.npy')

    initialM = oldM[-1]
    initialP = oldP[-1]
    initialV = oldV[-1]

    pData, vData, mData = work(
        initialP, initialV, initialM, t, dt, colRad, minParticles)

    thinP = thinData(pData, compressFactor)
    thinV = thinData(vData, compressFactor)
    thinM = thinData(mData, compressFactor)

    newP = np.concatenate((oldP[:-1], thinP))
    newV = np.concatenate((oldV[:-1], thinV))
    newM = np.concatenate((oldM[:-1], thinM))

    print('saving...')

    np.save(pathOfFolder + '16-2-21-200p-Myr-position',
            newP)
    np.save(pathOfFolder + '16-2-21-200p-Myr-velocity',
            newV)
    np.save(pathOfFolder + '16-2-21-200p-Myr-mass',
            newM)

    print('saved successfully')

    return len(newM)


length = 0


pbar = tqdm(total=finalLength)

while length <= finalLength:
    length = App()
    pbar.update(length)
