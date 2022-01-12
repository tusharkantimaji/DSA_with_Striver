# Time = n ^ 2
# Space = 1

nums = [15, -2, 2, -8, 1, 7, 10, 23]
d = {}
l = len(nums)
s = 0
ms = 0
for i in range(l):
    s += nums[i]
    if s == 0:
        ms = max(ms, i)
    elif s in d:
        ms = max(ms, i - d[s])
    else:
        d[s] = i
print(d)
print(ms)


