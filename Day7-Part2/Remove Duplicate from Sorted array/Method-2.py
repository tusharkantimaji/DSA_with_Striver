# Time - n
# Space - 1

nums = [0,0,1,1,1,2,2,3,3,4]
i = 0
j = 1
while j < len(nums):
    if nums[j] != nums[i]:
        i += 1
        nums[i] = nums[j]
    j += 1
for j in range(i+1):
    print(nums[j], end=" ")



    