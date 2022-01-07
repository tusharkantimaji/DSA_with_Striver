# Time = n!
# Space = n!

#     [1]
#    [1, 1]
#   [1, 2, 1]
#  [1, 3, 3, 1]
# [1, 4, 6, 4, 1]

n = 10
ans = []
for i in range(n):
    row =[1]
    if i > 1:
        for j in range(i-1):
            row.append(ans[i-1][j] + ans[i-1][j+1])
#         row.append(1)
    if i > 0:
        row.append(1)
    ans.append(row)
for i in range(len(ans)):
    print(' ' * (n-i-1), end="")
    print(ans[i])


    