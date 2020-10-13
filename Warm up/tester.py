import numpy as np
from display import Display
from work import Work
from init import data

workTest = Work(data.P0, data.V0, data.t, data.dt, data.M)

# test gForce

# test calcForceOnParticles

#print(workTest.calcForceOnParticles(data.P0, data.M))
# test calcNextPosition
#P, Phalf = workTest.calcNextPosition(data.P0, data.V0)
# test calcNextVelocity

# print(workTest.calcNextVelocity(
#     data.V0, workTest.calcForceOnParticles(data.P0, data.M), data.M))
# test numberCruncher
P, V, F = workTest.numberCruncher()

print('dataP', P)

display = Display(P, V, F, data.t, data.dt, data.M)
display.postitionPlot()

# dataP = np.full(
#     (10, len(data.M), 3), 0.0)
# dataP[1] = P
# print(dataP)
# print('next', P)
# print(dataP[1])
