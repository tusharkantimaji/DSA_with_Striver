# Time = n
# Space = 1

# Tortories Algorithm
arr = [10, 2, 5, 9, 6, 9, 3, 8, 4, 7, 1]
slow = arr[0]
fast = arr[0]
while True:
    slow = arr[slow]
    fast = arr[arr[fast]]
    if slow == fast:
        break
fast = arr[0]
while slow != fast:
    slow = arr[slow]
    fast = arr[fast]
print(slow)