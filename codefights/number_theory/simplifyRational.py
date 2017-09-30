def missingNumber(arr):
    sum_all = len(arr) * (len(arr)+1)/2
    return sum_all - sum(arr)

