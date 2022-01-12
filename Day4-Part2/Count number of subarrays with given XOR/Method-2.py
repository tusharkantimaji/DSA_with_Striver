# Time = n
# Space = n

nums = [5, 6, 7, 8, 9]
k = 5
d = {}
l = len(nums)
xor = 0
count = 0
for i in range(l):
    xor ^= nums[i]
    if xor == k:
        count += 1
    y = xor ^ k
    if y not in d:
        d[y] = 1
    else:
        d[y] += 1
    if xor in d:
        count += d[xor]
print(count)



