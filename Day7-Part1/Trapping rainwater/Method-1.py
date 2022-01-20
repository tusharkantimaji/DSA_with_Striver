# Time - n^2
# Space - 1

height = [0,1,0,2,1,0,1,3,2,1,2,1]
water = 0
l = len(height)
for i in range(l):
    max_left = 0
    max_right = 0
    for j in range(i):
        max_left = max(max_left, height[j])
    for j in range(i+1, l):
        max_right = max(max_right, height[j])
    water += max(0, min(max_left, max_right) - height[i])
print(water)

