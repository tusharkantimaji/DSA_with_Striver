# Time - n
# Space - n

arr = [4, 3, 6, 2, 1, 1] #  1 1 2 3 4 6
demo = [0] * len(arr)
for i in arr:
    demo[i-1] += 1
for i in range(len(demo)):
    if demo[i] == 2:
        re = i+1
    elif demo[i] == 0:
        mi = i+1
print(re, mi)