def f(x):
    return x * x * x - x - 1


def x2_gen(a, fa, b, fb):
    return (a * fb - b * fa) / (fb - fa)


def bisection_method():
    x0 = 50
    x1 = -50

    for i in range(20):
        fa = f(x0)
        fb = f(x1)
        x2 = (x0 + x1) / 2
        fc = f(x2)

        if fc < 0:
            x1 = x2
        else:
            x0 = x2

        print(x2)


def false_method():
    x0 = 50
    x1 = -50

    for i in range(10000):
        fa = f(x0)
        fb = f(x1)
        x2 = x2_gen(x0, fa, x1, fb)
        fc = f(x2)

        print(x2)

        if fc < 0:
            x1 = x2
        else:
            x0 = x2


if __name__ == "__main__":
    #    bisection_method()
    false_method()
