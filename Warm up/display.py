from matplotlib import pyplot as plt
import numpy as np


class Display(object):

    def __init__(self, P, E, t, dt, M):
        self.P = P
        self.E = E
        self.t = t
        self.dt = dt
        self.M = M

    def energyPlot(self, axis):
        T, KE, PE = self.E
        time = range(0, self.t, self.dt)
        axis.plot(time, T, label='Total Energy')
        axis.plot(time, KE, label='Kinetic Energy')
        axis.plot(time, PE, label='Potential Energy')

        axis.set_ylabel("Energy/J")
        axis.set_xlabel("time/s")
        axis.set_title(
            "Energies")

        axis.legend()
        return axis

    def energyPercentagePlot(self, axis):
        T = self.E[0]
        TPercent = 100 * T / T[0]
        time = range(0, self.t, self.dt)

        axis.plot(time, TPercent)
        axis.set_ylabel("% of initial Total energy")
        axis.set_xlabel("time/s")
        axis.set_title(
            "% of total energy")
        axis.set_xlim()
        axis.set_ylim(95, 105)
        return axis

    def xyPostitionPlot(self, axis):
        data = self.P
        labels = ['Sun', 'Earth', 'Jupiter']
        for i in range(len(self.M)):
            x = data[i][0]
            y = data[i][1]

            axis.plot(x, y, label=labels[i])

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
        axis.plot(time, R)
        axis.set_xlabel("time/t")
        axis.set_ylabel("ditance/m")
        axis.set_title(
            "distance between")
        axis.set_xlim()
        axis.set_ylim()

        return axis

    def display(self):
        fig, axis = plt.subplots(2, 2)
        self.xyPostitionPlot(axis[0, 0])
        self.distanceBetween(axis[0, 1])
        self.energyPlot(axis[1, 0])
        self.energyPercentagePlot(axis[1, 1])
        plt.show()
