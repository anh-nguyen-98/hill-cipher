import numpy as np

def transform(matrix, num_map_let):
    text = ""
    for col in range(matrix.shape[1]):
        for row in range(matrix.shape[0]):
            text += num_map_let[matrix[row][col]]

    return text