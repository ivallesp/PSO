import sys
import numpy as np


def get_test_function(name):
    try:
        f = getattr(sys.modules[__name__], name)
    except AttributeError:
        raise ValueError(f"Function {name} not found in functions.py")
    return f


def bowl(x, y):
    return x ** 2 + y ** 2


def rosenbrock(x, y):
    return 100 * (y - x ** 2) ** 2 + (1 - x) ** 2


def beale(x, y):
    return (
        1
        + (1.5 - x + x * y) ** 2
        + (2.25 - x + x * y ** 2) ** 2
        + (2.625 - x + x * y ** 3) ** 2
    ) / 10


def rastrigin(x, y):
    return (
        20 + x ** 2 - 10 * np.cos(2 * np.pi * x) + y ** 2 - 10 * np.cos(2 * np.pi * y)
    )


def levi_13(x, y):
    return (
        np.sin(3 * np.pi * x) ** 2
        + ((x - 1) ** 2) * (1 + np.sin(3 * np.pi * y) ** 2)
        + ((y - 1) ** 2) * (1 + np.sin(2 * np.pi * y) ** 2)
    )
