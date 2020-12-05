import numpy as np
import math

def is_invertible(matrix, alphabet):

    det = np.linalg.det(matrix)

    return not (det == 0 or (det % alphabet.alpha_size) % 2 == 0 or (det % alphabet.alpha_size) % 13 == 0)

def has_valid_length (n):
    if (n == 1):
        return True, 1

    for i in range(2, math.ceil(n/2 +1)):
        if i*i == n:
            return True, i

    return False, -1




# check invertible matrix mod 26

# tao matrix tu password:
# for numerical password
def to_matrix(password, n, type_password, alphabet):
    if type_password == "num":
        matrix = np.array([int(digit) for digit in password]).reshape((n, n))

    # for letter password:
    else:
        matrix = np.array([alphabet.let_map_num.get(letter) for letter in password]).reshape((n, n))

    return matrix
