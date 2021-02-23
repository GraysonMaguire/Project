import numpy as np
from time import time
from tqdm import tqdm


G = 6.674e-11
M0 = 2e32
year = 365.25 * 24 * 60 * 60

radiusOfCluster = 2e15
R = 3 * radiusOfCluster
V = np.sqrt(2 * G * M0 * 1 / R) * 0.1
dt = 10 * 24 * 60 * 60


def gForce(m1, m2, r1, r2):

    if m1 == 0 or m2 == 0:
        return result

    force = -m1 * m2 * G / ((r1 - r2)**2)

    return (force)


def nextVelocity(vPrev, f, m, dt):
    a = f * (1 / m)
    return vPrev + (a * dt)


def calcNextPosition(dPrev, v, dt):
    return dPrev + v * dt


P = R / 2
V = -V / 2


def iteration(P, V):
    F = gForce(M0, M0, P, -P)
    V = nextVelocity(V, F, M0, dt)
    P = calcNextPosition(P, V, dt)
    return P, V


time = 0
for i in tqdm(range(0, int(1000000 * year), dt)):
    P, V = iteration(P, V)
    time += dt
    if P < radiusOfCluster:
        break

    pass

print('time taken to collide: ', (time / year))
