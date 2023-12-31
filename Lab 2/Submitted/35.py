# -*- coding: utf-8 -*-
"""35.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XYZcNpP95dnz4ADMlqIPbKI9AHGM6AZ3
"""

import matplotlib.pyplot as plt
import numpy as np

i_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
err_vals = []
re_vals = []
err_vals2 = []
re_vals2 = []


def f(x):
    return x * x * x - x - 1


def secant_method():
    x_i0 = 50
    x_i1 = 48

    for i in range(20):
        f_x_i0 = f(x_i0)
        f_x_i1 = f(x_i1)
        d_f_x_i = (f_x_i1 - f_x_i0) / (x_i1 - x_i0)

        x_i2 = x_i1 - f_x_i1 / d_f_x_i
        err = x_i1 - x_i2
        re = err / x_i2

        err_vals.append(err)
        re_vals.append(re)

        print(f"i = {i + 1}")
        print(f"xi-1 = {x_i0:.6f}, f(xi-1) = {f_x_i0:.6f}")
        print(f"xi = {x_i1:.6f}, f(xi) = {f_x_i1:.6f}, f'(xi) = {d_f_x_i:.6f}")
        print(f"xi+1 = {x_i2:.6f}")
        print(f"approx. error = {err:.6f}")
        print(f"rel. approx. error = {re:.6f}\n")

        x_i0 = x_i1
        x_i1 = x_i2


def newtons_raphson():
    x_i = 50

    for i in range(20):
        f_x_i = x_i * x_i * x_i - x_i - 1

        d_f_x_i = 3 * x_i * x_i - 1

        x_i1 = x_i - f_x_i / d_f_x_i

        err = x_i - x_i1
        re = err / x_i1

        err_vals2.append(err)
        re_vals2.append(re)

        print(f"i = {i + 1}")
        print(f"xi = {x_i:.6f}")
        print(f"f(xi) = {f_x_i:.6f}")
        print(f"f'(xi) = {d_f_x_i:.6f}")
        print(f"xi+1 = {x_i1:.6f}")
        print(f"approx. error = {err:.6f}")
        print(f"rel. approx. error = {re:.6f}\n")

        x_i = x_i1


if __name__ == "__main__":
    secant_method()
    newtons_raphson()
    plt.bar(i_vals, err_vals)
    plt.xlabel("Iteration No.")
    plt.ylabel("Apprx. Error")
    plt.title("Secant Method Approx. Error")
    plt.show()

    plt.bar(i_vals, re_vals)
    plt.xlabel("Iteration No.")
    plt.ylabel("Relative Error")
    plt.title("Secant Method Relative Approx. Error")
    plt.show()

    plt.plot(i_vals, err_vals, label="Secant Method")
    plt.plot(i_vals, err_vals2, label="Newton-Raphson Method")
    plt.xlabel("Iteration No.")
    plt.ylabel("Apprx. Error")
    plt.title("Secant vs Newton-Raphson's method approx. error comparison")
    plt.legend()
    plt.show()

    plt.plot(i_vals, re_vals, label="Secant Method")
    plt.plot(i_vals, re_vals2, label="Newton-Raphson Method")
    plt.xlabel("Iteration No.")
    plt.ylabel("Error")
    plt.title("Secant vs Newton-Raphson's method Relative approx. error comparison")
    plt.legend()
    plt.show()