def trapRainWater(arr):
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1
    left_max = 0
    right_max = 0
    trapped_water = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                trapped_water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                trapped_water += right_max - arr[right]
            right -= 1

    return trapped_water

# Example usage:
arr1 = [3, 0, 1, 0, 4, 0, 2]
result1 = trapRainWater(arr1)
print(result1)