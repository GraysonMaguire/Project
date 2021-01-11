import numpy as np
normal = np.linalg.norm


class Data(object):

    def __init__(self, R, N, m, t, dt, epsilon, vMax, sunMass):
        P0 = self.generateP0(R, N)
        V0 = self.generateV0(vMax, N)
        M = self.generateM(N, m, sunMass)

        self.P0 = P0
        self.V0 = V0
        self.R = R
        self.N = N
        self.M = M
        self.t = t
        self.dt = dt
        self.epsilon = epsilon
        self.vMax = vMax

    def spherToCart(self, r, theta, phi):
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        return(np.array([x, y, z]))

    def generateP0(self, R, N):

        P0 = np.zeros((N, 3))
        for i in range(N):
            costheta = np.random.uniform(-1, 1)
            u = np.random.random()

            phi = np.random.uniform(0, (2 * np.pi))
            theta = np.arccos(costheta)
            r = R * (u)**(1 / 3)
            # print(r, theta, phi)
            P0[i] = self.spherToCart(r, theta, phi)
        P0[0] = np.array([1, 0, 0])
        return P0

    def generateV0(self, vMax, N):

        V0 = np.zeros((N, 3))
        for i in range(N):
            costheta = np.random.uniform(-1, 1)
            u = np.random.random()

            phi = np.random.uniform(0, (2 * np.pi))
            theta = np.arccos(costheta)
            v = vMax * (u)**(1 / 3)

            V0[i] = self.spherToCart(v, theta, phi)
        V0[0] = np.array([0, 0, 0])
        return V0

    def generateM(self, N, m, sunMass):
        M = np.full((N), m, dtype='float')
        M[0] = sunMass
        return M
