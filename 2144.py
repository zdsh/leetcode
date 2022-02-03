class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)
        ret = 0
        for i, c in enumerate(cost):
            if (i+1) % 3 == 0:
                continue
            ret += c
        return ret
