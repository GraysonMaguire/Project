from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm

normal = np.linalg.norm

plt.rc('font', family='serif')
# plt.style.use('dark_background')
fig, axis = plt.subplots()

dt = 10 * 24 * 60 * 60
compressFactor = 100
xUnit = 1000 * 365.25 * 24 * 60 * 60
effdt = compressFactor * dt / xUnit
yUnit = 3.086e13


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
            return orderedRadii[j] / yUnit

    pass


def halfMassRadiusOverTime(mData, pData, color, label):
    iterations = len(mData)
    dataPoints = 10000
    step = int(iterations / dataPoints)

    halfRadii = []
    time = []

    for i in tqdm(range(0, iterations, step)):
        halfRadii.append(calcHalfMassRadius(mData[i], pData[i]))
        time.append(i * effdt)

    axis.plot(time, halfRadii, color=color, label=label)

    pass


P = np.load(
    '/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-position.npy')
M = np.load(
    '/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-mass.npy')

halfMassRadiusOverTime(M, P, 'skyblue', None)

axis.set_xlabel('time/kyr')
axis.set_ylabel('Half mass radius/pc')
axis.set_xlim(0, 1000)
axis.axvline(x=84, color='r', linestyle='--', label='collision')
# axis.set_title('Half mass of Globular cluster over time')

plt.legend()
plt.savefig('./saves/halfMassRadius.png')
plt.show()
