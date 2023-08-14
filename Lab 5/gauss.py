import numpy as np

ITERATION_LIMIT = 1000

A = np.array(
    [
        [10.0, -1.0, 2.0, 0.0],
        [-1.0, 11.0, -1.0, 3.0],
        [2.0, -1.0, 10.0, -1.0],
        [0.0, 3.0, -1.0, 8.0],
    ]
)

b = np.array([6.0, 25.0, -11.0, 15.0])

x = np.zeros_like(b, np.float_)
for it_count in range(1, ITERATION_LIMIT):
    x_new = np.zeros_like(x, dtype=np.float_)
    print(f"Iteration {it_count}: {x}")
    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]
    if np.allclose(x, x_new, rtol=1e-8):
        break
    x = x_new

print(f"Solution: {x}")
error = np.dot(A, x) - b
print(f"Error: {error}")
