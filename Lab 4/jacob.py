import matplotlib.pyplot as plt
import numpy as np
import time

iteration = 28
n = 3

matrix = [[4, -1, -1], [-2, 6, 1], [-1, 1, 7]]

result = [3, 9, -6]


def linear_iteration():
    x0 = [0, 0, 0]
    x1 = [0, 0, 0]

    for k in range(iteration):
        for i in range(n):
            total_sum = 0

            for j in range(n):
                if i != j:
                    total_sum += matrix[i][j] * x0[j]

            x1[i] = (result[i] - total_sum) / matrix[i][i]

        print(f"{x0[0]} {x0[1]} {x0[2]}")

        x0 = x1.copy()


def compute_x(D, L, U, Di, x):
    ans = -np.dot(L + U, x)
    ans += result
    ans = np.dot(Di, ans)

    return ans


def matrix_iteration():
    x0 = [0, 0, 0]

    Diagonal = np.diag(matrix)
    Lower = np.tril(matrix, k=-1)
    Upper = np.triu(matrix, k=1)
    D_inverse = np.diag(1.0 / Diagonal)

    for k in range(iteration):
        x1 = compute_x(Diagonal, Lower, Upper, D_inverse, x0)

        print(f"{x0[0]} {x0[1]} {x0[2]}")

        x0 = x1.copy()


if __name__ == "__main__":
    linear_iteration()
    matrix_iteration()
