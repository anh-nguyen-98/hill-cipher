"""
Enciphers a plaintext.

@author: Nguyen Bao Ngoc
@author: Nguyen Hoang Nam Anh 
"""

import numpy as np
import scipy.linalg as lin
import math as math
import key_utils
import vec_transformation_utils



def encipher(message, key, n, alphabet):
    # step 2: process plaintext to numerical vector
    P = vec_transformation_utils.str_to_vec(message, n, alphabet.let_map_num)

    # step 3: from plaintext vector to ciphertext vector
    C = vec_transformation_utils.vec_to_vec(P, key, alphabet.alpha_size)

    # step 4: publish ciphertext
    ciphertext = vec_transformation_utils.vec_to_str(C, alphabet.num_map_let)

    return ciphertext
