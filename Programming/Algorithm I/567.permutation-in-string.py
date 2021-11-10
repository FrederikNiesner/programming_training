#
# @lc app=leetcode id=567 lang=python
#
# [567] Permutation in String
#

# @lc code=start
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # ## Solution 1 - Compare window

        # ls1, ls2 = len(s1), len(s2)

        # # if substring longer than string
        # if ls1 > ls2:
        #     return False

        # # create a list with count of each alphabetic letter
        # A = [0] * ls1
        # for x in range(ls1):
        #     A[x] = ord(s1[x]) - ord('a')

        # B = [0] * ls2
        # for x in range(ls2):
        #     B[x] = ord(s2[x]) - ord('a')

        # # capture the number of letters in 26 array
        # target = [0] * 26
        # for x in s1:  # get each letter
        #     i = ord(x) - ord('a')  # get letter's ASCI number
        #     target[i] += 1

        # window = [0] * 26

        # for x in range(ls2 - ls1 + 1):  # get each letter
        #     for j in range(ls1):
        #         j = j + x
        #         i = ord(s2[j]) - ord('a')  # get letter's ASCI number
        #         window[i] += 1
        #     if window == target:
        #         return True
        #     window = [0] * 26

        # return False

        # ## Solution 2 - Use Collections and Two Pointers

        import collections
        target = collections.defaultdict(int)
        window = collections.defaultdict(int)

        i = 0
        j = len(s1)  # window: j - i

        for x in s1:
            target[x] += 1

        for x in s2[i:j]:  # set initial dict of same length s1
            window[x] += 1

        while j < len(s2):  # loop until end of window j == end of string s2

            if window == target:
                return True

            # if not True -> slide window 1 to the right
            window[s2[i]] -= 1  # Remove start character count of window
            if window[s2[i]] < 1:
                window.pop(s2[i])
            window[s2[j]] = window.get(s2[j], 0) + 1  # add next character count
            i += 1
            j += 1

        return window == target

# @lc code=end

