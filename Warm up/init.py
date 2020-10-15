import numpy as np
normal = np.linalg.norm


class Data(object):

    def __init__(self, V, P, M, t, dt, epsilon):
        F0 = self.calcF0(P, M, epsilon)
        V0 = self.calcV0(V, F0, M, dt)
        self.V0 = V0
        self.P0 = P
        self.M = M
        self.t = t
        self.dt = dt
        self.epsilon = epsilon

    def prevVelocity(self, v, f, m, dt):
        a = f * (1 / m)
        return v - (a * dt)

    def calcV0(self, V, F, M, dt):

        V0 = np.full_like(V, 0.0)
        for i in range(len(M)):
            V0[i] = self.prevVelocity(V[i], F[i], M[i], dt)

        return V0

    def gForce(self, m1, m2, r1, r2, epsilon):
        force = -m1 * m2 * 6.674e-11 * \
            ((r1 - r2) / (normal(r1 - r2)**2 + epsilon**2)**1.5)
        return (force)

    def calcF0(self, P, M, epsilon):

        forces = np.full((len(P), 3), 0.0)
        y = 0
        x = 1
        for i in range(len(P) - 1):
            while x < len(P):
                force = self.gForce(M[x], M[y], P[x], P[y], epsilon)
                forces[x] += force
                forces[y] -= force
                x += 1
            y += 1
            x = y + 1
        return forces
