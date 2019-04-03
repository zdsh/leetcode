"""
File: 740_Delete_and_Earn.py
Date: 2019/04/03 19:48:42
"""
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1

        nums_sort = sorted(counter.keys())
        ret, i, n = 0, 0, len(nums_sort)
        while i < len(nums_sort):
            j = i + 1
            v0, v1 = 0, nums_sort[i] * counter[nums_sort[i]]
            dp = v1
            while j < n and nums_sort[j] == nums_sort[j-1] + 1:
                v2 = nums_sort[j] * counter[nums_sort[j]]
                dp = max(v1, v2+v0)
                v0, v1 = v1, dp
                j += 1
            ret += dp
            i = j
        return ret
