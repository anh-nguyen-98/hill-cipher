import numpy as np


def is_invertible(matrix):
    ALPHA_SIZE = 26

    det = np.linalg.det(matrix)

    return not (det == 0 or (det % ALPHA_SIZE) % 2 == 0 or (det % ALPHA_SIZE) % 13 == 0)


#print(is_invertible([[1, 2], [0, 3]]))
