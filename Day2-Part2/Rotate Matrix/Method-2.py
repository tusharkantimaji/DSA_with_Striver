# Time = n^2
# Space = 1

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = len(matrix)
c = len(matrix[0])
for i in range(r):
    for j in range(i):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# print(matrix)
for i in range(r):
    for j in range(c//2):
        matrix[i][j], matrix[i][c-j-1] = matrix[i][c-j-1], matrix[i][j]
print(matrix) 


