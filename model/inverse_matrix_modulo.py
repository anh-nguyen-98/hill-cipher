import numpy as np
import math

from model.multiplicative_inverse_modulo import find_inverse


def inv (key_matrix, m):
    #find_cofactor
    cofactor = find_cofactor(key_matrix)


    #find adjugate
    adjugate = find_adjugate(cofactor)

    #find inverse of det(key_matrix)
    multiplicative_inverse = find_inverse(round(np.linalg.det(key_matrix)), m)

    inverse_matrix = multiplicative_inverse*adjugate

    for row in range(inverse_matrix.shape[0]):
        for col in range(inverse_matrix.shape[1]):
            if inverse_matrix[row][col] > (m-1) or inverse_matrix[row][col] <0:
                inverse_matrix[row][col] %= m

    return inverse_matrix

def find_cofactor(key_matrix):
    co_factor = key_matrix.copy()

    # for i in range(key_matrix.shape[0]) :
    #     co_factor[i] = key_matrix[i].copy()

    for row in range(key_matrix.shape[0]):
        for col in range(key_matrix.shape[1]):
            minor_matrix = find_minor(key_matrix, row, col)
            co_factor[row][col] = round(np.linalg.det(minor_matrix))

    return co_factor


def find_minor(key_matrix, row, col):
    row_ids = list(range(0, key_matrix.shape[0]))
    col_ids = list(range(0, key_matrix.shape[0]))
    del row_ids[row]
    del col_ids[col]

    return key_matrix[np.ix_(row_ids, col_ids)]

def find_adjugate(co_factor):
    #apply checkerboard
    adjugate = np.zeros(co_factor.shape)

    for row in range(co_factor.shape[0]):
        if row % 2 == 0:
            for col in range(co_factor.shape[1]):
                adjugate[row][col] = pow(-1, col%2)*co_factor[row][col]

        else:
            for col in range(co_factor.shape[1]):
                adjugate[row][col] = pow(-1, col%2 -1)*co_factor[row][col]


    #transpose
    return adjugate.transpose()