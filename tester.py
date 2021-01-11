import numpy as np
from display import Display
from work import Work
from init import Data
import time


# constants
G = 6.67e-11
# initial data
N = 30000
m = 1e24
R = 1e10
t = 370 * 24 * 60 * 60
dt = 24 * 60 * 60
epsilon = 0
colRad = 1e7
sunMass = 1e30
vMax = np.sqrt(2 * G * sunMass / R)
# 3secs to do 100particles with multiprocessing
# dnf for 10000 Particles

# 0.07s for 100 particles with no multiprocessing

# new pool process seeems to have time of 0.85 for both 100 and 1000 particles
# 10000 in 4.76 seconds

if __name__ == '__main__':
    data = Data(R, N, m, t, dt, epsilon, vMax, sunMass)

    P0 = data.P0
    V0 = data.V0
    M = data.M

    # P0 = np.load('P0.npy')
    # V0 = np.load('V0.npy')
    # M = np.load('M.npy')

    worker = Work(P0, V0, t, dt, M, epsilon, colRad)

    def function():
        f1 = worker.calcForceOnParticles(P0, M)
        # f2 = worker.oldCalcForceOnParticles(P0, M)
        return f1
    tic = time.time()
    dif = function()
    toc = time.time()
    time = toc - tic
    print(time)

#
# newP, newV, newF = worker.numberCruncher()
#
#
# graph = Display(newP, 0, t, dt, M)
#
#
# # graph.display()
# graph.xyAnimation()
# print('Fs:', newF)
# print('Ps:', newP)
# print('Vs:', newV)

#
# P, V, F, E = worker.numberCruncher()
#
# print(worker.numberCruncher())

# r = range(0, 3600, int(3600 / 60))
# for i in r:
#     print(i)
# test gForce

# test calcForceOnParticles
# print(workTest.calcForceOnParticles(data.P0, data.M))

# test calcNextPosition
# P, Phalf = workTest.calcNextPosition(data.P0, data.V0)

# # test calcNextVelocity
# workTest.calcNextVelocity(
#     data.V0, workTest.calcForceOnParticles(data.P0, data.M), data.M)

# test calcCOM
# com = workTest.calcCOM(data.P0, data.M)
# print(com)

# # test calcPE
# pe = workTest.calcPE(
#     data.P0, data.M, workTest.calcForceOnParticles(data.P0, data.M))

# test calcKE
# ke = workTest.calcKE(data.V0, data.M)
# print(ke)

# def otherCalc():
#     p = data.P0
#     M = data.M
#     PE = -workTest.G * M[0] * M[1] / (np.linalg.norm(p[0] - p[1]))
#     return PE
# print(otherCalc() / (pe[0] + pe[1]))

# test numberCruncher


#
# display = Display(P, E, data.t, data.dt, data.M)
# display.display()

# dataP = np.full(
#     (10, len(data.M), 3), 0.0)
# dataP[1] = P
# print(dataP)
# print('next', P)
# print(dataP[1])

# test data
# data = Data(R=100000, N=10, m=100, t=1, dt=3600, epsilon=0)
