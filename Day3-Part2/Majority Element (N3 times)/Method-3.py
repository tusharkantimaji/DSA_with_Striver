# Soyer Voting Algorithm
# Time = n
# Space = 1

nums = [3, 3, 3, 1, 1, 2, 2, 2]
num1 = -1
num2 = -1
c1 = 0
c2 = 0
ans = []
for i in nums:
    if num1 == i:
        c1 += 1
    elif num2 == i:
        c2 += 1
    elif c1 == 0:
        num1 = i
        c1 += 1
    elif c2 == 0:
        num2 = i
        c2 += 1
    else:
        c1 -= 1
        c2 -= 1
c1, c2 = 0, 0
for i in nums:
    if i == num1:
        c1 += 1
    elif i == num2:
        c2 += 1
if c1 > len(nums)//3:
    ans.append(num1)
if c2 > len(nums)//3:
    ans.append(num2)
print(ans)

