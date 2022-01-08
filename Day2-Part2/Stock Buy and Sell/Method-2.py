# Time = n
# Space = 1

p = [7,1,5,3,6,4]
s = p[0]
m = 0
for i in range(len(p)):
    if p[i] < s:
        s = p[i]
    if p[i] - s > m:
        m = p[i] - s
print(m)


