# Time = n^3 * m(element in the ans)
# Space = 1 ==> no extra space in needed without the answer

nums = [-1,0,1,2,-1,-4]
nums.sort()
ans = []
l = len(nums)
for i in range(l):
    for j in range(i+1, l):
        for k in range(j+1, l):
            if nums[i] + nums[j] + nums[k] == 0:
                p = [nums[i], nums[j], nums[k]]
                if p not in ans:
                    ans.append(p)
print(ans)


