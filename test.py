
# array of nums, sorted ascending
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3


def rotateArray(nums, k):
    
    left, right = 0, len(nums)-1
    while k > 0:
        nums[left]


    """while k > 0:
        last = nums.pop()
        nums.insert(0, last) 
        k -= 1
        print(nums)
"""

rotateArray(nums, k)
