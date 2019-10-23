def containsCloseNums(nums, k):
    last_position = {}
    for i in range(len(nums)):
        if nums[i] in last_position.keys() and i-last_position[nums[i]]<=k:
            return True
        last_position[nums[i]] = i
        
    return False
        
