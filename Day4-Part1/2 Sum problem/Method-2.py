# Time = n
# Space = n

nums = [2, 7, 11, 15]
target = 9
l = len(nums)
d = {}
for i in range(l):
    if target - nums[i] not in d:
        d[nums[i]] = i
    else:
        print([i, d[target - nums[i]]])
        break


    