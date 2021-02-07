# imports
import numpy as np
from tqdm import tqdm

# import concurrent.futures
from functools import partial
from multiprocessing import Pool
import os

# verbose functions
normal = np.linalg.norm


class Work(object):
    def __init__(self, P0, V0, t, dt, M, colRad):

        self.P0 = P0
        self.V0 = V0
        self.t = t
        self.dt = dt
        self.M = M.flatten()
        self.G = 6.674e-11
        self.colRad = colRad
        self.pData = []
        self.vData = []
        self.mData = []

    def gForce(self, m1, m2, r1, r2):
        if m1 == 0 or m2 == 0:
            return 0

        force = -m1 * m2 * self.G * \
            ((r1 - r2) / (normal(r1 - r2)**2)**1.5)
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
            if M[i] == 0:
                nextVels[i] = VPrev[i]
                continue
            nextVels[i] = self.nextVelocity(VPrev[i], F[i], M[i])

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

    def checkForCollision(self, P, M, V):
        M = self.M
        i = 0
        while i < len(M):
            if M[i] == 0:
                i += 1

                continue
            j = i + 1
            while j < len(P):
                if M[j] == 0:
                    j += 1

                    continue
                p1 = P[i]
                p2 = P[j]
                if self.calcDistanceBetween(p1, p2) < self.colRad:
                    index1 = self.indexOf(P, p1)
                    index2 = self.indexOf(P, p2)
                    print('collision', index1, index2)
                    M, V, P = self.handleCollision(
                        M, V, P, [index1, index2])

                j += 1
            i += 1
        self.M = M

        return P, M, V

    def handleCollision(self, M, V, P, indexes):
        if M[indexes[0]] > M[indexes[1]]:
            primary = indexes[0]
            secondary = indexes[1]
        else:
            primary = indexes[1]
            secondary = indexes[0]

        primaryMomentum = M[primary] * V[primary]
        secondaryMomentum = M[secondary] * V[secondary]
        newMomentum = primaryMomentum + secondaryMomentum

        newMass = M[primary] + M[secondary]
        newVelcoity = newMomentum / newMass
        M[primary] = newMass
        V[primary] = newVelcoity
        M[secondary] = 0
        V[secondary] = 0
        # P[secondary] = 0
        # in final release this will be changed back
        # to original but for testting this makes most sense

        # newM = np.delete(M, secondary, axis=0)
        # newV = np.delete(V, secondary, axis=0)
        # newP = np.delete(P, secondary, axis=0)

        return (M, V, P)

    def calcDistanceBetween(self, p1, p2):
        return normal(p1 - p2)

    def indexOf(self, Array, item):
        for i in range(len(Array)):
            if (Array[i] == item).all():
                return i

    def calcKE(self, V, M):
        KE = np.zeros(len(M))

        for particle in range(len(M)):

            KE[particle] = 0.5 * M[particle] * normal(V[particle])**2

        return(KE)

    def gPE(self, m1, m2, r1, r2):

        return (-self.G * m1 * m2 * (1 / normal(r1 - r2)))

    def calcPE(self, P, M):

        PE = np.zeros(len(M))
        memory = 0
        x = 1

        for y in range(len(M) - 1):
            while x < len(M):
                pe = self.gPE(M[x], M[y], P[x], P[y])
                PE[x] += pe
                PE[y] += pe
                x += 1
            memory += 1
            x = memory + 1
        return PE

    def checkForEscape(self, P, V, M):
        PE = self.calcPE(P, M)

        KE = self.calcKE(V, M)

        T = KE + PE
        for i in range(len(T)):
            if self.M[i] == 0:
                continue
            if T[i] >= 0:
                self.M[i] = 0
                print('particle ejected: ', i)

        pass

    def reshapeData(self, data):
        totalSteps = int(self.t / self.dt)
        Dimensions = 3
        totalParticles = len(self.M)

        newData = np.full((totalParticles, Dimensions, totalSteps), 0.0)

        for i in tqdm(range(totalSteps)):
            for j in range(Dimensions):
                for k in range(totalParticles):
                    newData[k][j][i] = data[i][k][j]

        return newData

    def start(self):
        iterations = int(self.t / self.dt)
        P = self.P0
        V = self.V0
        M = self.M
        pHalf = P
        print('years: ', self.t / (60 * 60 * 24 * 365.25))
        print('iterations: ', iterations)
        print('number of particles: ', len(M))

        rawP = np.full((iterations, len(M), 3), 0.0)
        rawV = np.full((iterations, len(M), 3), 0.0)
        rawF = np.full((iterations, len(M), 3), 0.0)
        PHalf = np.full((iterations, len(M), 3), 0.0)
        rawM = np.full((iterations, len(M)), 0.0)

        rawV[0], rawP[0], PHalf[0] = V, P, pHalf

        print('beginning crunch')

        for i in tqdm(range(iterations)):
            rawP[i], rawM[i], rawV[i] = self.checkForCollision(
                rawP[i], rawM[i], rawV[i])

            rawF[i] = self.calcForceOnParticles(rawP[i], rawM[i])

            if i == iterations - 1:
                break

            rawV[i + 1] = self.calcNextVelocity(rawV[i], rawF[i], rawM[i])

            rawP[i + 1], PHalf[i +
                               1] = self.calcNextPosition(rawP[i], rawV[i + 1])

            self.checkForEscape(PHalf[i + 1], rawV[i + 1], rawM[i])

        print('crunch over, finalising data...')

        self.pData = rawP
        self.vData = rawV
        self.mData = rawM

        pass
