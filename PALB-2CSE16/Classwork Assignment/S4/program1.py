def isSubset(a, b):
    # Sort both arrays
    a.sort()
    b.sort()

    # Initialize pointers for both arrays
    i = 0
    j = 0

    # Traverse both arrays
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] == b[j]:
            i += 1
            j += 1
        else:
            return False

    # If we have traversed all elements of b, then it is a subset of a
    return j == len(b)

# Example usage:
a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
result = isSubset(a, b)
print(result)