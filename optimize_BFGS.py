from math import exp, sin
from scipy.optimize import minimize


def f(x):
    return sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)


def search_min(x0):
    res = minimize(f, x0, method='BFGS')
    return res['fun']

print(search_min(2), search_min(30))
