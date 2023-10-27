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
            row = [random.randint(1,100) for _ in range (rows)]
            self.__matrix.append(row)
        
    def calculate_mean_of_matrix(self):
        sum_of_all = 0
        quantity = self.__rows * self.__cols
        for row in range(self.__rows):
            sum_of_all = sum_of_all + sum(self.__matrix[row])
        
        return sum_of_all / quantity
    
    def print_matrix(self):
        for row in range(self.__rows):
            print(self.__matrix[row])
    
    def calculate_sum_of_row(self,index_of_row):
        if (index_of_row >= 0) and (index_of_row < self.__rows):
            return sum(self.__matrix[index_of_row])
        else:
            return None

    def calculate_average_of_column(self,index_of_col):
        if (index_of_col >= 0) and (index_of_col < self.__cols):
            sum_of_col = 0
            for row in self.__matrix:
                sum_of_col += row[index_of_col]

            return sum_of_col / self.__rows
        else:
            return None

    def print_submatrix(self,col1,col2,row1,row2):
         if (0 <= col1 < col2 < self.__cols) and (0 <= row1 < row2 < self.__rows):
            for i in range(row1,row2 + 1):
                row = self.__matrix[i][col1 : col2 + 1]
                print(row)
#main logic

myMat = Matrix(5,5)
myMat.print_matrix()
mean = myMat.calculate_mean_of_matrix()
print("Mean of matrix myMat: " + str(mean))

sum_of_row = myMat.calculate_sum_of_row(3)
print("Sum of elements of the row with index 3: " + str(sum_of_row))

average_of_column = myMat.calculate_average_of_column(3)
print("Average of elements of the row with index 3: " + str(average_of_column)) 

print("Submatrix of myMat (col1 = 0, col2 = 2, row1 = 1, row2 = 4)")
myMat.print_submatrix(0,2,1,4)
