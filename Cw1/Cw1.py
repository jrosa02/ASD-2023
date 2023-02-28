from typing import List, Tuple

class macierz:
    def __init__(self, matrix, val = 0):
        if(isinstance(matrix, List)):
            self.__matrix_ = matrix
        if(isinstance(matrix, Tuple)):
            self.__matrix_ = [[val] * matrix[1]] * matrix[0]

    def __getitem__(self, cord):
        return self.__matrix_[cord]

    def __add__(self, other):
        matrix = []
        for rownr in range(len(self.__matrix_)):
            row_ = []
            for col in range(len(self.__matrix_[0])):
                row_.append(self[rownr][col] + other[rownr][col])
            matrix.append(row_)
        return macierz(matrix)

    def __mul__(self, other):
        new_matrix = []
        for new_row_nr_i in range(self.size()[0]):
            new_row = []
            for new_col_nr_i in range(self.size()[0]):
                new_val = 0
                for i in range(self.size()[1]):
                    new_val += self[new_col_nr_i][i] * other[i][new_row_nr_i]
                new_row.append(new_val)
            new_matrix.append(new_row)
        return macierz(new_matrix)
        
    def __str__(self):
        row_q, col_q = self.size()
        strink = ""
        for row_nr in range(row_q):
            strink += "| "
            for col_nr in range(col_q):
                strink += str(self[row_nr][col_nr]) + " "
            strink += "|\n"
        return strink

    def size(self):
        return (len(self.__matrix_), len(self.__matrix_[0]))
    

def T(matrix: macierz):
    rows, cols = matrix.size()
    new_matrix = macierz((cols, rows))
    for i in range(cols):
        for j in range(rows):
            new_matrix[i][j] += matrix[j][i]
    return new_matrix

m1 = macierz(
[ [1, 0, 2],
  [-1, 3, 1] ]
)

m2 = macierz(
[ [3, 1],
  [2, 1],
  [1, 0]]
)

m3 = macierz((2, 3))

if __name__ == "__main__":
    print(m1.size())
    print(m1[0][0])
    print(m1 + m1)
    print(m1 * m2)
    print(T(m2))
