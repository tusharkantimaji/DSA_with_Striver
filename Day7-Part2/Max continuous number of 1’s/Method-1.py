# Time = n
# Space = 1

nums = [1,1,0,1,1,1]
m_c = 0
c = 0
for i in nums:
    if i == 1:
        c += 1
    else:
        m_c = max(m_c, c)
        c = 0
m_c = max(m_c, c)
print(m_c)


