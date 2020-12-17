from matplotlib import pyplot as plt
import numpy as np


class Display(object):

    def __init__(self, P, E, t, dt, M, steps):
        self.P = P
        self.E = E
        self.t = t
        self.dt = dt
        self.M = M
        self.steps = steps

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

        dataX = self.P[0]
        dataY = self.P[1]

        for i in range(len(dataX)):
            x = dataX[i]
            y = dataY[i]

            axis.scatter(x, y, label=('step: ' + str(i)))

        axis.set_xlabel("x")
        axis.set_ylabel("y")
        axis.set_title(
            "position")
        axis.set_xlim()
        axis.set_ylim()
        axis.legend()
        return axis

    def display(self):
        fig, axis = plt.subplots(2, 2)
        self.xyPostitionPlot(axis[0, 0])
        self.xyPostitionPlot(axis[0, 1])
        self.energyPlot(axis[1, 0])
        self.energyPercentagePlot(axis[1, 1])
        plt.show()
