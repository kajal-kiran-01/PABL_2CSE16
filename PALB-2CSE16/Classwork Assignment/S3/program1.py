def minJumps(arr):

    n = len(arr)
    
    # If first element is 0, can't move forward
    if arr[0] == 0:
        return -1
    
    # If array has only one element, already at the end
    if n == 1:
        return 0
    
    jumps = 0
    current_max = 0  # Farthest index reachable with current jumps
    next_max = 0     # Farthest index reachable with one more jump
    
    for i in range(n - 1):
        next_max = max(next_max, i + arr[i])
        
        # If we've reached the farthest index with current jumps
        if i == current_max:
            jumps += 1
            current_max = next_max
            
            # If we can reach or pass the last index
            if current_max >= n - 1:
                return jumps
    
    return -1

# Example usage:
arr1 = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr1))