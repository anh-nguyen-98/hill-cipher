"""
Enciphers a plaintext.

@author: Nguyen Bao Ngoc
@author: Nguyen Hoang Nam Anh 
"""

import numpy as np
import scipy.linalg as lin
import math as math


ALPHABET_ID = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
                "W": 23, "X": 24, "Y": 25, "Z": 0}
#step 1:

#Client Input: message, password

plaintext = input ("Plaintext: ")

#typePassword = input ("all-number or all-letter?")

password = input("Password: ")

#checkPerfectSquare



#check valid key
if (!isPerfectSquare(len(password))):
    print ("Error: length of password must be a perfect square 4, 16, 25, ... ")

else:
     n = int(math.sqrt(len(password)))
     
    #check invertible matrix mod 26
    
    #tao matrix tu password:
     #for numerical password
    if (typePassword == "all-number"):
        matrix = np.array([int(digit) for digit in password]).reshape((n, n))
    
    #for letter password:
    else:
        ALPHABET_ID = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                       "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
                       "W": 23, "X": 24, "Y": 25, "Z": 0}
        
        matrix = np.array(ALPHABET_ID.get(letter) for letter in password]).reshape((n, n))
        
    #check whether det(A) != 0 & (det(A)%26) ko chia het cho 2 va 13
        det = np.linalg.det(matrix)
        
        if (det == 0
            or (det % 26) % 2 == 0
            or  (det % 26) % 13 == 0):
                print ("Error: Please change the last 2 letters")
    else:
        print ("Your message is being encoded")
    
    
#step 2: process plaintext to numerical vector

list_p = []
for i in range(0, len(plaintext), n):
    p = []
    for j in range(i, i+n):
        if (j < len(plaintext)):  
            p.append(ALPHABET_ID.get(plaintext[j]))
            
    list_p.append(p)


if len(list_p[-1]) < n:
    last_letter  = list_p[-1][-1]
    for i in range(n-len(list_p[-1])):
        list_p[-1].append(last_letter)
    
    


#step 3: from plaintext vector to ciphertext vector



