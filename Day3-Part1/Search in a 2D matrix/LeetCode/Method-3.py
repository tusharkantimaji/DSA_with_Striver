# Time = log (n*m)
# Space = 1

def check(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    left = 0
    right = row*col - 1
    while left <= right:
        mid = (right + left) //2
        print(left, mid, right)
        if matrix[mid//col][mid%col] == target:
            return True
        elif target < matrix[mid//col][mid%col]:
            right = mid - 1
        else:
            left = mid + 1
    return False

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 31
print(check(matrix, target))

