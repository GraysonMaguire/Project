import numpy as np
from display import Display
from work import Work
from init import Data
import os

# constants
G = 6.67e-11
# initial data
N = 1000
m = 1e24
R = 1e10
t = 370 * 24 * 60 * 60
dt = 24 * 60 * 60
epsilon = 0
colRad = 1e7
sunMass = 1e30
vMax = np.sqrt(2 * G * sunMass / R)

# app

# currently takes 36~40 mins to run the above params,
# we will see what we can do with multithreading


def App():
    data = Data(R, N, m, t, dt, epsilon, vMax, sunMass)
    P0 = data.P0
    V0 = data.V0
    M = data.M

    worker = Work(P0, V0, t, dt, M, epsilon, colRad)
    dataP, dataV, dataF = worker.numberCruncher()
    # np.save('1', dataP)
    graph = Display(dataP, 0, t, dt, M, R)
    graph.xyAnimation()


App()
