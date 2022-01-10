# Time = m * n
# Space = m * n

# Total number of transition will be 
# (m-1) down and (n-1) right
# total = (m+n-2)
# So, the result will be (m+n-2)C(m-1) or (m+n-2)C(n-1)

def check(m, n):
    up = m+n-2
    down = m-1
    ans = 1
    for i in range(down, 0, -1):
        ans *= (up/i)
        up -= 1
    return int(ans)
    
m = 3
n = 6
print(check(m, n))

