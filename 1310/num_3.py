class Matrix:
    def __init__(self, matrix):
        q = len(matrix[0])
        n = 1
        for i in range(1, len(matrix)):
            if q == len(matrix[i]):
                n += 1
        if n == len(matrix):
            self.matrix = matrix
        else:
            print('Error')
    def transpone(self):
        tr_matrix = [[] for _ in self.matrix[0]]
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                tr_matrix[i].append(self.matrix[j][i])
        self.matrix = tr_matrix
        return tr_matrix

    def transponeV2(self):
        tr_matrix = [list(values) for values in zip(*self.matrix)]
        self.matrix = tr_matrix
        return tr_matrix

m1 = Matrix([[1,2],[6,7],[4,2]])
print(m1.transpone2())