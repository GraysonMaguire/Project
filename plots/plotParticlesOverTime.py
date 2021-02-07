from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm
# verbose functions
normal = np.linalg.norm

# P = np.load('../position.npy')
# V = np.load('../velocity.npy')
# F = np.load('../force.npy')
# M = np.load('../baby/babyM.npy')
PE = np.load('../data/30-1-21-150p-2000y-10d-daddy-PE.npy')
KE = np.load('../data/30-1-21-150p-2000y-10d-daddy-KE.npy')


def particlesOverTime():
    fig, axis = plt.subplots()
    T = KE + PE

    iterations = len(T)

    particlesOverTime = []

    indexOfEscapedParticles = []

    for step in tqdm(range(iterations)):
        N = len(T[0])
        for particle in range(N):

            # if particle in indexOfEscapedParticles:
            #     N = N - 1
            #     continue

            if T[step][particle] >= 0:
                N = N - 1
                indexOfEscapedParticles.append(particle)

        particlesOverTime.append(N)

    axis.plot(particlesOverTime)
    print('final number of particles is', particlesOverTime[-1])

    plt.show()
    pass


particlesOverTime()
