#!/usr/bin/python3

"""Function for matrix multiplication using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function returns multiplication of two matrices.

    Args:
        m_a (list of lists of ints/floats): For first matrix.
        m_b (list of lists of ints/floats): For second matrix.
    """

    return (np.matmul(m_a, m_b))
