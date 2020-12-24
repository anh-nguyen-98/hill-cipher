"""
Decodes a ciphertext.

@author: Nguyen Bao Ngoc
@author: Nguyen Hoang Nam Anh

"""

import numpy as np
import scipy.linalg as lin
import math as math

from model import vec_transformation_utils
from model.inverse_matrix_modulo import inv


def decipher(message, key, n, alphabet):
    #ciphermatrix
    # step 2: process ciphertext to numerical vector
    C = vec_transformation_utils.str_to_vec(message, n, alphabet.let_map_num)

    # step 3: from cipher vector to plaintext vector

        #finds inverse key mod n (deciphering matrix)
    key_inverse = inv(key, alphabet.alpha_size)

        # deciphering_matrix @ cipher_matrix
    P = vec_transformation_utils.vec_to_vec(C, key_inverse, alphabet.alpha_size)

    # step 4: publish plaintext
    plaintext = vec_transformation_utils.vec_to_str(P, alphabet.num_map_let)

    return plaintext

