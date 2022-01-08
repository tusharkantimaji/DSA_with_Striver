# Time = n^2
# Space = 1

p = [7,1,5,3,6,4]
l = len(p)
m = 0
for i in range(l):
    for j in range(i+1, l):
        if  p[j] - p[i] > m:
            m = p[j] - p[i]
print(m)

