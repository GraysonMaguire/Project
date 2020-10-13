# imports
import numpy as np
from init import data
# verbose functions
normal = np.linalg.norm
# global variables
epsilon = np.array([0, 0, 0])
G = 6.674e-11
N = data.N

# functions


class Work(object):
    def __init__(self, P0, V0, t, dt, M):
        self.P0 = P0
        self.V0 = V0
        self.t = t
        self.dt = dt
        self.M = M
        self.G = 6.674e-11
        self.epsilon = 0.1

    def gForce(self, m1, m2, r1, r2):
        force = -m1 * m2 * self.G * \
            ((r1 - r2) / (normal(r1 - r2)**2 + self.epsilon**2)**1.5)
        return (force)

    def calcForceOnParticles(self, P, M):

        forces = np.full((len(P), 3), 0.0)
        y = 0
        x = 1
        for i in range(len(P) - 1):
            while x < len(P):
                force = self.gForce(M[x], M[y], P[x], P[y])
                forces[x] += force
                forces[y] -= force
                x += 1
            y += 1
            x = y + 1
        return forces

    def nextVelocity(self, vPrev, f, m):
        return vPrev + f * self.dt / m

    def calcNextVelocity(self, VPrev, F, M):
        nextVels = np.full_like(VPrev, 0.0)
        for i in range(len(M)):
            nextVels[i] = self.nextVelocity(VPrev[i], F[i], M[i])
        return nextVels

    def calcNextPosition(self, dPrev, v):
        halfStep = dPrev + v * self.dt / 2
        fullStep = dPrev + v * self.dt
        return fullStep, halfStep

    def numberCruncher(self):
        print('beginning crunch')
        iterations = int(self.t / self.dt)
        P = self.P0
        V = self.V0
        M = self.M

        dataP = np.full(
            (iterations, len(M), 3), 0.0)
        dataV = np.full(
            (iterations, len(M), 3), 0.0)
        dataF = np.full(
            (iterations, len(M), 3), 0.0)
        dataV[0], dataP[0] = V, P

        for i in range(iterations):

            dataF[i] = self.calcForceOnParticles(dataP[i], M)

            if i == iterations - 1:
                break

            dataV[i + 1] = self.calcNextVelocity(dataV[i], dataF[i], M)
            dataP[i + 1], PHalf = self.calcNextPosition(dataP[i], dataV[i + 1])
        print('crunch over')
        return(dataP, dataV, dataF)
