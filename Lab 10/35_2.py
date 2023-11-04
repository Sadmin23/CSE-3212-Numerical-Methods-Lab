import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

x = [2, 3, 4, 5, 6, 7]
y = [12, 12, 32, 16, 22, 25]


def Quadratic_Spline():
    quadratic_interp = interp1d(x, y, kind="quadratic")
    x_new = np.linspace(2, 7, 100)

    y_quadratic = quadratic_interp(x_new)

    plt.scatter(x, y, label="Data Points")
    plt.plot(x_new, y_quadratic, label="Quadratic Spline", linestyle="--")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title("Quadratic Spline Interpolation")
    plt.grid(True)
    plt.show()


def Linear_Spline():
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    Quadratic_Spline()
    Linear_Spline()
