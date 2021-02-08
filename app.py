import numpy as np
from display import Display
from init import Data
from plummerModel import plummerModel
from numbaWork import work
from tqdm import tqdm
import time

t = 2000 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
N = 150
M0 = 3e32
colRad = 1e7
minParticles = 75
pathOfFolder = '/Users/garymagnum/Project/data/8-2-21-testCrunch/'

plummerRadiusArray = np.array(
    [1e9, 1e10, 1e11, 1e12, 1e13, 1e14, 1e15, 1e16, 1e17])


def appIteration(plummerRadius):

    initialV, initialP, initialM = plummerModel(N, M0, plummerRadius)

    pData, vData, mData = work(
        initialP, initialV, initialM, t, dt, colRad, minParticles)

    finalP = pData[-1]
    finalV = vData[-1]

    results = np.array([initialP, initialV, finalP, finalV, mData])

    fileName = f'8-2-21-150p-75por2000yr-10d-{plummerRadius}-results'

    path = pathOfFolder + fileName

    np.save(path, results)

    pass


def App():
    path = pathOfFolder + '8-2-21-150p-75por2000yr-10d-initArray'
    np.save(path, plummerRadiusArray)

    print('plummerRadius array has been saved! starting app...')

    for i in tqdm(range(len(plummerRadiusArray))):
        plummerRadius = plummerRadiusArray[i]
        appIteration(plummerRadius)

    print('App finished its crunch!')

    pass


App()
