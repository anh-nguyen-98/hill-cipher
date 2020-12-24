def find_inverse(n, m):
    for i in range(0, m):
        if n*i % m == 1:
            return i

    return -1


# print(find_inverse(-11, 26))