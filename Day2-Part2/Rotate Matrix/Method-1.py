# Time = n^2
# Space = n^2

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = len(matrix)
c = len(matrix[0])
temp_matrix = []
for i in range(r):
    temp_matrix.append([])
for i in matrix[::-1]:
    for j in range(len(i)):
        temp_matrix[j].append(i[j])
print(temp_matrix)
    


    