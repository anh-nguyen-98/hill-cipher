import numpy as np
import scipy.linalg as lin
import math as math

import decipher
import encipher
import key_utils.length
import key_utils.to_matrix
import key_utils.invertible_matrix
import vec_transformation_utils.str_to_vec
import vec_transformation_utils.vec_to_vec

ALPHABET_ID = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
                "W": 23, "X": 24, "Y": 25, "Z": 0}

CIPHER_ID = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

alpha_size = 26
#step 1:

#Client Input: message, password

message = input ("Coded message: ")

type_password = input ("numerical or alphabet?")

password = input("Password: ")

action = input("encode or decode? ")

#check valid key
valid, n = key_utils.length.has_valid_length(len(password))
if not valid:
    print ("Error: length is not a perfect square 4, 9, 16, ... ")

else:
    key = key_utils.to_matrix.to_matrix(password, n, type_password)
    if key_utils.invertible_matrix.is_invertible(key):
        if action == 'encode':
            print("Your message is being encoded")
            print(encipher.encipher(message, key, n))

        else:
            if len(message) % n != 0:
                print('Error: length of message must be multiple of n')

            else:
                print("Your message is being encoded")
                print(decipher.decipher(message, key, n))

    else:
        print('Please change last 2 characters')




