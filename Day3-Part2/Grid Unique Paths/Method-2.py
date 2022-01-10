# Time = m * n
# Space = m * n

def check(m, n):
    dp = [[1]*n]*m
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]
m = 3
n = 6
print(check(m, n))

