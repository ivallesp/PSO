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
        np.log(
            1
            + (1.5 - x + x * y) ** 2
            + (2.25 - x + x * y ** 2) ** 2
            + (2.625 - x + x * y ** 3) ** 2
        )
        / 10
    )
