# imports
import numpy as np
from tqdm import tqdm
import concurrent.futures
import os

# verbose functions
normal = np.linalg.norm


class Work(object):
    def __init__(self, P0, V0, t, dt, M, epsilon, colRad):
        self.processSplit = self.calcProcessSplit(len(P0))
        self.P0 = P0
        self.V0 = V0
        self.t = t
        self.dt = dt
        self.M = M
        self.epsilon = epsilon
        self.G = 6.674e-11
        self.colRad = colRad

    def calcProcessSplit(self, N):
        ys = [0]
        cores = os.cpu_count()
        fliped = []
        area = ((N - 1)**2) / (2 * cores)
        for i in range(cores):
            y = (2 * area + ys[i]**2)**0.5
            ys.append(y)
            ys[i] = int(ys[i])
            if(i == cores - 1):
                ys[i + 1] = N
        for i in range(cores + 1):
            fliped.append(np.absolute(ys[cores - i] - N))

        return fliped

    def gForce(self, m1, m2, r1, r2):
        force = -m1 * m2 * self.G * \
            ((r1 - r2) / (normal(r1 - r2)**2 + self.epsilon**2)**1.5)
        return (force)

    def calcForceOnParticles(self, P, M):

        N = len(P)
        # forces = np.full((len(P), 3), 0.0)
        print('start')
        # with concurrent.futures.ProcessPoolExecutor() as executer:
        #     results = []
        #     for i in range(os.cpu_count()):
        #         r = executer.submit(self.calcForceOnParticlesMultiProcess,
        #                             P, M, self.processSplit[i], self.processSplit[i + 1])
        #         results.append(r)
        #     for f in concurrent.futures.as_completed(results):
        #         forces += f.result()
        #         print('lock')

        forces = self.oldCalcForceOnParticles(P, M)
        # dif = forces - forces2

        # forces2 = self.calcForceOnParticlesMultiProcess(P, M, 0, 1000)
        # dif = forces - forces2
        # print('done', dif)

        return forces

    def oldCalcForceOnParticles(self, P, M):

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

    def calcForceOnParticlesMultiProcess(self, P, M, start, finish):

        N = len(P)
        forces = np.full((N, 3), 0.0)
        y = start
        x = start + 1

        while y < finish:
            while x < N:

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
        newP = P
        newM = M
        newV = V

        i = 0
        while i < len(newM):
            if newM[i] == 0:
                i += 1
                continue
            j = i + 1
            while j < len(P):
                if newM[j] == 0:
                    j += 1
                    continue
                p1 = P[i]
                p2 = P[j]
                if self.calcDistanceBetween(p1, p2) < self.colRad:
                    index1 = self.indexOf(P, p1)
                    index2 = self.indexOf(P, p2)
                    print('collision', index1, index2)
                    newM, newV, newP = self.handleCollision(
                        newM, newV, newP, [index1, index2])

                j += 1
            i += 1

        return (newP, newM, newV)

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
        ke = 0
        for i in range(len(M)):
            ke += 0.5 * M[i] * normal(V[i])**2
        return(ke)

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
        totalSteps = int(self.t / self.dt)
        Dimensions = 3
        totalParticles = len(self.M)

        newData = np.full((totalParticles, Dimensions, totalSteps), 0.0)

        for i in tqdm(range(totalSteps)):
            for j in range(Dimensions):
                for k in range(totalParticles):
                    newData[k][j][i] = data[i][k][j]

        return newData

    def numberCruncher(self):
        iterations = int(self.t / self.dt)
        P = self.P0
        V = self.V0
        M = self.M
        pHalf = P
        print('duration: ', self.t / (60 * 60 * 24 * 365.25))
        print('iterations: ', iterations)
        print('number of particles: ', len(M))

        rawP = np.full(
            (iterations, len(M), 3), 0.0)
        rawV = np.full(
            (iterations, len(M), 3), 0.0)
        rawF = np.full(
            (iterations, len(M), 3), 0.0)
        PHalf = np.full(
            (iterations, len(M), 3), 0.0)

        rawV[0], rawP[0], PHalf[0] = V, P, pHalf
        print('beginning crunch')
        for i in tqdm(range(iterations)):
            # rawP[i], M, rawV[i] = self.checkForCollision(
            #     rawP[i], M, rawV[i])
            rawF[i] = self.calcForceOnParticles(rawP[i], M)

            if i == iterations - 1:
                break

            rawV[i + 1] = self.calcNextVelocity(rawV[i], rawF[i], M)

            rawP[i + 1], PHalf[i +
                               1] = self.calcNextPosition(rawP[i], rawV[i + 1])

        print('crunch over, finalising data...')

        return(self.reshapeData(rawP), rawV, rawF)
