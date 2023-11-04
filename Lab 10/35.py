import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 3, 4, 5, 6, 7])
y = np.array([12, 12, 32, 16, 22, 25])

ax = []
bx = []


def Linear_Spline():
    for i in range(len(x) - 1):
        a = x[i]
        b = x[i + 1]
        y1 = y[i]
        y2 = y[i + 1]
        A = np.array([[a, 1], [b, 1]])
        B = np.array([y1, y2])
        C = np.linalg.solve(A, B)
        C[0] = np.round(C[0])
        a1, a2 = C
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    Linear_Spline()
