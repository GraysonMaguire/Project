from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class Display(object):

    def __init__(self, P, E, t, dt, M, R):
        self.P = P
        self.E = E
        self.t = int(t)
        self.dt = dt
        self.M = M
        self.R = R
        self.year = 365 * 24 * 3600
        self.au = 149597871000
        self.orbitLabels = [0, 20, 40, 60, 80, 100]

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

    def xyAnimation(self):
        fig = plt.figure(figsize=(5, 4))

        lim = self.R * 10
        ax = fig.add_subplot(111, autoscale_on=True,
                             xlim=(-lim, lim), ylim=(-lim, lim))
        ax.set_aspect('equal')
        ax.grid()

        line, = ax.plot([], [], 'o', lw=2)
        time_template = 'time = %.1fs'
        time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

        def animate(i):
            thisx = []
            thisy = []
            for particle in self.P:
                thisx.append(particle[0][i])
                thisy.append(particle[1][i])

            line.set_data(thisx, thisy)
            time_text.set_text(time_template % (i * self.dt))

            return line, time_text
        ani = animation.FuncAnimation(
            fig, animate, int(self.t / self.dt), interval=100, blit=False)

        plt.show()
        pass

    def display(self):

        fig, axis = plt.subplots(2, 2)
        self.xyPostitionPlot(axis[0, 0])

        plt.show()
