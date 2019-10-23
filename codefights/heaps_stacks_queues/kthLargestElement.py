def kthLargestElement(nums, k):
    nums.sort()
    return nums[len(nums)-k]

