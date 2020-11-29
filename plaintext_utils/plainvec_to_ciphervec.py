import numpy as np


def (plain_matrix, key, alpha_size):
    cipher_matrix = key @ plain_matrix

    for row in cipher_matrix.shape[0]:
        for col in cipher_matrix.shape[1]:
            if cipher_matrix[row][col] >= alpha_size:
                cipher_matrix[row][col] %= alpha_size

    return cipher_matrix