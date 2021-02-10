import numpy as np
from display import Display
from init import Data
from plummerModel import plummerModel
from numbaWork import work
from tqdm import tqdm
import time

t = 20000 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
N = 150
M0 = 3e32
colRad = 1e7
minParticles = 75
pathOfFolder = '/Users/garymagnum/Project/data/9-2-21-9e13Crunch/'

plummerRadiusArray = np.array(
    [9e13])


def appIteration(plummerRadius):

    initialV, initialP, initialM = plummerModel(N, M0, plummerRadius)

    pData, vData, mData = work(
        initialP, initialV, initialM, t, dt, colRad, minParticles)

    finalP = pData[-1]
    finalV = vData[-1]

    fileName = f'9-2-21-150p-75por20000yr-10d-{plummerRadius}-'

    path = pathOfFolder + fileName

    np.save(path + 'position', pData)
    np.save(path + 'velocity', vData)
    np.save(path + 'masses', mData)

    pass


def App():
    path = pathOfFolder + '9-2-21-150p-75por20000yr-10d-initArray'
    np.save(path, plummerRadiusArray)

    print('plummerRadius array has been saved! starting app...')

    for i in tqdm(range(len(plummerRadiusArray))):
        plummerRadius = plummerRadiusArray[i]
        appIteration(plummerRadius)

    print('App finished its crunch!')

    pass


App()
