from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt
import math


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


def approximation(x1, x2, x3, x4):
    factors = np.array([[1, x1, x1 ^ 2, x1 ^ 3], [1, x2, x2 ^ 2, x2 ^ 3],
                        [1, x3, x3 ^ 2, x3 ^ 3], [1, x4, x4 ^ 2, x4 ^ 3]])

    results = np.array([f(x1), f(x2), f(x3), f(x4)])
    file = open('output.txt', 'w')
    final_x = linalg.solve(factors, results)
    for i in final_x:
        file.write(str(i))
        file.write(' ')
    file.close()
