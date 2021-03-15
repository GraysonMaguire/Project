from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib
import numpy as np
from tqdm import tqdm

normal = np.linalg.norm

# plt.rc('font', family='serif', size='12')
# # plt.style.use('dark_background')
# fig, axis = plt.subplots(figsize=(8, 8), dpi=400)
#
# matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIXGeneral'
# plt.rcParams.update({'font.size': 16})

dt = 10 * 24 * 60 * 60
compressFactor = 100
xUnit = 1000 * 365.25 * 24 * 60 * 60
effdt = compressFactor * dt / xUnit
yUnit = 3.086e13
path = './coreRadiusData/'
# nBins = 2000


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


def volume(r):
    return (4 * np.pi * r ** 3) / 3


def calcRadiusFromVol(V):
    return (3 * V / (4 * np.pi))**(1 / 3)


def generateBins(rMax, nBins):
    totalVolume = volume(rMax)

    space = totalVolume / nBins

    v = space
    bins = []
    for i in range(nBins):
        bins.append(calcRadiusFromVol(v))
        v += space

    return bins


def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w


def formatP(P, M):
    com = calcCOM(P, M)
    pFormated = []

    for i in range(len(M)):
        m = M[i]
        p = P[i]
        if m == 0:
            continue
        p = p - com
        pFormated.append(normal(p))

    return np.array(pFormated)


def calcCoreRadius(M, P, nBins):

    R = formatP(P, M)

    rMax = np.amax(R) / 10
    bins = generateBins(rMax, nBins)
    density = []
    before = 0

    for after in bins:
        count = 0
        for r in R:
            if r < before:
                continue
            if r >= after:
                continue
            count += 1
        density.append(count)
        if density[-1] <= density[0] / 2:
            return (before + after) / (2 * yUnit)

        before = after

    pass


def coreRadiusOverTime(mData, pData, color, label, nBins):
    iterations = len(mData)
    dataPoints = len(mData)
    step = int(iterations / dataPoints)

    coreRadii = []
    time = []

    for i in tqdm(range(0, iterations, step)):
        coreRadii.append(calcCoreRadius(mData[i], pData[i], nBins))
        time.append(i * effdt)

    np.save(path + label + '_x', time)
    np.save(path + label + '_y', coreRadii)

    # coreRadii = moving_average(coreRadii, 800)
    # time = moving_average(time, 800)

    # axis.plot(time, coreRadii, 'o', color=color, label=label)

    pass


P = np.load(
    './finalData2/23-2-21-200p-Myr-position.npy')
M = np.load(
    './finalData2/23-2-21-200p-Myr-mass.npy')


coreRadiusOverTime(M, P, 'darkturquoise', '6000', 6000)
coreRadiusOverTime(M, P, 'red', '7000', 7000)
coreRadiusOverTime(M, P, 'red', '8000', 8000)
coreRadiusOverTime(M, P, 'red', '9000', 9000)
coreRadiusOverTime(M, P, 'red', '10000', 10000)

# axis.set_xlabel('time/kyr')
# axis.set_ylabel('core radius/pc')
# axis.set_xlim(0, 2000)
# axis.axvline(x=84, color='deeppink', linestyle='--', label='collision')
# # axis.set_title('Half mass of Globular cluster over time')
#
# plt.legend()
# plt.savefig('./saves/coreRadiusDots.png')
# plt.show()
