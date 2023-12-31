import matplotlib.pyplot as plt
import numpy as np
import time

ITERATION_LIMIT = 30
TOLERANCE = 1e-10

i_vals = []
err_vals = []
re_vals = []
time_vals1 = []
time_vals2 = []

A = np.array(
    [
        [4, -1, -1],
        [-2, 6, 1],
        [-1, 1, 7],
    ]
)

b = np.array([3, 9, -6])


def linear():
    n = len(b)
    x = np.zeros(n)

    start = time.time()

    for it_count in range(ITERATION_LIMIT):
        x_new = np.zeros(n)

        for i in range(n):
            s = 0.0
            for j in range(n):
                if j != i:
                    s += A[i, j] * x[j]
            x_new[i] = (b[i] - s) / A[i, i]

        sm1 = np.sum(x)
        sm2 = np.sum(x_new)

        err = abs(sm2 - sm1)
        re = err / sm2

        current = time.time() - start

        err_vals.append(err)
        re_vals.append(re)
        time_vals1.append(current)
        i_vals.append(it_count)

        print(
            f"Iteration {it_count}: {x} Err: {err:.6f} Rel Err: {re:.6f} Time: {current:.6f}"
        )

        if np.linalg.norm(x_new - x) < TOLERANCE:
            break

        x = x_new.copy()


def matrix():
    n = len(b)
    x = np.zeros(n)

    D = np.diag(A)
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    D_inv = np.diag(1.0 / D)

    start = time.time()

    for it_count in range(ITERATION_LIMIT):
        x_new = np.dot(D_inv, -np.dot(L + U, x) + b)

        sm1 = np.sum(x)
        sm2 = np.sum(x_new)

        err = abs(sm2 - sm1)
        re = err / sm2

        current = time.time() - start

        time_vals2.append(current)

        print(
            f"Iteration {it_count}: {x} Err: {err:.6f} Rel Err: {re:.6f} Time: {current:.6f}"
        )

        if np.linalg.norm(x_new - x) < TOLERANCE:
            break

        x = x_new.copy()


if __name__ == "__main__":
    linear()
    matrix()

    plt.plot(i_vals, err_vals)
    plt.xlabel("Iteration No.")
    plt.ylabel("Apprx. Error")
    plt.title("Approx. error comparison")
    plt.show()

    plt.plot(i_vals, re_vals)
    plt.xlabel("Iteration No.")
    plt.ylabel("Rel. Apprx. Error")
    plt.title("Rel Approx. error comparison")
    plt.show()

    plt.plot(i_vals, time_vals1, label="Without Matrix")
    plt.plot(i_vals, time_vals2, label="With Matrix")
    plt.xlabel("Iteration No.")
    plt.ylabel("Cummulative Time")
    plt.title("Matrix vs Without Matrix time comparison")
    plt.legend()
    plt.show()
