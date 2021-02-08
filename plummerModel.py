import numpy as np
from numba import njit


G = 6.67e-11


@njit
def spherToCart(spherical):
    r, theta, phi = spherical

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    return(np.array([x, y, z]))


# spherToCart(np.array([1, 0, 0]))


@njit
def generateRandomSphericalPolars(max):

    costheta = np.random.uniform(-1, 1)
    u = np.random.random()

    phi = np.random.uniform(0, (2 * np.pi))
    theta = np.arccos(costheta)
    r = max * (u)**(1 / 3)

    return np.array([r, theta, phi])


# generateRandomSphericalPolars(1)

@njit
def energy(r, v, M0, plummerRadius):
    e = (0.5 * (v)**2) - \
        ((G * M0) / (((r**2) + (plummerRadius**2))**0.5))
    return 0 if e > 0 else e


@njit
def plummerModelDistribution(r, v, N, plummerRadius, M0):
    e = energy(r, v, M0, plummerRadius)
    top = (24 * (np.sqrt(2)) * N *
           (plummerRadius**2) * ((-e) ** 3.5))
    bottom = (7 * (np.pi**3) * (G**5) * (M0**5))

    return (top / bottom)


# plummerModelDistribution(1, 1, 100, 1e11, 1e32)


@njit
def plummerModel(N, M0, plummerRadius):
    print('initilizing plummerModel function')

    R = 2 * plummerRadius
    G = 6.67e-11
    vMax = np.sqrt(2 * G * M0 / plummerRadius)

    V0 = np.full((N, 3), 0.0)
    P0 = np.full((N, 3), 0.0)
    M = np.full((N, 3), 0.0)

    roof = plummerModelDistribution(0, 0, N, plummerRadius, M0) * 1.1

    iteration = 0
    print('START plummerModel')

    while iteration < N:
        pSpherical = generateRandomSphericalPolars(R)
        vSpherical = generateRandomSphericalPolars(vMax)
        f = plummerModelDistribution(
            pSpherical[0], vSpherical[0], N, plummerRadius, M0)

        r = roof * np.random.random()

        if(r < f):
            P0[iteration] = spherToCart(pSpherical)
            V0[iteration] = spherToCart(vSpherical)
            M[iteration] = M0 / N

            iteration += 1

    print('FINISH plummerModel')

    return (V0, P0, M)


N = 150
M0 = 3e32  # total mass of cluster
plummerRadius = 1e11

plummerModel(1, M0, plummerRadius)

plummerModel(N, M0, plummerRadius)
