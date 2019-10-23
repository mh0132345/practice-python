def arrayMaxConsecutiveSum2(inputArray):
    final_max = -1000
    curr_max = 0
     
    for i in range(0, len(inputArray)):
        curr_max = curr_max + inputArray[i]
        if final_max < curr_max:
            final_max = curr_max
        if curr_max < 0:
            curr_max = 0
    return final_max
