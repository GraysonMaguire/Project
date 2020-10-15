import numpy as np
normal = np.linalg.norm


class Data(object):

    def __init__(self, R, N, m, t, dt, epsilon):
        P0 = self.generateP0(R, N)
        self.V0 = np.zeros((N, 3))
        self.P0 = P0
        self.M = np.full(N, m)
        self.t = t
        self.dt = dt
        self.epsilon = epsilon

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

        return P0
