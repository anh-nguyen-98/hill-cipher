import numpy as np

ALPHABET_ID = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
               "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
               "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
               "S": 19, "T": 20, "U": 21, "V": 22,
               "W": 23, "X": 24, "Y": 25, "Z": 0}


# check invertible matrix mod 26

# tao matrix tu password:
# for numerical password
def to_matrix(password, n, type_password):
    if type_password == "numerical":
        matrix = np.array([int(digit) for digit in password]).reshape((n, n))

    # for letter password:
    else:
        matrix = np.array([ALPHABET_ID.get(letter) for letter in password]).reshape((n, n))

    return matrix


print(to_matrix("ABCD", 2, "al"))
