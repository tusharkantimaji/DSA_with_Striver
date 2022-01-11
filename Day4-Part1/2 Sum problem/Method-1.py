# Time = n^2
# Space = 1

nums = [2, 7, 11, 15]
target = 9
l = len(nums)
for i in range(l):
    for j in range(i+1, l):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
    else:
        continue
    break
    


    