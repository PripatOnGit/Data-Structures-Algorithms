'''Approach
1. Create a hash map to store the elements of the array and their indices.
2. Iterate through the array and for each element, calculate the complement (target - current element).
3. Check if the complement exists in the hash map. If it does, return the indices of the current element and the complement.
4. If the complement does not exist in the hash map, add the current element and its index to the hash map.
5. If no solution is found after iterating through the array, return None or an appropriate value indicating that no solution exists.
1. Initialize an empty hash map (dictionary) to store the elements and their indices.   
'''


def solution(arr, target):
    d = {}
    for i,j in enumerate(arr):
        #print(i,j)
        num = target - j
        if num in d:
            return (d[num],i)
        else:
            d[j] = i

arr = [4,5,7,6,2]
result = solution(arr, 10)
print(result)

