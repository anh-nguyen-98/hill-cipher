import math

def has_valid_length (n):
    if (n == 1):
        return True, 1

    for i in range(2, math.ceil(n/2 +1)):
        if i*i == n:
            return True, i

    return False, -1

print(has_valid_length(4))