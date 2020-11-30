import numpy as np


def transform(text, set_size, let_map_num):
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


print(transform('ABCD', 2))
