# Time - n log n + n
# Space 1

arr = [4, 3, 6, 2, 1, 1] #  1 1 2 3 4 6
arr.sort()
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        re = arr[i]
    elif arr[i+1] - arr[i] == 2:
        mi = arr[i] + 1
print(re, mi)