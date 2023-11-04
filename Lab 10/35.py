import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 3, 4, 5, 6, 7])
y = np.array([12, 12, 32, 16, 22, 25])

ax = []
bx = []


def Linear_Spline():
    plt.plot(x, y)
    plt.show()


def Quadratic_Spline():
    A = np.zeros((15, 15))

    print(A)

    A[0, :3] = [4, 2, 1]
    A[1, :3] = [9, 3, 1]
    A[2, 3:6] = [9, 3, 1]
    A[3, 3:6] = [16, 4, 1]
    A[4, 6:9] = [16, 4, 1]
    A[5, 6:9] = [25, 5, 1]
    A[6, 9:12] = [25, 5, 1]
    A[7, 9:12] = [36, 6, 1]
    A[8, 12:15] = [36, 6, 1]
    A[9, 12:15] = [49, 7, 1]
    A[10, :2] = [9, 1]
    A[10, 3:5] = [-9, -1]
    A[11, 3:5] = [16, 1]
    A[11, 6:8] = [-16, -1]
    A[12, 6:8] = [25, 1]
    A[12, 9:11] = [-25, -1]
    A[13, 9:11] = [36, 1]
    A[13, 12:14] = [-36, -1]
    A[14, 0] = 1

    A = A.astype(int)
    print(A)


if __name__ == "__main__":
    Quadratic_Spline()
