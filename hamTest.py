import numpy as np
from numbaWork import work
from plummerModel import plummerModel
from init import Data
import os
from time import time
from tqdm import tqdm

t = 100 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
N = 200
M0 = 2e32
colRad = 1e7
minParticles = 50

babyP0 = np.load('baby/babyP0.npy')
babyV0 = np.load('baby/babyV0.npy')
babyM0 = np.load('baby/babyM.npy').flatten()

tick = time()

work(babyP0, babyV0, babyM0, t, dt, colRad, minParticles)

tock = time()

print(tock - tick)
