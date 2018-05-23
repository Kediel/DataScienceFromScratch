# Linear Algebra
# -*- coding: iso-8859-15 -*-

import re, math, random # regexes, math functions, random numbers
import matplotlib.pyplot as plt # pyplot
from collections import defaultdict, Counter
from functools import partial, reduce


###################### Vectors ###########################

def vector_add(v, w):

    # Adds corresponding elements
    return [v_i + w_i for  v_i, w_i in zip(v,w)]

def vector_subtract(v, w):

    # Subtracts corresponding elements
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def vector_sum(vectors):

    # Sums all corresponding elements
    # or vector_sum = partial(reduce, vector_add)
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):

    # C is a number, v is a vector

    return [c * v_i for v_i in v]

def vector_mean(vectors):

    # Compute the vector whose nth element is the mean of the nth elements of the input vectors
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

def dot(v, w):

    # v_1 * w_1 + ... + v_n * w_n
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):

    # v_i * v_i + ... + v_n * v_n
    return dot(v, v)

def magnitude(v):

    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):

    # (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):

    return math.sqrt(squared_distance(v, w))
    # or return magnitude(vector_subtract(v, w))

###################### Matrices ###########################

if __name__ == "__main__":



