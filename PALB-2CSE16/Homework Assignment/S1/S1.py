# You are given an array of integers. You heve to reverse the given array.
# NOTE : Modify the arreey in place.

class solution:
    def reverse_array(self, arr):

        # return arr[::-1] #Wrong Soultion

        left,right = 0,len(arr)-1

        while left < right:

            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1

        return arr


obj = solution()

arr = [1, 2, 3, 4, 5]

result = obj.reverse_array(arr)
print("Reversed Array:", result)