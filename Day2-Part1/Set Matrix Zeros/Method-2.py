# Time = n*m
# Space = 1

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

row = len(matrix)
column = len(matrix[0])
col_1 = False
for i in range(row):
    if matrix[i][0] == 0:
        col_1 = True
    for j in range(1, column):
        if matrix[i][j] == 0:
            matrix[0][j] = 0
            matrix[i][0] = 0
for i in range(1, row):
    for j in range(1, column):
        if matrix[i][0] == 0 or matrix[0][j] == 0:
            matrix[i][j] = 0
if matrix[0][0] == 0:
    for j in range(column):
        matrix[0][j] = 0
if col_1 == True:
    for i in range(row):
        matrix[i][0] = 0
print(matrix)
            



            