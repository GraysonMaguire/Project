from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm

# import raw position data here
# [iteration][particle][position]
pRaw = 0
plummerRadius = 9e13
path = '/Users/garymagnum/Project/hamData/23-2-21-200p-Myr-position.npy'
pData = np.load(
    '/Users/grays/Project/hamData/23-2-21-200p-Myr-position.npy')[0]
print(np.shape(pData))
R = 1e17


def xyzPostitionPlot(P=pData):

    fig = plt.figure(figsize=(5, 4))
    axis = fig.add_subplot(projection='3d')

    x = []
    y = []
    z = []

    for i in range(len(P)):
        x.append(P[i][0])
        y.append(P[i][1])
        z.append(P[i][2])

    axis.plot(x, y, z, 'o', lw=2)

    axis.set_xlabel("x")
    axis.set_ylabel("y")
    axis.set_zlabel('z')
    axis.set_xlim(-R, R)
    axis.set_ylim(-R, R)
    axis.set_zlim(-R, R)
    axis.set_title(
        "position")

    plt.show()
    pass


xyzPostitionPlot()
