from cmath import pi


nums1, nums2, nums3 = [1,7,3,6,5,6], [1,2,3], [2,1,-1]
# output1, output2, output3 = 3, -1, 0

def pivotIndex(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    left = 0 
    right = 0

    for i in range(len(nums)):
        pivot = i
        right = sum(nums[i+1: len(nums)])
        if left == right: break
        left = sum(nums[:i+1])
        
    # print(pivot)
    return pivot
    
pivotIndex(nums3) 