from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
from tqdm import tqdm

# import raw position data here
# [iteration][particle][position]
pRaw = 0

pData = np.load('../data/30-1-21-150p-2000y-10d-baby-position.npy')


def reshapeData(data):
    totalSteps = len(data[0][0])
    Dimensions = len(data[0])
    totalParticles = len(data)

    newData = np.full((totalSteps, totalParticles, Dimensions), 0.0)

    for i in tqdm(range(totalSteps)):
        for j in range(Dimensions):
            for k in range(totalParticles):
                newData[i][k][j] = data[k][j][i]

    return newData


pData = reshapeData(pData)


def xyzPostitionPlot(P=pData[-1]):

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
    axis.set_title(
        "position")

    plt.show()
    pass


xyzPostitionPlot()
