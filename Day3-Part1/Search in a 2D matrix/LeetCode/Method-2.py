# Time = n + m
# Space = 1

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 60

for i in matrix:
    if i[-1] >= target:
        for j in i:
            if j == target:
                print(True)
                break
        else:
            print(j)
            print(False)
            break


        