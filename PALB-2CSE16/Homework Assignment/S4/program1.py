class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        common = []
        
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                if not common or common[-1] != arr1[i]:  # Avoid duplicates
                    common.append(arr1[i])
                i += 1
                j += 1
                k += 1
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        return common if common else [-1]
    
# Example usage:

solution = Solution()
arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(solution.commonElements(arr1, arr2, arr3))