# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IThZ7HK8QFUTL-k2Ds37EGdf1tEMUWmB
"""

import matplotlib.pyplot as plt
import numpy as np


i_vals1 = range(26)
i_vals2 = range(11000)
err_vals = []
re_vals = []
err_vals1 = []
re_vals1 = []
err_vals2 = []
re_vals2 = []


def f(x):
    return x * x * x - x - 1


def x2_gen(a, fa, b, fb):
    return (a * fb - b * fa) / (fb - fa)


def bisection_method():
    x0 = 50
    x1 = -50

    for i in range(11000):
        fa = f(x0)
        fb = f(x1)
        x2 = (x0 + x1) / 2
        fc = f(x2)

        err = x1 - x2
        if x2:
            re = err / x2
        else:
            re = 0

        err_vals.append(err)
        re_vals.append(re)

        if i<26:
            err_vals1.append(err)
            re_vals1.append(re)

        if fc < 0:
            x1 = x2
        else:
            x0 = x2

    print(
         f"i={i} x0={x0:.6f} x1={x1:.6f} x2={x2:.6f} f(x0)={fa:.6f} f(x1)={fb:.6f} f(x2)={fc:.6f} err={err:.6f} re={re:.6f}"
    )


def false_method():
    x0 = 50
    x1 = -50

    for i in range(11000):
        fa = f(x0)
        fb = f(x1)
        x2 = x2_gen(x0, fa, x1, fb)
        fc = f(x2)

        err = x1 - x2

        if err >= 1 or err <= -1:
            err = 0

        re = err / x2

        err_vals2.append(err)
        re_vals2.append(re)

        print(
            f"i={i} x0={x0:.6f} x1={x1:.6f} x2={x2:.6f} f(x0)={fa:.6f} f(x1)={fb:.6f} f(x2)={fc:.6f} err={err:.6f} re={re:.6f}"
        )

        if fc < 0:
            x1 = x2
        elif fc < 0:
            x0 = x2

    return x2


if __name__ == "__main__":
    false_method()
    bisection_method()

    plt.bar(i_vals1, err_vals1)
    plt.xlabel("Iteration No.")
    plt.ylabel("Apprx. Error")
    plt.title("Bisection Method Approx. Error")
    plt.show()

    plt.bar(i_vals1, re_vals1)
    plt.xlabel("Iteration No.")
    plt.ylabel("Relative Error")
    plt.title("Bisection Method Relative Approx. Error")
    plt.show()

    plt.bar(i_vals2, err_vals2)
    plt.xlabel("Iteration No.")
    plt.ylabel("Apprx. Error")
    plt.title("False Method Approx. Error")
    plt.show()

    plt.bar(i_vals2, re_vals2)
    plt.xlabel("Iteration No.")
    plt.ylabel("Relative Error")
    plt.title("False Method Relative Approx. Error")
    plt.show()

    plt.plot(i_vals2, err_vals, label="Bisection Method")
    plt.plot(i_vals2, err_vals2, label="False Method")
    plt.xlabel("Iteration No.")
    plt.ylabel("Apprx. Error")
    plt.title("Bisection vs False method approx. error comparison")
    plt.legend()
    plt.show()

    plt.plot(i_vals2, re_vals, label="Bisection Method")
    plt.plot(i_vals2, re_vals2, label="False Method")
    plt.xlabel("Iteration No.")
    plt.ylabel("Error")
    plt.title("Bisection vs Falase method Relative approx. error comparison")
    plt.legend()
    plt.show()