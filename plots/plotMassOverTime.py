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
mData = np.load(
    '/Users/garymagnum/Project/data/11-2-21-9e13BabyCrunch/11-2-21-100p-50por100000yr-10d-9e13-mass.npy')


plt.rc('font', family='serif')
plt.style.use('dark_background')

fig, axis = plt.subplots()


totalMassOverTime = np.sum(mData, 1)

time = np.array(list(range(len(totalMassOverTime)))) * effdt

M0 = totalMassOverTime[0]

normalisedMassOverTime = totalMassOverTime / M0


axis.plot(time, normalisedMassOverTime, color='red', label='9e13m')


axis.set_xlabel('time/kyr')
axis.set_ylabel('Total mass of cluster/M0')

axis.set_title('Mass of Globular cluster over time')

axis.legend()

plt.savefig('massOverTime.png', transparent=True)
plt.show()
