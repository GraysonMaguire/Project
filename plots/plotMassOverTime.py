from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm
# verbose functions
normal = np.linalg.norm

dt = 10 * 24 * 60 * 60
compressFactor = 100
xUnit = 1000 * 365.25 * 24 * 60 * 60
effdt = compressFactor * dt / xUnit
mData1 = np.load(
    '/Users/garymagnum/Project/data/19-2-21-e16Crunch/16-2-21-100p-baby-mass.npy')
# mData2 = np.load(
#     '/Users/garymagnum/Project/data/12-2-21-2e14BabyCrunch/12-2-21-100p-50por100000yr-10d-2e14-mass.npy')
# mData3 = np.load(
#     '/Users/garymagnum/Project/data/13-2-21-1e15BabyCrunch/13-2-21-100p-50por100000yr-10d-1e15-mass.npy')
# mData4 = np.load(
#     '/Users/garymagnum/Project/data/13-2-21-5e14BabyCrunch/13-2-21-100p-50por100000yr-10d-5e14-mass.npy')


plt.rc('font', family='serif', weight='bold', size='18')
plt.style.use('dark_background')

fig, axis = plt.subplots(figsize=(8, 4))


def massPlot(mData, color, label):
    totalMassOverTime = np.sum(mData, 1)
    time = np.array(list(range(len(totalMassOverTime)))) * effdt

    M0 = totalMassOverTime[0]

    normalisedMassOverTime = totalMassOverTime / M0

    axis.plot(time, normalisedMassOverTime, color=color, label=label)

    pass


massPlot(mData1, 'deepskyblue', 'collision')


axis.set_xlabel('time/kyr')
axis.set_ylabel('Total mass of cluster/M0')

# axis.set_title('Mass of Globular cluster over time')
axis.set_xlim(0, 200)

axis.legend()
plt.tight_layout()

plt.savefig('massOverTime.png', transparent=True)
plt.show()
