def f(x):
    return x * x * x - x - 1


def x2_gen(a, fa, b, fb):
    return (a * fb - b * fa) / (fb - fa)


def bisection_method():
    x0 = 50
    x1 = -50

    for i in range(500):
        fa = f(x0)
        fb = f(x1)
        x2 = (x0 + x1) / 2
        fc = f(x2)

        if fc < 0:
            x1 = x2
        else:
            x0 = x2

        print(
            f"i={i} x0={x0:.6f} x1={x1:.6f} x2={x2:.6f} f(x0)={fa:.6f} f(x1)={fb:.6f} f(x2)={fc:.6f}"
        )


def false_method():
    x0 = 50
    x1 = -50

    for i in range(10000):
        fa = f(x0)
        fb = f(x1)
        x2 = x2_gen(x0, fa, x1, fb)
        fc = f(x2)

        if fc * fa < 0:
            x1 = x2
        elif fc * fb < 0:
            x0 = x2

        print(
            f"i={i} x0={x0:.6f} x1={x1:.6f} x2={x2:.6f} f(x0)={fa:.6f} f(x1)={fb:.6f} f(x2)={fc:.6f}"
        )


if __name__ == "__main__":
    print(false_method())
    print(bisection_method())
