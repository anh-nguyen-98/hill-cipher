import numpy as np
import scipy.linalg as lin
import math as math

import decipher
import encipher
import key_utils

import vec_transformation_utils
import vec_transformation_utils
from alphabet_utils.alphabet import Alphabet


alphabet = Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#step 1:
print("\nConsole Version")
print ("\n***WELCOME TO BIJOU & CHRISTINE CRYPTOLAND***\n")

#Client Input: message, password
action = input("encode or decode? \n")

message = input ("\nmessage:\n")

type_password = input ("\nPassword type: num or alp? \n")

password = input("\nPassword: \n")

print()



#check valid key
valid, n = key_utils.has_valid_length(len(password))
if not valid:
    print ("Error: length is not a perfect square 4, 9, 16, ... ")

else:
    key = key_utils.to_matrix(password, n, type_password,alphabet)
    if key_utils.is_invertible(key, alphabet):
        if action == 'encode':
            print("Your message is being encoded")
            print(encipher.encipher(message, key, n, alphabet))

        else:
            if len(message) % n != 0:
                print('Error: length of message must be multiple of n')

            else:
                print("Your message is being decoded")
                print(decipher.decipher(message, key, n, alphabet))

    else:
        print('Please change last 2 characters')




