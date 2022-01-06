# Time = n log n + n
# Space = n

arr =  [[1,4],[4,5]] #[[1,6],[8,10],[15,18]]
arr.sort(key = lambda x: x[0])
# print(arr)
ans = []
target = arr[0]
for i in arr:
    if i[0] <= target[1]:
        target = [target[0], max(target[1], i[1])]
    else:
        ans.append(target)
        target = i
ans.append(target)
print(ans)