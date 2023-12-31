import matplotlib.pyplot as plt
import numpy as np
import time

it = []
error = []
rel_err = []
error2 = []
rel_err2 = []
time_count = []
time_count2 = []


def linear_iteration(n, matrix, result, tolerance=1e-8):
    x0 = np.zeros(n)
    x1 = np.zeros(n)

    start_timer = time.time()

    iteration = 0
    while True:
        for i in range(n):
            total_sum = np.dot(matrix[i], x0) - matrix[i][i] * x0[i]
            x1[i] = (result[i] - total_sum) / matrix[i][i]

        sum0 = np.sum(x0)
        sum1 = np.sum(x1)

        err = abs(sum1 - sum0)
        re = err / sum1

        current_time = (time.time() - start_timer) * 1000

        error.append(err)
        rel_err.append(re)
        time_count.append(current_time)
        it.append(iteration)

        print(
            f"Iteration {iteration}:",
            " ".join(f"x{i+1}={x:.6f}" for i, x in enumerate(x0)),
        )

        print(f"approx. error={err} rel. approx. error={re} time={current_time}ms\n")

        if re < tolerance:
            break

        x0 = x1.copy()
        iteration += 1


def compute_x(D, L, U, Di, x):
    ans = -np.dot(L + U, x)
    ans += result
    ans = np.dot(Di, ans)

    return ans


def matrix_iteration(n, matrix, result, tolerance=1e-8):
    x0 = np.zeros(n)

    Diagonal = np.diag(matrix)
    Lower = np.tril(matrix, k=-1)
    Upper = np.triu(matrix, k=1)
    D_inverse = np.diag(1.0 / Diagonal)

    start_timer = time.time()

    iteration = 0
    while True:
        x1 = compute_x(Diagonal, Lower, Upper, D_inverse, x0)

        sum0 = np.sum(x0)
        sum1 = np.sum(x1)

        err = abs(sum1 - sum0)
        re = err / sum1

        current_time = (time.time() - start_timer) * 1000

        error2.append(err)
        rel_err2.append(re)
        time_count2.append(current_time)

        print(
            f"Iteration {iteration}:",
            " ".join(f"x{i+1}={x:.6f}" for i, x in enumerate(x0)),
        )
        print(f"approx. error={err} rel. approx. error={re} time={current_time}ms\n")

        if re < tolerance:
            break

        x0 = x1.copy()
        iteration += 1


if __name__ == "__main__":
    n = int(input("Enter the value of n: "))

    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Enter row {i+1} of the matrix: ").split()))
        matrix.append(row)

    result = list(map(int, input("Enter the result vector: ").split()))

    linear_iteration(n, matrix, result)
    matrix_iteration(n, matrix, result)

    plt.plot(it, error, label="Without Matrix")
    plt.plot(it, error2, label="With Matrix")
    plt.xlabel("Iteration No.")
    plt.ylabel("Approx. Error")
    plt.title("Matrix vs Without Matrix error")
    plt.legend()
    plt.show()

    plt.plot(it, rel_err, label="Without Matrix")
    plt.plot(it, rel_err2, label="With Matrix")
    plt.xlabel("Iteration No.")
    plt.ylabel("Rel. Approx. Error")
    plt.title("Matrix vs Without Matrix error")
    plt.legend()
    plt.show()

    plt.plot(it, time_count, label="Without Matrix")
    plt.plot(it, time_count2, label="With Matrix")
    plt.xlabel("Iteration No.")
    plt.ylabel("Cummulative Time")
    plt.title("Matrix vs Without Matrix time comparison")
    plt.legend()
    plt.show()
