import numpy as np

tolerance = 0.30


def fx(x):
    return x * x


def A(a, b):
    return (b * b * b - a * a * a) / 3


def Left_Reimann_Sum(n, a, b):
    h = (b - a) / n

    sum = 0.0

    i = a
    while i <= b:
        sum += fx(i)
        i += h

    return sum * h


def Right_Reimann_Sum(n, a, b):
    h = (b - a) / n

    sum = 0.0

    i = a
    while i <= b:
        sum += fx(i + h)
        i += h

    return sum * h


def Mid_Reimann_Sum(n, a, b):
    h = (b - a) / n

    sum = 0.0

    i = a
    while i <= b:
        m = i + h / 2
        sum += fx(m)
        i += h

    return sum * h


def Trapezium_Rule(n, a, b):
    h = (b - a) / n

    sum = 0.0

    i = a
    while i <= b:
        x = fx(i)
        y = fx(i + h)
        sum += (x + y) / 2
        i += h

    return sum * h


def perform_integration(arg):
    tv = A(5, 15)
    ans_p = 0

    for it in range(1, 10000):
        if arg == 0:
            ans_n = Left_Reimann_Sum(it, 5, 15)

        elif arg == 1:
            ans_n = Right_Reimann_Sum(it, 5, 15)

        elif arg == 2:
            ans_n = Mid_Reimann_Sum(it, 5, 15)

        elif arg == 3:
            ans_n = Trapezium_Rule(it, 5, 15)

        te = abs(tv - ans_n)
        rte = te / tv

        print(
            f"Iteration {it}:   Value = {ans_n:.6f}   True Error = {te:.6f}   Rel. True Error = {rte:.6f}"
        )

        if it > 1:
            ae = abs(ans_n - ans_p)
            rae = ae / ans_n
            print(f"Approx. Error = {ae:.6f}   Rel. Approx. Error = {rae:.6f}\n")

        else:
            print("\n")

        ans_p = ans_n

        if te < tolerance:
            break


if __name__ == "__main__":
    perform_integration(3)
