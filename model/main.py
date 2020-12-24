import numpy as np
import scipy.linalg as lin
import math as math

import model.key_utils

import model.vec_transformation_utils
import model.vec_transformation_utils

from model.decipher import decipher
from model.encipher import encipher
from model import key_utils
from model.alphabet import Alphabet

ERROR_MSG = 'ERROR'

# alphabet = alphabet.Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# step 1:

#
# print("\nConsole Version")
# print ("\n***WELCOME TO BIJOU & CHRISTINE CRYPTOLAND***\n")
#
# #Client Input: message, password
# action = input("encode or decode? \n")
#
# type_password = input ("\nPassword type: num or alp? \n")
#
# password = input("\nPassword: \n")
#
# alphabet_type = input("\n Alphabet: \n")
# message = input("\nmessage:\n")


# print()

class Model():
    def evaluate_password (self, type_password, password, alphabet_type):
        try:
            alphabet = Alphabet(alphabet_type)
            valid, n = key_utils.has_valid_length(len(password))
            ret = []
            if not valid:
                ret.append(-1)
                return ret
            else:
                key = key_utils.to_matrix(password, n, type_password, alphabet)
                if not key_utils.is_invertible(key, alphabet):
                    ret.append(0)

                else:
                    ret.append(1)
                    ret.append(n)
                    ret.append(key)
                    ret.append(alphabet)
            return ret

        except ValueError:
            ret.append(0)
            return ret



    def encipher(self, key, n, alphabet, message):
        try:
            return model.encipher.encipher(message, key, n, alphabet)
        except Exception:
            return "Re-enter plaintext. It only includes characters on your alphabet."

    def decipher (self, key, n, alphabet, message):
        try:
            if len(message) % n != 0:
                return 'Make sure length of ciphertext be divisible by n'
            return model.decipher.decipher(message, key, n, alphabet)
        except Exception:
            return "Re-enter ciphertext. It only includes characters on your alphabet."


#
# #
# test = Model()
# #
# print(test.evaluate_password(0, 'B5HC', "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
