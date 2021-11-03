
# array of nums, sorted ascending
nums = [-1, 0, 3, 5, 9, 12]
target = 9


def binarySearch(array, target):

    # search target int in nums
    leftPointer, rightPointer = 0, (len(array) - 1)

    while leftPointer <= rightPointer:
        mid = leftPointer + (rightPointer - leftPointer) // 2
        test = array[mid]
        if target == test:
            print(mid)
            return mid
        elif target < test:
            rightPointer = mid - 1
        else:
            leftPointer = mid + 1
    print('-1')
    return -1  # target not in array

    # 0(log n) runtime


binarySearch(nums, target)