Time = n + m
Space = 1

def check(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    i = 0
    j = col - 1
    while i < row and j >= 0:
        if matrix[i][j] == target:
            return [i+1, j+1]
        elif target < matrix[i][j]:
            j -= 1
        else:
            i += 1
    return ('Not Found')

matrix = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
target = 24
print(check(matrix, target))


