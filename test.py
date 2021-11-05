
# array of nums, sorted ascending
n = 5
bad = 4


def isBadVersion(n):
    if n > 4:
        return False
    else:
        return True


def firstBadVersion(n):

    left, right = 1, n

    while left <= right:
        version = left + (right - left) // 2  # the current version to test
        check1 = isBadVersion(version)
        check2 = isBadVersion(version + 1)  # API call -> minimize
        
        versionCheck = check1 + check2

        if versionCheck == 1:
            print(version)
            return version + 1

        elif versionCheck == 2:
            left = version

        else:
            right = version


firstBadVersion(5)
