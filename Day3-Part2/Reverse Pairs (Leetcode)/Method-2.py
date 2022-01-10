# Not Completed

# Using Marge Sort

# Time = n log n + n (for marge operiation) + n (for the counting algorithm)
# Space = n


def marge_sort(arr):
    count = 0
    if len(arr) > 1:
        div = len(arr) // 2
        left_arr = arr[:div]
        right_arr = arr[div:]
        count += marge_sort(left_arr)
        count += marge_sort(right_arr)
        p1, p2, p3 = 0, 0, 0
        while p1 < len(left_arr) and p2 < len(right_arr):
            
            if left_arr[p1] < right_arr[p2]:
                arr[p3] = left_arr[p1]
                p1 += 1
            else:
                arr[p3] = right_arr[p2]
                p2 += 1
            p3 += 1
        while p1 < len(left_arr):
            arr[p3] = left_arr[p1]
            p1 += 1
            p3 += 1
        while p2 < len(right_arr):
            arr[p3] = right_arr[p2]
            p2 += 1
            p3 += 1
    return count

arr = [2, 4, 3, 5, 1]
print("Ans = ", marge_sort(arr))
print(arr)



