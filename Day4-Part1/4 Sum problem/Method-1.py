# Time = n^3 log n + log n
# Space = 1

def binary_search(nums, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    return -1

nums = [1, 0, -1, 0, -2, 2]
target = 0
nums.sort()
l = len(nums)
result = []
for i in range(0, l-1):
    for j in range(i+1, l-1):
        for k in range(j+1, l-1):
            remain = target - nums[i] - nums[j] - nums[k]
            index = binary_search(nums, remain, k+1, l-1)
            if index > 0:
                result.append([nums[i], nums[j], nums[k], nums[index]])
print(result)


