# Time = n ^ 2
# Space = n

s = "tmmzuxt"
l = len(s)
c = 0
for i in range(l):
    a = ''
    for j in range(i, l):
        a += s[j]
        if len(set(a)) == len(a):
            c = max(c, len(a))
print(c)


