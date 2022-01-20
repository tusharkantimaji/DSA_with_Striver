# Time = n*2
# space = 1


nums = [-1,0,1,2,-1,-4]
ans = []
nums.sort()
l = len(nums)
i = 0
while i < l:
    target = -nums[i]
    low = i+1
    high = l-1
    while low < high:
        if nums[low] + nums[high] == target:
            ans.append([nums[i], nums[low], nums[high]])
            j = nums[low]
            low += 1
            while nums[low] == j and low < high:
                low += 1
            k = nums[high]
            high -= 1
            while nums[high] == k and high > low:
                high -= 1
        elif nums[low] + nums[high] < target:
            j = nums[low]
            low += 1
            while nums[low] == j and low < high:
                low += 1
        else:
            k = nums[high]
            high -= 1
            while nums[high] == k and high > low:
                high -= 1
    p = nums[i]
    i += 1
    while  i < l-1 and nums[i] == p:
        i += 1
print(ans)


