class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        s, e = 1, max(piles)
        while s < e:
            mid, c = (s + e) / 2, 0
            for pile in piles:
                c += (pile + mid - 1) / mid
            if c <= h:
                e = mid
            else:
                s = mid + 1
        return (s+e) / 2       
