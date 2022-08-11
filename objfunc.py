import numpy as np


def rastrigin(x, out=None):
    if len(x.shape) == 2:
        axis = 1
    else:
        axis = 0
    x = np.asarray_chkfinite(x)
    if out is None:
        y = np.zeros((x.shape[0]), dtype=x.dtype)
    else:
        y = out
    n = np.size(x, axis)
    y[:] = 10 * n + np.sum(x ** 2 - 10 * np.cos(2 * np.pi * x), axis)
    return y


def rosenbrock(x, out=None):
    if len(x.shape) == 2:
        axis = 1
    else:
        axis = 0
    x = np.asarray_chkfinite(x)
    if out is None:
        y = np.zeros((x.shape[0]), dtype=x.dtype)
    else:
        y = out
    n = np.size(x, axis)
    x0 = x[:, 0:n-1]
    x1 = x[:, 1:n]
    y[:] = np.sum((1 - x0) ** 2 + 100 * (x1 - x0 ** 2) ** 2, axis)
    return y


def schwefel(x, out=None):
    if len(x.shape) == 2:
        axis = 1
    else:
        axis = 0
    x = np.asarray_chkfinite(x)
    if out is None:
        y = np.zeros((x.shape[0]), dtype=x.dtype)
    else:
        y = out
    n = np.size(x, axis)
    y[:] = 418.9829 * n - np.sum(x * np.sin(np.sqrt(abs(x))), axis)
    return y
