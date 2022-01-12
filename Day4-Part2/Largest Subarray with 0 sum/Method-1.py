# Time = n ^ 2
# Space = 1

nums = [15, -2, 2, -8, 1, 7, 10, 23]
mc = 0
l = len(nums)
for i in range(l):
    s = 0
    for j in range(i, l):
        s += nums[j]
        if s == 0:
            mc = max(mc, j-i+1)
print(mc)

