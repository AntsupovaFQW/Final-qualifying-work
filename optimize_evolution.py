from math import exp, sin
from scipy.optimize import differential_evolution


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


def search_min(bounds):
    res = differential_evolution(f, bounds)
    return res['fun']

print(search_min([(1, 30)]))
