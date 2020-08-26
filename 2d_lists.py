#2 dimensional lists
#We can model a matrix in python using 2 dimensional lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix[0][1] = 20
print(matrix[0][1]) #Brings out the first list with the second item

# You can also use nested loops to iterate over all the items in the matrix
for row in matrix:
    for item in row:
        print(item)