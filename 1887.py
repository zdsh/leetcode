class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        curValue, minValue = nums[0], nums[-1]
        curRet, ret = 0, 0
        for num in nums:
            if num == minValue:
                return ret + curRet
            elif num == curValue:
                curRet += 1
            else:
                ret += curRet
                curValue = num
                curRet += 1
