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