from matplotlib import pyplot as plt
import numpy as np


class Display(object):

    def __init__(self, P, E, t, dt, M):
        self.P = P
        self.E = E
        self.t = int(t)
        self.dt = dt
        self.M = M
        self.year = 365 * 24 * 3600
        self.au = 149597871000
        self.orbitLabels = [0, 20, 40, 60, 80, 100]

    def energyPlot(self, axis):
        T, KE, PE = self.E
        time = range(0, self.t, self.dt)
        orbits = range(0, self.t + 20 * self.year, 20 * self.year)

        axis.plot(time, T, label='Total Energy')
        axis.plot(time, KE, label='Kinetic Energy')
        axis.plot(time, PE, label='Potential Energy')

        axis.set_ylabel("Energy/J")
        axis.set_xlabel("time/s")
        axis.set_xticks(orbits)
        axis.set_xticklabels(self.orbitLabels)
        axis.set_xlim(0, 100 * self.year)
        axis.set_title(
            "Energies")

        axis.legend()
        return axis

    def energyPercentagePlot(self, axis):
        T = self.E[0]
        TPercent = 100 * T / T[0]
        time = range(0, self.t, self.dt)
        orbits = range(0, self.t + 20 * self.year, 20 * self.year)

        axis.plot(time, TPercent)
        axis.set_ylabel("Total energy/%")
        axis.set_xlabel("Orbits")
        axis.set_title(
            "% of total energy")
        axis.set_xticks(orbits)
        axis.set_xticklabels(self.orbitLabels)
        axis.set_xlim(0, 100 * self.year)
        axis.set_ylim(99.5, 100.5)
        return axis

    def xyPostitionPlot(self, axis):
        data = self.P

        for i in range(len(self.M)):
            x = data[i][0]
            y = data[i][1]

            axis.plot(x, y)

        axis.set_xlabel("x")
        axis.set_ylabel("y")
        axis.set_title(
            "position")
        axis.set_xlim()

        axis.set_ylim()
        axis.legend()
        return axis

    def distanceBetween(self, axis):
        R = np.zeros(len(self.P[0][0]))

        for i in range(len(self.P[0][0])):

            R[i] = ((self.P[0][0][i] - self.P[1][0][i])**2 +
                    (self.P[0][1][i] - self.P[1][1][i])**2)**0.5

        time = range(0, self.t, self.dt)
        orbits = range(0, self.t + 20 * self.year, 20 * self.year)

        axis.plot(time, R)
        axis.set_xlabel("time/t")
        axis.set_ylabel("ditance/Au")
        axis.set_title(
            "distance between")
        axis.set_xticks(orbits)
        axis.set_xticklabels(self.orbitLabels)
        axis.set_yticks([0.9 * self.au, 0.95 * self.au,
                         self.au, 1.05 * self.au, 1.1 * self.au, 1.15 * self.au])
        axis.set_yticklabels([0.90, 0.95, 1.00, 1.05, 1.10, 1.15])
        axis.set_xlim(0, 100 * self.year)
        axis.set_ylim()

        return axis

    def display(self):

        fig, axis = plt.subplots(2, 2)
        self.xyPostitionPlot(axis[0, 0])

        plt.show()
