import numpy as np
normal = np.linalg.norm


class Data(object):

    def __init__(self, R, N, M0, t, dt, epsilon, vMax, sunMass):

        # self.P0 = P0
        # self.V0 = V0
        self.R = R
        self.N = N
        # self.M = M
        self.M0 = M0
        self.t = t
        self.dt = dt
        self.epsilon = epsilon
        self.vMax = vMax
        self.a = 1e11
        self.G = 6.67e-11

    def spherToCart(self, spherical):
        r, theta, phi = spherical

        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        return(np.array([x, y, z]))

    def generateRandomSphericalPolars(self, max):

        costheta = np.random.uniform(-1, 1)
        u = np.random.random()

        phi = np.random.uniform(0, (2 * np.pi))
        theta = np.arccos(costheta)
        r = max * (u)**(1 / 3)

        return np.array([r, theta, phi])

    def plummerModelDistribution(self, r, v):
        e = self.energy(r, v)
        top = (24 * (np.sqrt(2)) * self.N * (self.a**2) * ((-e) ** 3.5))
        bottom = (7 * (np.pi**3) * (self.G**5) * (self.M0**5))

        return (top / bottom)

    def energy(self, r, v):
        e = (0.5 * (v)**2) - \
            ((self.G * self.M0) / (((r**2) + (self.a**2))**0.5))
        return 0 if e > 0 else e

    def generateData(self):
        V0 = np.full((self.N, 3), 0.0)
        P0 = np.full((self.N, 3), 0.0)
        M = np.full((self.N, 3), 0.0)
        roof = self.plummerModelDistribution(0, 0) * 1.1
        print(f'roof: {roof}')
        iteration = 0
        while iteration < self.N:
            pSpherical = self.generateRandomSphericalPolars(self.R)
            vSpherical = self.generateRandomSphericalPolars(self.vMax)
            f = self.plummerModelDistribution(pSpherical[0], vSpherical[0])
            # print(f'p: {pSpherical}, v: {vSpherical}, f: {f}')

            r = roof * np.random.random()
            if(r < f):
                print(f'current length of data: {iteration}')
                P0[iteration] = self.spherToCart(pSpherical)
                V0[iteration] = self.spherToCart(vSpherical)
                M[iteration] = self.M0 / self.N
                iteration += 1

        return (V0, P0, M)
