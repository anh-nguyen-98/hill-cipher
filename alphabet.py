class Alphabet():
    def __init__(self, alphabet):
        self.num_map_let = alphabet
        self.alpha_size = len(alphabet)
        self.let_map_num = self.__construct_map__()


    def __construct_map__(self):
        let_map_num = {}
        for i in range(0, self.alpha_size):
            let_map_num[self.num_map_let[i]] = i

        return let_map_num


