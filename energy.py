import numpy as np
from tqdm import tqdm
# verbose functions
normal = np.linalg.norm

G = 6.674e-11


def calcKE(vData, M):
    KE = np.zeros((len(vData), len(M)))

    for iteration in range(len(vData)):

        for particle in range(len(M)):
            V = vData[iteration][particle]
            KE[iteration][particle] = 0.5 * M[particle] * normal(V)**2

    return(KE)


def gPE(m1, m2, r1, r2):
    return (-G * m1 * m2 * (1 / normal(r1 - r2)))


def calcPE(pData, M):

    PE = np.zeros((len(pData), len(M)))

    for iteration in tqdm(range(len(pData))):
        P = pData[iteration]
        memory = 0
        x = 1
        for y in range(len(M) - 1):
            while x < len(M):
                pe = gPE(M[x], M[y], P[x], P[y])
                PE[iteration][x] += pe
                PE[iteration][y] += pe
                x += 1
            memory += 1
            x = memory + 1
    return PE


def reshapeData(data):
    totalSteps = len(data[0][0])
    Dimensions = 3
    totalParticles = len(data)

    newData = np.full((totalSteps, totalParticles, Dimensions), 0.0)

    for i in tqdm(range(totalSteps)):
        for j in range(Dimensions):
            for k in range(totalParticles):
                newData[i][k][j] = data[k][j][i]

    return newData


def App(pData, vData, M):
    print('crunching daddys energies')
    PE = calcPE(pData, M)
    np.save('30-1-21-150p-2000y-10d-daddy-PE', PE)
    KE = calcKE(vData, M)
    np.save('30-1-21-150p-2000y-10d-daddy-KE', KE)
    pass


P = np.load('data/30-1-21-150p-2000y-10d-daddy-position.npy')
V = np.load('data/30-1-21-150p-2000y-10d-daddy-velocity.npy')
M = np.load('daddy/daddyM.npy')

P = reshapeData(P)


App(P, V, M)
