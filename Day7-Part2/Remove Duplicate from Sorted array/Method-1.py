# Time - n
# Space - n

nums = [0,0,1,1,1,2,2,3,3,4]
s = set(nums)
c = 0
for i in s:
    nums[c] = i
    c += 1
for i in range(c):
    print(nums[i], end=" ")


    