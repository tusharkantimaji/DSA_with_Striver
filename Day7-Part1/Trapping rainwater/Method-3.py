# Time - n
# Space - 1

height = [0,1,0,2,1,0,1,3,2,1,2,1]
left = 0
right = len(height) -1
water = 0
left_max = 0
right_max = 0
while left <= right:
    if height[left] <= height[right]:
        left_max = max(left_max, height[left])
        water += max(0, left_max - height[left])
        left += 1
    else:
        right_max = max(right_max, height[right])
        water += max(0, right_max - height[right])
        right -= 1
print(water)