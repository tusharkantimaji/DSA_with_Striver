# Time = 2 (n*m)
# Space = n + m

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
r = [] 
c = []
row = len(matrix)
column = len(matrix[0])
for i in range(row):
    for j in range(column):
        if matrix[i][j] == 0:
            r.append(i)
            c.append(j)
for i in range(row):
    for j in range(column):
        if i in r or j in c:
            matrix[i][j] = 0
print(matrix)



