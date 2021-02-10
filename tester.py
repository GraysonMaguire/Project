import numpy as np
from display import Display
from numba import jit
from work import Work
# from numbaWork import work
from init import Data
from tqdm import tqdm
import time
import os

normal = np.linalg.norm

# constants
G = 6.67e-11
# initial data
N = 100
M0 = 1e32
R = 1e14
t = 20000 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
colRad = 1e7
sunMass = 1e30
vMax = np.sqrt(2 * G * M0 / R)
minParticles = 50
print('loading data')
P = np.load('/Users/garymagnum/Project/data/9-2-21-9e13Crunch/9-2-21-150p-75por20000yr-10d-90000000000000.0-position.npy')
print('finished loading')
M = [0, 0, 0]

E = 0


def reshapeData(data):
    totalSteps = len(data)
    Dimensions = len(data[0][0])
    totalParticles = len(data[0])

    newData = np.full((totalParticles, Dimensions, totalSteps), 0.0)

    for i in tqdm(range(totalSteps)):
        for j in range(Dimensions):
            for k in range(totalParticles):
                newData[k][j][i] = data[i][k][j]

    return newData


P = reshapeData(P)
display = Display(P, E, t, dt, M, R)
display.xyAnimation()
