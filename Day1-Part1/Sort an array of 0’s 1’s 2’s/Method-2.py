# Time = n
# Space = 1

nums = [2,0,2,1,1,0]
c_0 = c_1 = c_2 = 0
for i in nums:
    if i == 0:
        c_0 += 1
    elif i == 1:
        c_1 += 1
    else:
        c_2 += 1
for i in range(c_0):
    nums[i] = 0
for i in range(c_1):
    nums[c_0 + i] = 1
for i in range(c_2):
    nums[c_0 + c_1 +i] = 2
print(nums)