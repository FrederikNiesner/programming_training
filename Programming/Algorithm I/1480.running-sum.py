
nums1, nums2 = [1,2,3,4] , [1,1,1,1,1]
sol1, sol2 = [1,3,6,10] , [1,2,3,4,5]

def runningSum(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    result = []
    y = 0

    for i in range(len(nums)): 
        x = nums[i]  
        z = x + y  
        result.append(z)
        y = z 

    return result

runningSum(nums1)