# Time = n^2
# Space = 1

arr =  [12, 11, 13, 5, 6, 7]
c = 0
l = len(arr)
for i in range(l):
    for j in range(i+1, l):
        if arr[i] > arr[j]:
            c += 1
print(c)

