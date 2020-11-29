"""
Enciphers a plaintext.

@author: Nguyen Bao Ngoc
@author: Nguyen Hoang Nam Anh 
"""

import numpy as np
import scipy.linalg as lin
import math as math
import password_utils.length
import password_utils.to_matrix
import password_utils.invertible_matrix
import plaintext_utils.plaintext_to_vector
import plaintext_utils.plainvec_to_ciphervec



ALPHABET_ID = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
                "W": 23, "X": 24, "Y": 25, "Z": 0}

CIPHER_ID = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

alpha_size = 26
#step 1:

#Client Input: message, password

message = input ("Message: ")

type_password = input ("numerical or alphabet?")

password = input("Password: ")


#check valid key
valid, n = password_utils.length.has_valid_length(len(password))
if not valid:
    print ("Error: length is not a perfect square 4, 9, 16, ... ")

else:
    key = password_utils.to_matrix.to_matrix(password, n, type_password)
    if password_utils.invertible_matrix.is_invertible(key):
        print("Your message is being encoded")
    else:
        print('Please change last 2 characters')

    
#step 2: process plaintext to numerical vector
P = plaintext_utils.plaintext_to_vector.transform(message, n)
    
    
#step 3: from plaintext vector to ciphertext vector

C = plaintext_utils.plainvec_to_ciphervec.transform(P, key, alpha_size)

ciphertext = ""
for col in range(C.shape[1]):
    for row in range(C.shape[0]):
        ciphertext += CIPHER_ID[C[row][col]]



print (ciphertext)






