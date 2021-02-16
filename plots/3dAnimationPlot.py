from matplotlib import pyplot as plt
from matplotlib import animation
from display import Display
import numpy as np
from tqdm import tqdm

R = 1e14
P = np.load(
    '/Users/garymagnum/Project/data/11-2-21-9e13BabyCrunch/11-2-21-100p-50por100yr-10d-9e13-position.npy')
E = 0
M = 100
t = 100 * 370 * 24 * 60 * 60
compressFactor = 100
dt = 10 * 24 * 60 * 60 * compressFactor
year = 365.25 * 24 * 60 * 60


def reshapeData(data):
    totalSteps = len(data)
    totalParticles = len(data[0])
    Dimensions = len(data[0][0])

    newData = np.full((totalParticles, Dimensions, totalSteps), 0.0)

    for i in tqdm(range(totalSteps)):
        for j in range(Dimensions):
            for k in range(totalParticles):
                newData[k][j][i] = data[i][k][j]

    return newData


P = reshapeData(P)
display = Display(P, E, t, dt, M, R)
display.xyAnimation()