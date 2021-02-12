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
N = 100
M0 = 2e32
colRad = 1e7
minParticles = 50
pathOfFolder = '/Users/garymagnum/Project/data/12-2-21-2e14BabyCrunch/'
plummerRadius = 9e13
compressFactor = 100

finalLength = 37000 * 2


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

    initialM = np.load(pathOfFolder + 'babyM0.npy')
    initialP = np.load(pathOfFolder + 'babyP0.npy')
    initialV = np.load(pathOfFolder + 'babyV0.npy')

    pData, vData, mData = work(
        initialP, initialV, initialM, t, dt, colRad, minParticles)

    thinP = thinData(pData, compressFactor)
    thinV = thinData(vData, compressFactor)
    thinM = thinData(mData, compressFactor)

    oldP = np.load(
        pathOfFolder + '12-2-21-100p-50por100000yr-10d-2e14-position.npy')
    oldV = np.load(
        pathOfFolder + '12-2-21-100p-50por100000yr-10d-2e14-velocity.npy')
    oldM = np.load(
        pathOfFolder + '12-2-21-100p-50por100000yr-10d-2e14-mass.npy')

    newP = np.concatenate((oldP[:-1], thinP))
    newV = np.concatenate((oldV[:-1], thinV))
    newM = np.concatenate((oldM[:-1], thinM))

    print('saving...')

    np.save(pathOfFolder + '12-2-21-100p-50por100000yr-10d-2e14-position',
            newP)
    np.save(pathOfFolder + '12-2-21-100p-50por100000yr-10d-2e14-velocity',
            newV)
    np.save(pathOfFolder + '12-2-21-100p-50por100000yr-10d-2e14-mass',
            newM)

    np.save(pathOfFolder + 'babyM0', newM[-1])
    np.save(pathOfFolder + 'babyP0', newP[-1])
    np.save(pathOfFolder + 'babyV0', newV[-1])

    print('saved successfully')

    return len(newM)


length = 0
tick = time()
iterations = 0

while length <= finalLength:

    length = App()
    iterations += 1
    tock = time()
    print('current length: ', length)
    print('current iteration: ', iterations)
    print('time taken: ', tock - tick)
