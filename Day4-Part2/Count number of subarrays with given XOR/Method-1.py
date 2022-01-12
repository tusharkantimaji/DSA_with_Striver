# Time = n ^ 3
# Space = 1

def check(arr):
    result = arr[0]
    for i in arr[1:]:
        result ^= i
    return result

nums = [4, 2, 2, 6, 4]
k = 6
l = len(nums)
count = 0
for i in range(l):
    a = []
    for j in range(i, l):
        a.append(nums[j])
        if check(a) == k:
            count += 1
print(count)


