# Time = n log n + n
# Space = 1

nums = [102, 4, 100, 1, 101, 3, 2] # 1, 2, 3, 4, 100, 101, 102
nums.sort()
l = len(nums)
mc = 0
c = 1
p_e = nums[0]
for i in range(1, l):
    if nums[i] - 1 == p_e:
        c += 1
        p_e = nums[i]
    else:
        if mc < c:
            mc = c
        c = 0
        p_e = nums[i]
mc = max(mc, c)
print(mc)
        


        