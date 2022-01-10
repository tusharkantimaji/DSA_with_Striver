# Time = n^2
# Space = 1

arr = [2, 4, 3, 5, 1]
l = len(arr)
count = 0
for i in range(l):
    for j in range(i+1, l):
        if arr[i] > arr[j] * 2:
            count += 1
print(count)


