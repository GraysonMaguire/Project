import numpy as np
from display import Display
from work import Work
from init import Data
import os

# constants
G = 6.67e-11
# initial data
N = 100
M0 = 1e32
R = 1e13
t = 370 * 24 * 60 * 60
dt = 24 * 60 * 60
epsilon = 0
colRad = 7e8
sunMass = 1e30
vMax = np.sqrt(2 * G * M0 / R)

# app

# currently takes 36~40 mins to run the above params,
# we will see what we can do with multithreading


def App():
    # data = Data(R, N, M0, t, dt, epsilon, vMax, sunMass)

    # V0, P0, M = data.generateData()

    # P0 = np.load()
    # V0 = data.V0
    # M = data.M

    # np.save('P0', P0)
    # np.save('V0', V0)
    M = np.full(N, sunMass)
    # np.save('M', M)

    P0 = np.load('P0.npy')
    V0 = np.load('V0.npy')

    # worker = Work(P0, V0, t, dt, M, epsilon, colRad)
    # dataP, dataV, dataF = worker.numberCruncher()
    # np.save('testGC', dataP)

    dataP = np.load('testGC.npy')

    graph = Display(dataP, 0, t, dt, M, R)
    graph.xyAnimation()


if __name__ == '__main__':

    App()
