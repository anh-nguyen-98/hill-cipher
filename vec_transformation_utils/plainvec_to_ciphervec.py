import numpy as np


def transform(plain_matrix, key, alpha_size):
    cipher_matrix = np.dot(key, plain_matrix)

    for row in range(cipher_matrix.shape[0]):
        for col in range(cipher_matrix.shape[1]):
            if cipher_matrix[row][col] >= alpha_size:
                cipher_matrix[row][col] %= alpha_size

    return cipher_matrix


