"""
File: 930_Binary_Subarrays_With_Sum.py
Author: zhaodongpo(zhaodongpo@baidu.com)
Date: 2019/02/17 17:00:19
"""
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        ret = 0
        counter = collections.defaultdict(int)
        counter[0] = 1
        pre_sum = 0
        for a in A:
            pre_sum += a
            ret += counter[pre_sum - S]
            counter[pre_sum] += 1
        return ret
