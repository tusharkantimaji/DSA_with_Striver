# Time = n * n
# Space = 1

nums = [2,2,1,1,1,2,2]
l = len(nums)
for i in range(l):
    c = 1
    for j in range(i+1, l):
        if nums[i] == nums[j]:
            c += 1
    if c > l//2:
        print(nums[i])
        break


