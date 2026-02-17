from typing import List
class Solution:
    def merge(self, a: List[int], b: List[int]) -> None:
        n = len(a)
        m = len(b)

        for i in range(n):
            if a[i] > b[0]:
                a[i], b[0] = b[0], a[i]
                first = b[0]

                k = 1
                while k < m and b[k] < first:
                    b[k - 1] = b[k]
                    k += 1
                b[k - 1] = first

# Example usage:

solution = Solution()
a = [2, 4, 7, 10]
b = [2, 3]
solution.merge(a, b)

print("Merged a:", a)
print("Merged b:", b)   