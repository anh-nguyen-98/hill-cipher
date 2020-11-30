"""
Enciphers a plaintext.

@author: Nguyen Bao Ngoc
@author: Nguyen Hoang Nam Anh 
"""

import numpy as np
import scipy.linalg as lin
import math as math
import key_utils.length
import key_utils.to_matrix
import key_utils.invertible_matrix
import vec_transformation_utils.str_to_vec
import vec_transformation_utils.vec_to_vec
import vec_transformation_utils.vec_to_str

LET_MAP_NUM = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
               "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
               "W": 23, "X": 24, "Y": 25, "Z": 0}

NUM_MAP_LET = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

alpha_size = 26


def encipher(message, key, n):
    # step 2: process plaintext to numerical vector
    P = vec_transformation_utils.str_to_vec.transform(message, n, LET_MAP_NUM)

    # step 3: from plaintext vector to ciphertext vector
    C = vec_transformation_utils.vec_to_vec.transform(P, key, alpha_size)

    # step 4: publish ciphertext
    ciphertext = vec_transformation_utils.vec_to_str.transform(C, NUM_MAP_LET)

    return ciphertext
