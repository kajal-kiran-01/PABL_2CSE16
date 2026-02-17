def find3Numbers(arr, target):
    # Sort the array
    arr.sort()

    # Traverse the array
    for i in range(len(arr) - 2):
        # Initialize two pointers
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return False

# Example usage:
arr = [1, 4, 45, 6, 10, 8]
target = 13
result = find3Numbers(arr, target)
print(result)