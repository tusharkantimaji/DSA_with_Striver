# Time = n * m
# Space = 1

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 100
for i in matrix:
    for j in i:
        if j == target:
            print(True)
            break
    else:
        continue
    break
else:
    print(False)


