import matplotlib.pyplot as plt
import numpy as np

tolerance = 0.1

dx = []
av = []
av2 = []
av3 = []
av4 = []
av5 = []
trv = []


def fx(x):
    return x * x


def A(a, b):
    return (b * b * b - a * a * a) / 3


def Left_Reimann_Sum(h, a, b):
    sum = 0.0

    i = a
    while i < b:
        sum += fx(i)
        i += h

    return sum * h


def Right_Reimann_Sum(h, a, b):
    sum = 0.0

    i = a
    while i < b:
        sum += fx(i + h)
        i += h

    return sum * h


def Mid_Reimann_Sum(h, a, b):
    sum = 0.0

    i = a
    while i < b:
        m = i + h / 2
        sum += fx(m)
        i += h

    return sum * h


def Trapezium_Rule(h, a, b):
    sum = 0.0

    i = a
    while i < b:
        x = fx(i)
        y = fx(i + h)
        sum += (x + y) / 2
        i += h

    return sum * h


def Simpson_Rule(h, a, b):
    sum = 0.0

    i = a
    while i < b:
        x0 = i
        x1 = i + h
        x2 = i + 2 * h

        sum += (fx(x0) + 4 * fx((x0 + x1) / 2) + fx(x1)) / 6
        sum += (fx(x1) + 4 * fx((x1 + x2) / 2) + fx(x2)) / 6

        i += 2 * h

    return sum * h


def perform_integration():
    tv = A(0, 4)

    for it in range(1, 10001):
        h = it / 10000

        dx.append(h)
        trv.append(tv)

        ans_n = Left_Reimann_Sum(h, 0, 4)

        av.append(ans_n)

        print(f"dx = {h:.6f} a=0 b=4\n  Value = {ans_n:.6f}\n")


def perform_integration2():
    tv = A(0, 4)

    for it in range(1, 10001):
        h = it / 10000

        ans_n = Right_Reimann_Sum(h, 0, 4)
        av2.append(ans_n)

        print(f"dx = {h:.6f} a=0 b=4\n  Value = {ans_n:.6f}\n")


def perform_integration3():
    tv = A(0, 4)

    for it in range(1, 10001):
        h = it / 10000

        ans_n = Mid_Reimann_Sum(h, 0, 4)
        av3.append(ans_n)

        print(f"dx = {h:.6f} a=0 b=4\n  Value = {ans_n:.6f}\n")


def perform_integration4():
    tv = A(0, 4)

    for it in range(1, 10001):
        h = it / 10000

        ans_n = Trapezium_Rule(h, 0, 4)
        av4.append(ans_n)

        print(f"dx = {h:.6f} a=0 b=4\n  Value = {ans_n:.6f}\n")

def perform_integration5():
    tv = A(0, 4)

    for it in range(1, 10001):
        h = it / 10000

        ans_n = Simpson_Rule(h, 0, 4)
        av5.append(ans_n)

        print(f"dx = {h:.6f} a=0 b=4\n  Value = {ans_n:.6f}\n")

if __name__ == "__main__":
    print("\nLEFT REIMANN SUM:\n\n")
    perform_integration()
    print("\nRIGHT REIMANN SUM:\n\n")
    perform_integration2()
    print("\nMID REIMANN SUM:\n\n")
    perform_integration3()
    print("\nTRAPEZOID RULE:\n\n")
    perform_integration4()
    print("\nSIMPSON'S RULE:\n\n")
    perform_integration5()

    plt.plot(dx, trv, label="True Value")
    plt.plot(dx, av, label="Left Reimann Sum")
    plt.plot(dx, av2, label="Right Reimann Sum")
    plt.plot(dx, av3, label="Mid Reimann Sum")
    plt.plot(dx, av4, label="Trapezium Rule")
    plt.plot(dx, av5, label="Trapezium Rule")
    plt.xlabel("dx")
    plt.ylabel("Approx. Value")
    plt.title("Numerical Integration")
    plt.legend()
    plt.show()
