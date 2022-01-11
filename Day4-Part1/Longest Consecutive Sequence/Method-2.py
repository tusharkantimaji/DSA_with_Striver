# Time = n(make the set) + n(linear iteration) + n(checking the next one)
# Space = n

nums = [1, 2, 3, 4, 5, 6, 100, 101, 102] # 1, 2, 3, 4, 100, 101, 102
l = len(nums)
s = set(nums)
mc = 0
for i in range(l):
    if nums[i] - 1 not in s:
        n = nums[i] + 1
        c = 1
        while True:
            if n in s:
                c += 1
            else:
                break
            n += 1
        mc = max(mc, c)
print(mc)


