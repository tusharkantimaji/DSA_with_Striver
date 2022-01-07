# Time = n
# Space = 1

def nextPermutation(N, arr):
    # code here
    for i in range(N-1, 0, -1):
        if arr[i-1] < arr[i]:
            break
    else:
        return arr[::-1]
    i -= 1
    for j in range(N-1, i, -1):
        if arr[j] > arr[i]:
            break
    arr[i], arr[j] = arr[j], arr[i]
    p = 1
    while p <= (N-i)//2:
        arr[i+p], arr[N-p] = arr[N-p], arr[i+p]
        p += 1
    return arr

print(nextPermutation(4, [1, 4, 3, 2]))