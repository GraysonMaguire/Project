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
    '/Users/garymagnum/Project/data/11-2-21-9e13BabyCrunch/11-2-21-100p-50por100000yr-10d-9e13-mass.npy')
mData2 = np.load(
    '/Users/garymagnum/Project/data/12-2-21-2e14BabyCrunch/12-2-21-100p-50por100000yr-10d-2e14-mass.npy')
mData3 = np.load(
    '/Users/garymagnum/Project/data/13-2-21-1e15BabyCrunch/13-2-21-100p-50por100000yr-10d-1e15-mass.npy')
mData4 = np.load(
    '/Users/garymagnum/Project/data/13-2-21-5e14BabyCrunch/13-2-21-100p-50por100000yr-10d-5e14-mass.npy')


plt.rc('font', family='serif', weight='bold', size='18')
plt.style.use('dark_background')

fig, axis = plt.subplots(figsize=(8, 4))


totalMassOverTime1 = np.sum(mData1, 1)
totalMassOverTime2 = np.sum(mData2, 1)
totalMassOverTime3 = np.sum(mData3, 1)
totalMassOverTime4 = np.sum(mData4, 1)

time = np.array(list(range(len(totalMassOverTime1)))) * effdt
time3 = np.array(list(range(len(totalMassOverTime3)))) * effdt
time4 = np.array(list(range(len(totalMassOverTime4)))) * effdt

M0 = totalMassOverTime1[0]

normalisedMassOverTime1 = totalMassOverTime1 / M0
normalisedMassOverTime2 = totalMassOverTime2 / M0
normalisedMassOverTime3 = totalMassOverTime3 / M0
normalisedMassOverTime4 = totalMassOverTime4 / M0


axis.plot(time, normalisedMassOverTime2, color='deepskyblue', label='1e14m')
axis.plot(time4, normalisedMassOverTime4, color='orange', label='5e14m')
axis.plot(time3, normalisedMassOverTime3, color='lime', label='1e15m')


axis.set_xlabel('time/kyr')
axis.set_ylabel('Total mass of cluster/M0')

# axis.set_title('Mass of Globular cluster over time')
axis.set_xlim(0, 200)

axis.legend()
plt.tight_layout()

plt.savefig('massOverTime.png', transparent=True)
plt.show()
