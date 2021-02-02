import numpy as np
from display import Display
from work import Work
from init import Data
import time
import os


# constants
G = 6.67e-11
# initial data
N = 100
M0 = 1e32
R = 1e14
t = 370 * 24 * 60 * 60
dt = 24 * 60 * 60
epsilon = 0
colRad = 1e7
sunMass = 1e30
vMax = np.sqrt(2 * G * M0 / R)

P = np.load('position.npy')
V = np.load('velocity.npy')
F = np.load('force.npy')
M = np.load('baby/babyM.npy')
PE = np.load('PE.npy')
KE = np.load('KE.npy')

graph = Display(P, V, 0, 1, 1, M, 1e30)

graph.particlesInClusterOverTime()

# worker = Work(P0, V0, t, dt, M, epsilon, colRad)
#
# def function():
#     f1 = worker.calcForceOnParticles(P0, M)
#     # f1 = worker.oldCalcForceOnParticles(P0, M)
#     return f1
# tic = time.time()
# dif = function()
# toc = time.time()
# time = toc - tic
# print(time)
