# Time = n
# Space = n

nums = [1, 2]
d = {}
ans = []
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    if d[i] > len(nums)//3:
        ans.append(i)
print(ans)

