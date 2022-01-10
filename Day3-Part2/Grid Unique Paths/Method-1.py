# Time = exponential
# Space = exponential

def check(i, j, m, n):
    if i == m-1 and j == n-1:
        return 1
    elif i > m-1 or j > n-1:
        return 0
    return check(i+1, j, m, n) + check(i, j+1, m, n)
m = 3
n = 6
print(check(0, 0, m, n))

