import numpy as np


def last_minimum_occurrence_index(x):
    b = x[::-1]
    return len(b) - np.argmin(b) - 1


def last_maximum_occurrence_index(x):
    b = x[::-1]
    return len(b) - np.argmax(b) - 1


def rescale_by_part(x, first, minimum, maximum):
    if x >= first:
        assert x <= maximum,  "input is above maximal contraint"
        return np.float(x-first) / (maximum-first)
    else:
        assert x >= minimum, "input is bellow minimum contraint"
        return np.float(x - first) / (first - minimum)


def rescale(x):
    a = np.vectorize(rescale_by_part)
    return a(x=x, first=x[0], minimum=min(x), maximum=max(x))
