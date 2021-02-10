from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm
# verbose functions
normal = np.linalg.norm


def particlesOverTime(mData, plummerRadius, axis):

    particlesOverTime = np.count_nonzero(mData, 1)

    axis.plot(particlesOverTime, label=plummerRadius)

    print('final number of particles is', particlesOverTime[-1])

    pass


pathOfFolder = '/Users/garymagnum/Project/data/8-2-21-e13Crunch/'


initArray = np.load(
    '/Users/garymagnum/Project/data/8-2-21-e13Crunch/8-2-21-150p-75por2000yr-10d-initArray.npy', allow_pickle=True)

fig, axis = plt.subplots()

for i in range(len(initArray)):
    plummerRadius = initArray[i]
    path = f'/Users/garymagnum/Project/data/8-2-21-e13Crunch/8-2-21-150p-75por2000yr-10d-{plummerRadius}-results.npy'
    mData = np.load(path, allow_pickle=True)[-1]

    particlesOverTime(mData, plummerRadius, axis)
    axis.legend()
    # axis[i].set_title(plummerRadius)

plt.show()
