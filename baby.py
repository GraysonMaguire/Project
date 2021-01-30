import numpy as np
from display import Display
from work import Work
from init import Data
import os
import time

# constants
G = 6.67e-11
# initial data
N = 100
M0 = 1e32
R = 1e15
t = 2000 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
epsilon = 0
colRad = 7e8
sunMass = 1e30
vMax = np.sqrt(2 * G * M0 / R)


def App():

    P0 = np.load('baby/babyP0.npy')
    V0 = np.load('baby/babyV0.npy')
    M = np.load('baby/babyM.npy')

    tick = time.time()

    worker = Work(P0, V0, t, dt, M, epsilon, colRad)

    dataP, dataV, dataF = worker.numberCruncher()

    np.save('30-1-21-150p-2000y-10d-baby-position', dataP)
    np.save('30-1-21-150p-2000y-10d-baby-velocity', dataV)
    np.save('30-1-21-150p-2000y-10d-baby-force', dataF)

    tock = time.time()
    print(f'completed in:{tock - tick}')
    # dataP = np.load('29-1-21-100p-2000y-10d-baby.npy')
    #
    # graph = Display(dataP, 0, t, dt, M, R)
    # graph.xyAnimation()


if __name__ == '__main__':

    App()
