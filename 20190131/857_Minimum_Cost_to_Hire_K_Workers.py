"""
File: 857_Minimum_Cost_to_Hire_K_Workers.py
Date: 2019/02/21 15:31:36
"""
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        N, ret = len(quality), None
        ratio = sorted([(float(wage[i])/quality[i], i) for i in xrange(N)])
        works = []
        for r, i in ratio:
            bisect.insort(works, quality[i])
            if len(works) >= K:
                ret = sum(works[0:K]) * r if ret == None else min(ret, sum(works[0:K]) * r)

        return ret 
