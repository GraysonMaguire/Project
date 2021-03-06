from matplotlib import pyplot as plt
from matplotlib import animation
import matplotlib

import numpy as np
from tqdm import tqdm
# verbose functions
normal = np.linalg.norm

dt = 10 * 24 * 60 * 60
compressFactor = 100
xUnit = 1000 * 365.25 * 24 * 60 * 60
effdt = compressFactor * dt / xUnit
mData1 = np.load(
    '/Users/grays/Project/Data/finalData2/23-2-21-200p-Myr-mass.npy')


plt.rc('font', family='serif', size='12')
# plt.style.use('dark_background')
fig, axis = plt.subplots(figsize=(8, 4), dpi=400)

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
plt.rcParams.update({'font.size': 16})


def massPlot(mData, color, label):
    totalMassOverTime = np.sum(mData, 1)
    time = np.array(list(range(len(totalMassOverTime)))) * effdt

    M0 = totalMassOverTime[0]

    normalisedMassOverTime = totalMassOverTime * 200 / M0

    axis.plot(time, normalisedMassOverTime, color=color, label=label)

    pass


massPlot(mData1, 'darkturquoise', None)


axis.set_xlabel('time/kyr')
axis.set_ylabel('Total mass of cluster/M0')
axis.set_xlim(0, 2000)
axis.set_ylim(0, 205)
axis.axvline(x=84, color='deeppink', linestyle='--', label='collision')

axis.legend()
plt.tight_layout()

plt.savefig('./saves/massOverTime.png')
# plt.show()
