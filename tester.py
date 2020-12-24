import numpy as np
from display import Display
from work import Work
from init import Data


P0 = np.array(
    [[0.0, 0.0, 0.0], [1.4960e11, 0.0, 0.0], [-7.7854e11, 0.0, 0.0], [1e11, 1e11, 0]])
V0 = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [
    0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
t = 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
M = np.array([1, 5, 1, 1])
steps = 1
epsilon = 0
colRad = 1000


data = Data(R, N, m, t, dt, steps, epsilon)

# worker = Work(P0, V0, t, dt, M, steps, epsilon, colRad)
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
