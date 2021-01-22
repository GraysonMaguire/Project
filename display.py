from matplotlib import pyplot as plt
from matplotlib import animation
# import mpl_toolkits.mplot3d.axes3d as p3
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
        ax = fig.add_subplot(projection='3d')

        lim = self.R * 2
        ax.grid()

        particleLine, = ax.plot([], [], [], 'o', lw=2)
        P1Line, = ax.plot([], [], [], 'o', lw=2, color='red')
        time_template = 'time = %.1fyears'
        # time_text = ax.text(0.05, 0.9, 'yes', fontdict=None,
        #                     transform=ax.transAxes)

        ax.set_xlim3d([-lim, lim])
        ax.set_xlabel('X')

        ax.set_ylim3d([-lim, lim])
        ax.set_ylabel('Y')

        ax.set_zlim3d([-lim, lim])
        ax.set_zlabel('Z')

        def update_time():
            t = 0
            t_max = int(self.t / self.dt)
            while t < t_max:
                newT = t + anim.direction
                if(np.abs(newT) < t_max):
                    t += anim.direction
                else:
                    t = t_max - 1
                yield t

        def animateP1(i):
            thisx = self.P[0][0][i]
            thisy = self.P[0][1][i]
            thisz = self.P[0][2][i]

            P1Line.set_data_3d(thisx, thisy, thisz)

            return animP1

        def animateParticles(i):
            thisx = []
            thisy = []
            thisz = []
            for particle in self.P:
                thisx.append(particle[0][i])
                thisy.append(particle[1][i])
                thisz.append(particle[2][i])

            particleLine.set_data_3d(thisx, thisy, thisz)
            ax.set_title(time_template % (i * self.dt / self.year))

            return particleLine

        def on_press(event):
            if event.key.isspace():
                if anim.running:
                    anim.event_source.stop()
                    animP1.event_source.stop()

                else:
                    anim.event_source.start()
                    animP1.event_source.start()
                anim.running ^= True
            elif event.key == 'a':
                anim.direction += -1
                ax.legend([anim.direction])

                # animP1.direction += -1
            elif event.key == 'd':
                anim.direction += +1
                ax.legend([anim.direction])
                # animP1.direction += +1

        fig.canvas.mpl_connect('key_press_event', on_press)
        animP1 = animation.FuncAnimation(
            fig, animateP1, frames=update_time, interval=100, blit=False, repeat=True)
        anim = animation.FuncAnimation(
            fig, animateParticles, frames=update_time, interval=100, blit=False, repeat=True)
        anim.running = True
        animP1.running = True
        anim.direction = +1
        ax.legend([anim.direction])

        plt.show()
        pass

    def display(self):

        fig, axis = plt.subplots(2, 2)
        self.xyPostitionPlot(axis[0, 0])

        plt.show()
