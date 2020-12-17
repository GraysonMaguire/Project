import numpy as np
from display import Display
from work import Work
from init import Data
# initial data
V = np.array([[0.0, 0.0, 0.0], [0.0, 29780, 0.0], [0.0, -13070, 0.0]])
P = np.array(
    [[0.0, 0.0, 0.0], [1.4960e11, 0.0, 0.0], [-7.7854e11, 0.0, 0.0]])
M = np.array([1.9889e30, 5.9742e24, 1.8986e27])
t = 100 * 370 * 24 * 60 * 60
dt = 10 * 24 * 60 * 60
epsilon = 0

# app


def App():

    data = Data(V, P, M, t, dt, epsilon)

    worker = Work(data.P0, data.V0, data.t, data.dt, data.M, data.epsilon)
    Positions, Velocitys, Forces, Energys = worker.numberCruncher()

    display = Display(Positions, Energys, data.t, data.dt, data.M)
    display.display()


App()
