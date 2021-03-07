from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm

normal = np.linalg.norm

nBins = 100
rMinPower = 0
rMaxPower = 16


plt.rc('font', family='serif', weight='bold', size='18')
# plt.style.use('dark_background')

fig, axis = plt.subplots(figsize=(8, 4))
plt.xscale('log')
# plt.yscale('log')


def calcCOM(P, M):
    sumMR = np.zeros(3)
    sumM = 0
    for i in range(len(M)):
        sumM += M[i]
        sumMR += M[i] * P[i]
    return(sumMR / sumM)


def generateBins():
    diff = (rMaxPower - rMinPower) / (nBins)
    bins = []
    binData = []
    for i in range(nBins + 1):
        bins.append(10**(rMinPower + i * diff))
        if i < nBins:
            binData.append([])

    return bins, binData


def whichBin(value, bins):
    for i in range(len(bins) - 1):
        lower = bins[i]
        upper = bins[i + 1]
        if value < upper and value >= lower:
            return i

    return -1


def generateData(vData, pData):

    bins, binData = generateBins()
    xData = []
    yData = []

    for i in range(len(pData)):
        v = normal(vData[i])
        r = normal(pData[i])
        binLocation = whichBin(r, bins)
        binData[binLocation].append(v)

    for i in range(len(binData)):
        xData.append((bins[i] + bins[i + 1]) / 2)
        yData.append(np.mean(binData[i]))

    return xData, yData


def velocityDispersion(vData, pData, label, color):
    xData, yData = generateData(vData, pData)

    axis.plot(xData, yData, 'o', color=color, label=label)

    pass


P = np.load(
    '/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-position.npy')[-1]
V = np.load(
    '/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-velocity.npy')[-1]
M = np.load(
    '/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-mass.npy')[-1]
P2 = np.load(
    '/Users/grays/Project/Data/Baby/23-2-21-100p-baby-position.npy')[0]
V2 = np.load(
    '/Users/grays/Project/Data/Baby/23-2-21-100p-baby-velocity.npy')[0]
M2 = np.load(
    '/Users/grays/Project/Data/Baby/23-2-21-100p-baby-mass.npy')[0]

pCentered = P - calcCOM(P, M)

velocityDispersion(V, pCentered, 'final cluster', 'deepskyblue')
velocityDispersion(V2, P2, 'initial cluster', 'red')

plt.savefig('./saves/velocityDispersionInitial.png')
plt.show()
