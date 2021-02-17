import numpy as np
from numbaWork import work
from plummerModel import plummerModel
from init import Data
import os
from time import time
from tqdm import tqdm

print('creating np saves for iterations...')

t = 10000 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
N = 200
M0 = 2e32
colRad = 1e7
minParticles = 50

pathOfFolder = 'hamData/'
pathOfSave = '/ddn/data/xnlg39/'

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

newP = thinP
newV = thinV
newM = thinM

np.save(pathOfSave + '16-2-21-200p-Myr-position',
        newP)
np.save(pathOfSave + '16-2-21-200p-Myr-velocity',
        newV)
np.save(pathOfSave + '16-2-21-200p-Myr-mass',
        newM)


print('CREATED')
