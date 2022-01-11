# Time = n^3
# Space = 

nums = [1, 0, -1, 0, -2, 2]
target = 0
nums.sort()
l = len(nums)
result = []
for i in range(0, l-1):
    for j in range(i+1, l-1):
        rem = target - nums[i] - nums[j]
        left = j + 1
        right = l - 1
        while left < right:
            if nums[left] + nums[right] == rem:
                result.append([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < rem:
                left += 1
            else:
                right -= 1
print(result)


