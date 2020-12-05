import numpy as np

ALPHABET_ID = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
                "W": 23, "X": 24, "Y": 25, "Z": 0}

CIPHER_ID = "ZABCDEFGHIJKLMNOPQRSTUVWXY"

def str_to_vec(text, set_size, let_map_num):
    ret = np.array([], dtype='int64')
    for i in range(0, len(text), set_size):
        p = np.zeros((set_size,), dtype='int64')
        for j in range(i, i + set_size):
            if j < len(text):
                p[j % set_size] = (let_map_num.get(text[j]))
        ret = np.append(ret, p, axis=0)

    dummy_count = set_size - (len(text) % set_size)

    if  dummy_count  < set_size:
        dummy_id = let_map_num.get(text[len(text) -1])
        for i in range(dummy_count):
            ret[ret.shape[0] -1 - i] = dummy_id

    return ret.reshape(-1, set_size).transpose()


def vec_to_str(matrix, num_map_let):
    text = ""
    for col in range(matrix.shape[1]):
        for row in range(matrix.shape[0]):
            text += num_map_let[int(matrix[row][col])]

    return text



def vec_to_vec(from_matrix, key, alpha_size):
    to_matrix = np.dot(key, from_matrix)

    for row in range(to_matrix.shape[0]):
        for col in range(to_matrix.shape[1]):
            if to_matrix[row][col] >= alpha_size:
                to_matrix[row][col] %= alpha_size

    return to_matrix

