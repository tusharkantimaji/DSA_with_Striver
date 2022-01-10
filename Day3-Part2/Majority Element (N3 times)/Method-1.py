# Time = n * n
# Space = 1

nums = [1, 2]
l = len(nums)
ans = []
for i in range(l):
    c = 1
    for j in range(i+1, l):
        if nums[i] == nums[j]:
            c += 1
    if c > l//3:
        ans.append(nums[i])
print(ans)


