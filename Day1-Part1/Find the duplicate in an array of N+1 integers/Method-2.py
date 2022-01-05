# Time = n
# Space = n

arr = [2, 5, 9, 6, 9, 3, 8, 4, 7, 1]
s = set()
for i in arr:
    if i in s:
        print(i)
        break
    else:
        s.add(i)