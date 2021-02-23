import numpy as np
from time import time
from tqdm import tqdm

path = '/Users/garymagnum/Project/hamData/'
path2 = '/Users/garymagnum/Project/data/23-2-21-MyrCrunchHam/'
datePrefix = '23-2-21-'

babyMass = np.load(
    path2 + 'baby/' + datePrefix + '100p-baby-mass.npy')
babyPosition = np.load(
    path2 + 'baby/' + datePrefix + '100p-baby-position.npy')
babyVelocity = np.load(
    path2 + 'baby/' + datePrefix + '100p-baby-velocity.npy')

daddyMass = np.load(
    path2 + 'daddy/' + datePrefix + '100p-daddy-mass.npy')
daddyPosition = np.load(
    path2 + 'daddy/' + datePrefix + '100p-daddy-position.npy')
daddyVelocity = np.load(
    path2 + 'daddy/' + datePrefix + '100p-daddy-velocity.npy')

year = 365.25 * 24 * 60 * 60
t = 100000 * year
M0 = 2e32
G = 6.67e-11

radiusOfCluster = 2e15

rNeeded = (((t / np.pi)**2) * 16 * G * M0)**(1 / 3)

R = 3 * radiusOfCluster

timeCollide = np.pi * np.sqrt((R**3) / (16 * G * M0))

vMax = np.sqrt(2 * G * M0 * 1 / radiusOfCluster)
vFromInf = np.sqrt(2 * G * M0 * 1 / R)

test = R / vFromInf
print(test / year, timeCollide / year)

V = vFromInf / 10
# R = rNeeded


def perturber(array, pertubation):

    for i in range(int(len(array) / 2)):
        array[i] = array[i] - pertubation
        array[-(i + 1)] = array[-(i + 1)] + pertubation

    return array


def App():
    newMass = np.concatenate((babyMass[0], daddyMass[0]))

    tempVelocity = np.concatenate((babyVelocity[0], daddyVelocity[0]))
    tempPosition = np.concatenate((babyPosition[0], daddyPosition[0]))

    newPosition = perturber(tempPosition, np.array([R / 2, 0, 0]))
    newVelocity = perturber(tempVelocity, np.array([-V / 2, 0, 0]))

    np.save(path + datePrefix + '200p-Myr-mass', np.array([newMass]))
    np.save(path + datePrefix + '200p-Myr-position', np.array([newPosition]))
    np.save(path + datePrefix + '200p-Myr-velocity', np.array([newVelocity]))

    m = np.load(path + datePrefix + '200p-Myr-mass.npy')
    v = np.load(path + datePrefix + '200p-Myr-velocity.npy')
    p = np.load(path + datePrefix + '200p-Myr-position.npy')

    print(np.shape(m), np.shape(v), np.shape(p))

    pass


App()
