import random

def generate_random_matrix(rows,cols):
    matrix = []
    for row in range(rows):
        row = [random.randint(1,100) for _ in range(cols)]
        matrix.append(row)

    return matrix

def get_column_sum(matrix,index_of_col):
    column_sum = 0
    for el in range(len(matrix)):
        column_sum += matrix[el][index_of_col]
    return column_sum

def get_row_average(matrix,index_of_row):
    rowsum = sum(matrix[index_of_row])
    n = len(matrix[index_of_row])
    return rowsum / n
    

matrix_2d = generate_random_matrix(4,4)
print("The 2D matrix:")
for i in range (len(matrix_2d)):
    print(matrix_2d[i])

print("The sum of the elements of the 3th column:",end = " ")
sum3 = get_column_sum(matrix_2d,3)
print(sum3)

print("The average of the elements of teh 2nd row:",end = " ")
avg2 = get_row_average(matrix_2d,2)
print(avg2)