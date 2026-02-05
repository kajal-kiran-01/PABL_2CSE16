# Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

# Note: The kth smallest element is determined based on the sorted order of the array.

# Examples :
# Input: arr[] = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10], k = 4
# Output: 5

# Explanation: 4th smallest element in the given array is 5.

# Link: practice.geeksforgeeks.org/problems/kth-smallest-element/0

class solution:
    def kth_smallest(self, arr, k):
        # Sort the array using a simple sorting algorithm (e.g., bubble sort)
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr[k-1]

obj = solution()
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]

k = 4

result = obj.kth_smallest(arr, k)
print("Kth smallest element is:", result)