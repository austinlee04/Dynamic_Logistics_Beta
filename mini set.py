import numpy as np
import matplotlib.pyplot as plt

x, y = [],[]
while True :
    for i in range(13):
        x.append(np.random.randint(1, 100))
        y.append(np.random.randint(1, 100))

    print(x)
    print(y)
    plt.scatter(x, y)
    plt.show()

    a = input()
    if a == 'y' :
        break
    del x[:]
    del y[:]
