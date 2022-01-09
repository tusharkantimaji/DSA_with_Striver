# Time = log n
# Space = 1

def check(x, n):
    ans = 1
    n_copy = n
    n = abs(n)
    if n == 0:
        return round(1, 5)
    while n > 0:
        if n % 2 == 0:
            x *= x
            n //= 2
        else:
            ans *= x
            n -= 1
    if n_copy > 0:
        return round(ans, 5)
    else:
        return round(1/ans, 5)

x = 2.00000
n = 0
print(check(x, n))

