# You are given two arrays a[] and b[], return the Union of both the arrays in any order.

# The Union of two arrays is a collection of all distinct elements present in either of the arrays. If an element appears more than once in one or both arrays, it should be included only once in the result.

#Note: Elements of a[] and b[] are not necessarily distinct.
#Note that, You can return the Union in any order but the driver code will print the result in sorted order only.

# Input: a[] = [1, 2, 3, 2, 1], b[] = [3, 2, 2, 3, 3, 2]
# Output: [1, 2, 3]

# Explanation: Union set of both the arrays will be 1, 2 and 3.

# Link: https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1

class solution:
    def union_arrays(self, a, b):
        union_set = set()  # Using a set to store distinct elements

        # Add elements from the first array
        for num in a:
            union_set.add(num)

        # Add elements from the second array
        for num in b:
            union_set.add(num)

        return list(union_set)  # Convert the set back to a list before returning
    
obj = solution()

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

result = obj.union_arrays(a, b)
print("Union of arrays:", result)