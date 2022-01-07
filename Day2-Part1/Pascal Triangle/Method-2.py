# If they told you to print the element of R row and C column
# The formula is (R-1)C(c-1)
# and the formula of nCr is n*(n-1)*(n-2).../r*(r-1)*(r-2).... The element in up and down are same

# Time = c
# sapce = 1

r = 9
c = 5
r -= 1
c -= 1
ans = 1
for i in range(c, 0, -1):
    ans *= r/i
    r-=1
print(int(ans))

