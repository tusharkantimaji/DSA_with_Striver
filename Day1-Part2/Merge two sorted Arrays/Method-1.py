# Time = n logn
# Space = 1

arr = [2, 5, 9, 6, 9, 3, 8, 4, 7, 1]
arr.sort()
l = len(arr)
for i in range(l-1):
    if arr[i] == arr[i+1]:
        print(arr[i])
        break