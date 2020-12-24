import numpy as np
import math

from model.alphabet import Alphabet


def divisor_list (m):
    divisor_ls = []
    for i in range(2, m):
        if m % i == 0:
            divisor_ls.append(i)

    return divisor_ls

# alphabet = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# matrix = np.array([[5, 6], [2, 3]])

def is_invertible(matrix, alphabet):

    det = round(np.linalg.det(matrix))
    if det == 0: return False
    divisor_ls = divisor_list(alphabet.alpha_size)
    for d in divisor_ls:
        if det % d == 0: return False

    return True
#
# print(is_invertible(matrix, alphabet))
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
    if type_password == 0:
        matrix = np.array([int(digit) for digit in password]).reshape((n, n))

    # for letter password:
    else:
        matrix = np.array([alphabet.let_map_num.get(letter) for letter in password]).reshape((n, n))

    return matrix
