# Time = n
# Space = 1

def check(x, n):
    ans = 1
    if n == 0:
        return round(1, 5)
    elif n > 0:
        for i in range(n):
            ans *= x
        return round(ans, 5)
    else:
        for i in range(-n):
            ans *= x
        return round(1/ans, 5)

x = 2.00000
n = 10
print(check(x, n))

