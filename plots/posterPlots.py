from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm

normal = np.linalg.norm

plt.rc('font', family='serif', weight='bold', size='20')

plt.style.use('dark_background')
fig = plt.subplots(figsize=(12, 20), dpi=400)
axisTop = plt.subplot(4, 3, (1, 3))
axisMain = plt.subplot(4, 3, (4, 9))
axisSec = plt.subplot(4, 3, (10, 12))


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

    ormalise = np.mean(halfRadii)

    totalMassOverTime = np.sum(mData, 1)
    time1 = np.array(list(range(len(totalMassOverTime)))) * effdt

    normalisedMassOverTime = totalMassOverTime / totalMassOverTime[0]

    axisMain.plot(time, halfRadii, color=color, label=label)

    normalise = np.mean(halfRadii)

    halfRadii = np.array(halfRadii) / normalise

    axisSec.plot(time, halfRadii, color=color, label=label)
    axisTop.plot(time1, normalisedMassOverTime, color=color, label=label)

    pass


# Import dataPoints
mData2 = np.load(
    '/Users/garymagnum/Project/data/12-2-21-2e14BabyCrunch/12-2-21-100p-50por100000yr-10d-2e14-mass.npy'
)
pData2 = np.load(
    '/Users/garymagnum/Project/data/12-2-21-2e14BabyCrunch/12-2-21-100p-50por100000yr-10d-2e14-position.npy'
)
mData3 = np.load(
    '/Users/garymagnum/Project/data/13-2-21-1e15BabyCrunch/13-2-21-100p-50por100000yr-10d-1e15-mass.npy')
pData3 = np.load(
    '/Users/garymagnum/Project/data/13-2-21-1e15BabyCrunch/13-2-21-100p-50por100000yr-10d-1e15-position.npy')
mData4 = np.load(
    '/Users/garymagnum/Project/data/13-2-21-5e14BabyCrunch/13-2-21-100p-50por100000yr-10d-5e14-mass.npy')
pData4 = np.load(
    '/Users/garymagnum/Project/data/13-2-21-5e14BabyCrunch/13-2-21-100p-50por100000yr-10d-5e14-position.npy')

axisSec.set_xlabel('time/kyr')
axisMain.set_ylabel('HMR/pc')
axisSec.set_ylabel('Normalised to mean')
axisTop.set_ylabel('Total mass of cluster/M0')

axisTop.set_xticks([])
axisMain.set_xticks([])
axisSec.set_yticks([0.5, 0.75, 1, 1.25, 1.5])

axisSec.set_ylim(0.5, 1.5)
axisSec.set_xlim(0, 200)
axisMain.set_xlim(0, 200)
axisTop.set_xlim(0, 200)
axisSec.plot([0, 200], [1, 1], '--', color='white')


halfMassRadiusOverTime(mData2, pData2, 'deepskyblue', '1e14m')
halfMassRadiusOverTime(mData4, pData4, 'orange', '5e14m')
halfMassRadiusOverTime(mData3, pData3, 'lime', '1e15m')


plt.subplots_adjust(hspace=0)

axisMain.legend(title='Plummer radius')

# plt.tight_layout()

# plt.legend()
plt.savefig('posterPlot.png', transparent=True)
plt.show()
