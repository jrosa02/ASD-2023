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
    T_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    for col_i in range(cols):
        for row_i in range(rows):
            T_matrix[col_i][row_i] += matrix[row_i][col_i]
    return macierz(T_matrix)

m1 = macierz(
[ [1, 0, 2],
  [-1, 3, 1] ]
)

m2 = macierz(
[ [3, 1],
  [2, 1],
  [1, 0]]
)

m3 = macierz((2, 3), 1)

#print(T(m1))
#print(m1 + m3)
#print(m1 *m2)



def determinant(matrix: macierz, b: float  = 1, depth = 1):
    rows, cols = matrix.size()
    print(b)
    print(matrix)
    if rows != cols:
        raise BaseException()
    if rows < 2:
        return matrix[0][0] / b
    else:
        new_matrix = [[0 for _ in range(rows-1)] for _ in range(cols-1)]
        for i in range(rows-1):
            for j in range(cols - 1):
                new_matrix[i][j] = matrix[0][0]*matrix[i+1][j+1] - matrix[i+1][0]*matrix[0][j+1]
        b *= matrix[0][0]**(rows-2)
        new_matrix = macierz(new_matrix)
    return determinant(new_matrix, b, depth=depth+1)


m4 = macierz([
[5 , 1 , 1 , 2 , 3],
[4 , 2 , 1 , 7 , 3],
[2 , 1 , 2 , 4 , 7],
[9 , 1 , 0 , 7 , 0],
[1 , 4 , 7 , 2 , 2]
])

m5 = macierz(  [
     [0 , 1 , 1 , 2 , 3],
     [4 , 2 , 1 , 7 , 3],
     [2 , 1 , 2 , 4 , 7],
     [9 , 1 , 0 , 7 , 0],
     [1 , 4 , 7 , 2 , 2]
    ])

print(determinant(m4))
print(determinant(m5))

