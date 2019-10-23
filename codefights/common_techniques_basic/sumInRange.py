def sumInRange(nums, queries):
    sub_sum = [nums[0]]
    for i in range(1,len(nums)):
        sub_sum.append(sub_sum[i-1] + nums[i])
    
    sum = 0
    for query in queries:
        sum = sum + sub_sum[query[1]] - sub_sum[query[0]] + nums[query[0]]
    return sum%(10**9+7)

