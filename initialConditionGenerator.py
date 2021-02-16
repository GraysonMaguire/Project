import numpy as np
from time import time
from tqdm import tqdm

path = '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/'

babyMass = np.load(
    '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/baby/16-2-21-100p-baby-mass.npy')
babyPosition = np.load(
    '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/baby/16-2-21-100p-baby-position.npy')
babyVelocity = np.load(
    '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/baby/16-2-21-100p-baby-velocity.npy')

daddyMass = np.load(
    '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/daddy/16-2-21-100p-daddy-mass.npy')
daddyPosition = np.load(
    '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/daddy/16-2-21-100p-daddy-position.npy')
daddyVelocity = np.load(
    '/Users/garymagnum/Project/data/16-2-21-CollisionCrunch/daddy/16-2-21-100p-daddy-velocity.npy')

t = 60000 * 365.25 * 24 * 60 * 60
M0 = 2e32
G = 6.67e-11

R = ((t**2) * 16 * M0 * G / (np.pi**2))**(1 / 3)


def perturber(array, pertubation):

    print(int(len(array) / 2))
    for i in range(int(len(array) / 2)):
        array[i] = array[i] - pertubation
        array[-(i + 1)] = array[-(i + 1)] + pertubation

    return array


def App():
    newMass = np.concatenate((babyMass, daddyMass))

    tempVelocity = np.concatenate((babyVelocity, daddyVelocity))
    tempPosition = np.concatenate((babyPosition, daddyPosition))

    newPosition = perturber(tempPosition, np.array([R / 2, 0, 0]))
    newVelocity = perturber(tempVelocity, np.array([-100, 0, 0]))

    np.save(path + '16-2-21-200p-Myr-mass', np.array([newMass]))
    np.save(path + '16-2-21-200p-Myr-position', np.array([newPosition]))
    np.save(path + '16-2-21-200p-Myr-velocity', np.array([newVelocity]))

    m = np.load(path + '16-2-21-200p-Myr-mass.npy')
    v = np.load(path + '16-2-21-200p-Myr-velocity.npy')
    p = np.load(path + '16-2-21-200p-Myr-position.npy')

    print(np.shape(m), np.shape(v), np.shape(p))

    pass


App()
