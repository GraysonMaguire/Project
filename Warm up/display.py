from matplotlib import pyplot as plt
import numpy as np


class Display(object):

    def __init__(self,  P, V, F, t, dt, M):
        self.P = P
        #self.PHalf = PHalf
        self.V = V
        self.F = F
        self.t = t
        self.dt = dt
        self.M = M

    def readData(self):
        data = np.full((len(self.M), 3, len(self.P)), 0.0)
        for i in range(len(self.P)):
            for j in range(len(self.M)):
                data[j][0][i] = self.P[i][j][0]
                data[j][1][i] = self.P[i][j][1]
                data[j][2][i] = self.P[i][j][2]
        return data

    def postitionPlot(self):
        data = self.P
        for i in range(len(self.M)):
            x = data[i][0]
            y = data[i][1]

            plt.plot(x, y, label=str(i))

        plt.xlabel("x")
        plt.ylabel("y")
        plt.title(
            "position")
        plt.xlim()
        plt.ylim()
        plt.legend()
        plt.show()
