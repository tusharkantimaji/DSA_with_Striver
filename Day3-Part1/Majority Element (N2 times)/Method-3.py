# Moor Voting Algorithm
# Time = n
# Space = 1

nums = [7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]
count = 0
elm = 0
for i in nums:
    if count == 0:
        elm = i
    if i == elm:
        count += 1
    else:
        count -= 1
print(elm)

