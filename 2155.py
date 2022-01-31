class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_0, num_1 = 0, 0
        for num in nums:
            num_1 += num == 1
        maxSocre, ret = num_1, [0]
        for i in range(1, len(nums)+1):
            num_0 += nums[i-1] == 0
            num_1 -= nums[i-1] == 1
            score = num_0 + num_1
            if score == maxSocre:
                ret.append(i)
            if score > maxSocre:
                maxSocre, ret = score, [i]
        return ret
        
