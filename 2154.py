class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        record = {}
        for num in nums:
            record[num] = 1
        while original in record:
            original = original * 2
        return original
