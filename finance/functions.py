import numpy as np


def last_maximum_occurrence_index(x):
    b = x[::-1]
    return len(b) - np.argmax(b) - 1
