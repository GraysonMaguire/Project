from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm

# import raw position data here
# [iteration][particle][position]
pRaw = 0
plummerRadius = 9e13
path = f'/Users/garymagnum/Project/data/8-2-21-e13Crunch/8-2-21-150p-75por2000yr-10d-{plummerRadius}-results.npy'
pData = np.load(path, allow_pickle=True)[-3]
print(np.shape(pData))
R = 5e14


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
