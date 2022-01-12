# Time = n
# Space = n (max 26 character, so we can tell 1)

s = "tmmzuxt"
length = len(s)
l = 0
r = 0
d = {}
ml = 0
while r < length:
    if s[r] in d and d[s[r]] >= l and d[s[r]] <= r:
        l = d[s[r]]+1
    ml = max(ml, r-l+1)
    d[s[r]] = r
    r += 1
print(ml)


