# Time = n
# Space = n

nums = [2,2,1,1,1,2,2]
d = {}
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
for i in d:
    if d[i] > len(nums)//2:
        print(i)
        break

