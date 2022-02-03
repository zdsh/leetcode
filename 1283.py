class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        s, e = 1, max(nums)
        while s < e:
            divisor = (s + e) / 2
            value = 0
            for num in nums:
                value += (num + divisor -1) / divisor
            if value > threshold:
                s = divisor + 1
            elif value <= threshold:
                e = divisor
          
        return (s + e) / 2
