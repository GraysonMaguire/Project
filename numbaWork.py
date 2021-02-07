# imports
import numpy as np
from tqdm import tqdm
from numba import njit
from time import time

# verbose functions

G = 6.674e-11
P0 = np.load('baby/babyP0.npy')
V0 = np.load('baby/babyV0.npy')
M0 = np.load('baby/babyM.npy').flatten()


@njit
def normal(x):
    y = 0
    for i in x:
        y += i**2

    return np.sqrt(y)


@njit
def gForce(m1, m2, r1, r2):
    result = np.zeros(3)

    if m1 == 0 or m2 == 0:
        return result

    multiplier = -m1 * m2 * G / (normal(r1 - r2)**3)
    force = r1 - r2
    np.multiply(force, multiplier, result)

    return (result)


@njit
def calcForceOnParticles(P, M):

    forces = np.full((len(P), 3), 0.0)
    y = 0
    x = 1

    for i in range(len(P) - 1):
        while x < len(P):
            force = gForce(M[x], M[y], P[x], P[y])
            forces[x] += force
            forces[y] -= force

            x += 1
        y += 1
        x = y + 1

    return forces


@njit
def nextVelocity(vPrev, f, m, dt):
    a = f * (1 / m)
    return vPrev + (a * dt)


@njit
def calcNextVelocity(VPrev, F, M, dt):
    nextVels = np.full_like(VPrev, 0.0)
    for i in range(len(M)):
        if M[i] == 0:
            nextVels[i] = VPrev[i]

            continue
        nextVels[i] = nextVelocity(VPrev[i], F[i], M[i], dt)

    return nextVels


@njit
def calcNextPosition(dPrev, v, dt):
    halfStep = dPrev + v * (dt / 2)
    fullStep = dPrev + v * dt
    return (fullStep, halfStep)


@njit
def calcCOM(P, M):
    result = np.zeros(3)
    sumMR = np.zeros(3)
    sumM = np.sum(M)
    for i in range(len(M)):

        sumMR += M[i] * P[i]

    return (sumMR / sumM)


@njit
def indexOf(Array, item):
    for i in range(len(Array)):
        if (Array[i] == item):
            return i


@njit
def handleCollision(M, V, P, indexes):

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

    return M, V, P


@njit
def checkForCollision(P, M, V, colRad):
    indexes = np.array([0, 0])
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
            if normal(p1 - p2) < colRad:
                indexes[0] = indexOf(P, p1)
                indexes[1] = indexOf(P, p2)

                print('collision', indexes)
                M, V, P = handleCollision(M, V, P, indexes)

            j += 1
        i += 1

    return P, M, V


@njit
def numberOfParticles(M):
    number = 0
    for m in M:
        if m != 0:
            number += 1
    return number


@njit
def calcKE(V, M):
    KE = np.zeros(len(M))

    for particle in range(len(M)):

        KE[particle] = 0.5 * M[particle] * normal(V[particle])**2

    return KE


@njit
def gPE(m1, m2, r1, r2):
    return (-G * m1 * m2 * (1 / normal(r1 - r2)))


@njit
def calcPE(P, M):

    PE = np.zeros(len(M))
    memory = 0
    x = 1

    for y in range(len(M) - 1):
        while x < len(M):
            pe = gPE(M[x], M[y], P[x], P[y])
            PE[x] += pe
            PE[y] += pe
            x += 1
        memory += 1
        x = memory + 1
    return PE


@njit
def checkForEscape(P, V, M):
    PE = calcPE(P, M)

    KE = calcKE(V, M)

    T = np.add(PE, KE)
    for i in range(len(T)):
        if M[i] == 0:
            continue
        if T[i] >= 0:
            M[i] = 0
            print('particle ejected: ', i)

    pass


# @njit
# def reshapeData(data):
#     totalSteps = len(data)
#     totalParticles = len(data[0])
#     Dimensions = len(data[0][0])
#
#     newData = np.full((totalParticles, Dimensions, totalSteps), 0.0)
#
#     for i in tqdm(range(totalSteps)):
#         for j in range(Dimensions):
#             for k in range(totalParticles):
#                 newData[k][j][i] = data[i][k][j]
#
#     return newData
#
#     pass
# checkForEscape(P0, V0, M0)
# tick = time()
# (checkForEscape(P0, V0, M0))
# tock = time()
# print(tock - tick)

@njit
def work(P0, V0, t, dt, M, colRad, minParticles):
    print('START')
    iterations = int(t / dt)
    P = P0
    V = V0
    M = M
    pHalf = P
    print('years: ', t / (60 * 60 * 24 * 365.25))
    print('iterations: ', iterations)
    print('number of particles: ', len(M))

    rawP = np.full((iterations, len(M), 3), 0.0)
    rawV = np.full((iterations, len(M), 3), 0.0)
    rawF = np.full((iterations, len(M), 3), 0.0)
    PHalf = np.full((iterations, len(M), 3), 0.0)
    rawM = np.full((iterations, len(M)), 0.0)
    rawM[0] = M
    rawV[0], rawP[0], PHalf[0] = V, P, pHalf

    print('beginning crunch...')

    for i in (range(iterations)):
        if i > 0:
            rawP[i], rawM[i], rawV[i] = checkForCollision(
                rawP[i], rawM[i - 1], rawV[i], colRad)

        rawF[i] = calcForceOnParticles(rawP[i], rawM[i])

        if i == iterations - 1:
            break

        if numberOfParticles(rawM[i]) < minParticles:
            break

        rawV[i + 1] = calcNextVelocity(rawV[i], rawF[i], rawM[i], dt)

        rawP[i + 1], PHalf[i + 1] = calcNextPosition(rawP[i], rawV[i + 1], dt)

        checkForEscape(PHalf[i + 1], rawV[i + 1], rawM[i])

    print('FINISH')

    return rawP, rawV, rawM


work(P0, V0, 4, 1, M0, 1e7, 50)
