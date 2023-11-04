import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 3, 4, 5, 6, 7])
y = np.array([12, 12, 32, 16, 22, 25])


def A(a, b):
    return (b * b * b - a * a * a) / 3

if __name__ == "__main__":
