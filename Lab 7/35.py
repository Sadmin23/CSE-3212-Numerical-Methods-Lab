import numpy as np


def f1(x, y, z):
    return x * x - 2 * x + y * y - z + 1


def f2(x, y, z):
    return x * y * y - x - 3 * y + y * z + 2


def f3(x, y, z):
    return x * z * z - 3 * z + y * z * z + x * y


def df11(x, y, z):
    return 2 * x - 2


def df12(x, y, z):
    return y * y - 1


def df13(x, y, z):
    return z * z + y


def df21(x, y, z):
    return 2 * y


def df22(x, y, z):
    return 2 * x * y - 3 + z


def df23(x, y, z):
    return z * z + x


def df31(x, y, z):
    return -1


def df32(x, y, z):
    return y


def df33(x, y, z):
    return 2 * x * z - 3 + 2 * y * z


def Multivariable_Newton_Raphson(x, y, z):
    A = np.array([x, y, z])
    B = np.array(
        [
            [df11(x, y, z), df21(x, y, z), df31(x, y, z)],
            [df12(x, y, z), df22(x, y, z), df32(x, y, z)],
            [df13(x, y, z), df23(x, y, z), df33(x, y, z)],
        ]
    )
    B = np.linalg.inv(B)
    C = np.array([f1(x, y, z), f2(x, y, z), f3(x, y, z)])
    D = A - np.dot(B, C)
    return D


if __name__ == "__main__":
    x0 = 1.0
    y0 = 2.0
    z0 = 3.0

    for i in range(1000):
        result = Multivariable_Newton_Raphson(x0, y0, z0)
        x1, y1, z1 = result[0], result[1], result[2]

        d1 = x0 + y0 + z0

        d2 = x1 + y1 + z1

        ae = abs(d2 - d1)

        rae = ae / d2

        print(
            f"Iteration {i}: \n{result}\nApprox. Error: {ae:.6f} Rel Approx. Error: {rae:.6f}\n"
        )

        x0 = x1
        y0 = y1
        z0 = z1

        if ae < 10e-8:
            break
