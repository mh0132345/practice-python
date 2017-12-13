def findLongestSubarrayBySum(s, arr):
    if len(arr) == 1:
        if arr[0] != s:
            return [-1]
        else:
            return [1,1]

    max_len, sum = 0, 0               
    answer = [-1]
    sumDict = {0:-1}                   
    for i in range(len(arr)):
        sum += arr[i]
        if sum not in sumDict:
            sumDict[sum] = i
        if sum-s in sumDict:           
            prevIndex = sumDict[sum-s]
            if max_len < i-prevIndex:
                max_len = i-prevIndex
                answer = [prevIndex+2,i+1]    
    return answer
