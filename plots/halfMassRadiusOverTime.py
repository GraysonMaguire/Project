from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm

normal = np.linalg.norm


def calcCOM(P, M):
    result = np.zeros(3)
    sumMR = np.zeros(3)
    sumM = np.sum(M)
    for i in range(len(M)):

        sumMR += M[i] * P[i]

    return (sumMR / sumM)


def calcRadius(p, com):
    r = p - com
    return normal(r)


def calcHalfMassRadius(M, P):
    orderedRadii = []
    orderedMasses = []
    com = calcCOM(P, M)
    for i in range(len(M)):
        m = M[i]
        p = P[i]
        if m == 0:
            continue
        r = calcRadius(p, com)
        orderedRadii.append(r)
        orderedMasses.append(m)

    orderedRadii, orderedMasses = (list(t) for t in zip(
        *sorted(zip(orderedRadii, orderedMasses))))
    halfMass = sum(orderedMasses) / 2

    total = 0
    for j in range(len(orderedRadii)):
        total += orderedMasses[j]
        if total >= halfMass:
            return orderedRadii[j]

    pass


def halfMassRadiusOverTime(mData, pData):
    iterations = len(mData)
    dataPoints = 1000
    step = int(iterations / dataPoints)

    year = 36.5

    fig = plt.figure()
    ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

    halfRadii = []
    time = []

    for i in tqdm(range(0, iterations, step)):
        halfRadii.append(calcHalfMassRadius(mData[i], pData[i]))
        time.append(i / year)

    ax.plot(time, halfRadii)

    plt.show()

    pass


mData = np.load(
    '/Users/garymagnum/Project/data/9-2-21-9e13Crunch/9-2-21-150p-75por20000yr-10d-90000000000000.0-masses.npy')
pData = np.load(
    '/Users/garymagnum/Project/data/9-2-21-9e13Crunch/9-2-21-150p-75por20000yr-10d-90000000000000.0-position.npy')

halfMassRadiusOverTime(mData, pData)
