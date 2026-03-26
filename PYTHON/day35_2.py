#wap that creates a 2d list having a number of rows and n number of rows and number of column. all the elements in the diagonal
#should be 0, the elemets above the diagonal should be 1 and the elements below the diagonal should be -1, values for m adn n should be taken from the user.
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
matrix = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if i == j:
            matrix[i][j] = 0
        elif j > i:
            matrix[i][j] = 1
        else:
            matrix[i][j] = -1
for row in matrix:
    print(row)