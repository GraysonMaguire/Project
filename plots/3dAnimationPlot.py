from matplotlib import pyplot as plt
from matplotlib import animation
from display import Display
import numpy as np
from tqdm import tqdm

R = 1e14
P = np.load(
    '/Users/grays/Project/Data/23-2-21-200p-Myr-position.npy')
E = 0
M = 100
t = 100000 * 370 * 24 * 60 * 60
compressFactor = 100
dt = 10 * 24 * 60 * 60 * compressFactor
t = len(P)*dt
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
