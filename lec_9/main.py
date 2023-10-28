import random

#class Matrix
class Matrix:
    #ctor
    def __init__(self,rows,cols):
        self.__rows = rows
        self.__cols = cols
        self.__matrix = []
        for _ in range (rows):
            row = []
            row = [random.randint(1,20) for _ in range (cols)]
            self.__matrix.append(row)

    #magic methods
    #__str__
    def __str__(self):
        matrix_string = ""
        for row in self.__matrix:
            matrix_string += " ".join([f"{num:4}" for num in row]) + "\n"
        return matrix_string

    #__add__
    def __add__(self,rhs):
        if self.__rows != rhs.__rows or self.__cols != rhs.__cols:
            raise ValueError("Matrix dimensions must match for addition") 
        
        result = Matrix(self.__rows,self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] + rhs.__matrix[i][j]
        return result

    #__sub__
    def __sub__(self,rhs):
        if self.__rows != rhs.__rows or self.__cols != rhs.__cols:
            raise ValueError("Matrix dimensions must match for addition") 
        
        result = Matrix(self.__rows,self.__cols)
        for i in range(self.__rows):
            for j in range(self.__cols):
                result.__matrix[i][j] = self.__matrix[i][j] - rhs.__matrix[i][j]
        return result

    #__mul__
    def __mul__(self,rhs):
        if self.__cols != rhs.__rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        
        result = Matrix(self.__rows,rhs.__cols)
        for i in range(self.__rows):
            for j in range(rhs.__cols):
                for k in range(self.__cols):
                    result.__matrix[i][j] += self.__matrix[i][k] * rhs.__matrix[k][j]
            
        return result

    
#main logic

matrix_a = Matrix(5,7)
print("Matrix A: ")
print(str(matrix_a))

matrix_b = Matrix(5,7)
print("Matrix B: ")
print(str(matrix_b))

print("A + B: ")
print(str(matrix_a + matrix_b))

print("A - B: ")
print(str(matrix_a - matrix_b))

matrix_c = Matrix(7,3)
print("A * C: ")
print(str(matrix_a * matrix_c))
