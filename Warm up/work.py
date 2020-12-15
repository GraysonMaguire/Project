# imports
import numpy as np
from tqdm import tqdm
# verbose functions
normal = np.linalg.norm


class Work(object):
    def __init__(self, P0, V0, t, dt, M, steps, epsilon):
        self.P0 = P0
        self.V0 = V0
        self.t = t
        self.dt = dt
        self.M = M
        self.steps = steps
        self.epsilon = epsilon
        self.G = 6.674e-11
    def checkForCollision(self,P):
        for i in range(len(P)):
            for j in range(len(P)):
                if i=j: next
                    pass
        return()
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
        a = f * (1 / m)
        return vPrev + (a * self.dt)

    def calcNextVelocity(self, VPrev, F, M):
        nextVels = np.full_like(VPrev, 0.0)
        for i in range(len(M)):
            nextVels[i] = self.nextVelocity(VPrev[i], F[i], M[i])
            # print(i, VPrev[i], nextVels[i], F[i])
        return nextVels

    def calcNextPosition(self, dPrev, v):
        halfStep = dPrev + v * (self.dt / 2)
        fullStep = dPrev + v * self.dt
        return (fullStep, halfStep)

    def calcCOM(self, P, M):
        sumMR = np.zeros(3)
        sumM = 0
        for i in range(len(M)):
            sumM += M[i]
            sumMR += M[i] * P[i]
        return(sumMR / sumM)

    def calcKE(self, V, M):
        ke = 0
        for i in range(len(M)):
            ke += 0.5 * M[i] * normal(V[i])**2
        return(ke)
        # return(normal(0.5 * M[:, np.newaxis] * V**2))

    def calcPE(self, P, M, F):
        com = self.calcCOM(P, M)
        PE = np.zeros(len(M))
        for i in range(len(M)):
            r = -com + P[i]
            PE[i] = np.dot(F[i], r)
        return(np.sum(PE))

    def calcEnergies(self, P, F, V):
        PE = self.calcPE(P, self.M, F)
        KE = self.calcKE(V, self.M)
        T = KE + PE
        return([T, KE, PE])

    def reshapeData(self, data):
        totalSteps = len(data)
        Dimensions = 3
        totalParticles = len(data[0])

        newData = np.zeros((3, self.steps, totalParticles))
        step = 0
        for i in tqdm(range(0, totalSteps, int(totalSteps / self.steps))):
            for j in range(Dimensions):
                for k in range(totalParticles):
                    newData[j][step][k] = data[i][k][j]
                    ++step
        return newData

    def numberCruncher(self):
        print('beginning crunch')
        iterations = int(self.t / self.dt)
        print('iterations', self.t / self.dt)
        P = self.P0
        V = self.V0
        M = self.M
        pHalf = P

        rawP = np.full(
            (iterations, len(M), 3), 0.0)
        rawV = np.full(
            (iterations, len(M), 3), 0.0)
        rawF = np.full(
            (iterations, len(M), 3), 0.0)
        PHalf = np.full(
            (iterations, len(M), 3), 0.0)
        Energies = np.zeros((3, iterations))

        rawV[0], rawP[0], PHalf[0] = V, P, pHalf
        for i in tqdm(range(iterations)):

            rawF[i] = self.calcForceOnParticles(rawP[i], M)
            Energies[0][i], Energies[1][i], Energies[2][i] = self.calcEnergies(
                PHalf[i], rawF[i], rawV[i])
            if i == iterations - 1:
                break

            rawV[i + 1] = self.calcNextVelocity(rawV[i], rawF[i], M)

            rawP[i + 1], PHalf[i +
                               1] = self.calcNextPosition(rawP[i], rawV[i + 1])
        print('crunch over, finalising data...')

        return(rawP, rawV, rawF, Energies)
